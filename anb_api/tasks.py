import frappe
import json
import requests
from frappe.utils import add_days, today, nowtime
def get_account_statment(account_number, settings, try_again=True, offset="", headers={}):
    from_date = add_days(today(), -7) 
    response = requests.get(f"https://test-api.anb.com.sa/v2/report/account/statement?accountNumber={account_number}&offset={offset}&type=JSON&fromDate={from_date}", headers=headers)
    if response.status_code != 200:
        if try_again:
            get_account_statment(account_number, settings, False, offset, headers)
        else:
            return {"account_number": account_number, "completed": False}
    else:
        return json.loads(response.text)
    
@frappe.whitelist()
def get_statments():
    settings = frappe.get_doc("ANB Settings")
    response = json.loads(settings.start_connection().text)
    headers = {
        "Authorization": f"Bearer {response['access_token']}",
        "Accept": "application/json"
    }
    results = []
    for account in settings.accounts:
        transactions, offset, num_of_trcn = [], "", 0
        while result := get_account_statment(account.account_number, settings, True, offset, headers):
            offset = result["offset"]
            num_of_trcn += result["numberOfRecords"]
            if result["statement"]:
                transactions.extend(result["statement"]["transactions"])
            if result["completed"]:
                result["statement"]["transactions"] = transactions
                result["numberOfRecords"] = num_of_trcn
                break
                
        results.append(result)

    return results

@frappe.whitelist()
def check_latest_failed_logs(account_number):
    last_doc = frappe.get_list("Anb Log Queue", filters=[["account_number", "=", account_number], ["docstatus", "=", 1]], fields=['name', 'status'], order_by='creation desc', limit=1)
    failed_transactions = []
    if isinstance(last_doc, list) and len(last_doc) == 1:
        if last_doc[0].status == "Failed":
            frappe.db.set_value("Anb Log Queue", last_doc[0].name, "status", "Discarded")
        failed_payments = []
        if last_doc[0].status != "Completed":
            failed_payments = frappe.get_list("Anb Payment Log", filters={"status": "Failed", "log_queue": last_doc[0].name}, fields=["transaction_number"])
        if failed_payments:
            for payment in failed_payments:
                failed_transactions.append(payment.transaction_number)
    return failed_transactions

@frappe.whitelist()
def make_bank_logs():
    bank_responses = get_statments()
    for bank_response in bank_responses:
        company_account_number = bank_response.get("accountNumber")
        if isinstance(bank_response, dict) and bank_response.get("statement") and bank_response.get("statement").get("transactions"):
            failed_transactions = check_latest_failed_logs(company_account_number)
            transactions = bank_response.get("statement").get("transactions")
            (mode_of_payment, company, currency) = frappe.db.get_value("Anb Settings Table", [["account_number", "=", company_account_number]], ["mode_of_payment", "company", "currency"])
            queue = frappe.get_doc(dict(
                doctype = "Anb Log Queue",
                posting_date = today(),
                posting_time = nowtime(),
                company = company,
                account_number = company_account_number
            )).insert()
            queue_logs = []
            for transaction in transactions:
                if (not frappe.db.get_value("Anb Payment Table", [["transaction_number", "=", transaction["refNum"]], ["docstatus", "=", 1]]) 
                    or transaction["refNum"] in failed_transactions
                ):
                    customer = frappe.db.get_value("Customer", [["anb_bank_account", "=", transaction.get("srcAcctNum") or ""]], ["name", "anb_bank_account"], as_dict=True)
                    if transaction.get("srcAcctNum"):
                        failed_log = frappe.db.get_value("Anb Payment Log", [[ "transaction_number", "=", transaction["refNum"]], ["status", "=", "Failed"]], ["name", "status"], as_dict=True)
                        payment_log = frappe.get_doc(dict(
                            doctype = "Anb Payment Log",
                            company = company,
                            transaction_number = transaction["refNum"],
                            customer_name = customer.name if customer else "",
                            bank_account_number = customer.anb_bank_account if customer else transaction.get("srcAcctNum"),
                            company_account_number = bank_response.get("accountNumber"),
                            date = transaction["valueDate"],
                            time = transaction["postingTime"],
                            amount = transaction["amount"].get("amount"),
                            currency= transaction["amount"].get("currencyCode"),
                            dflt_currency = currency,
                            channel= transaction["channel"],
                            network= transaction["network"],
                            type = transaction["type"],
                            mode_of_payment = mode_of_payment,
                            log_queue = queue.name,
                            log= str(transaction),
                            failed_log= failed_log.name if failed_log else ""   
                        )).insert()
                        if failed_log:
                            frappe.db.set_value("Anb Payment Log", failed_log.name, "status", "Discarded")
                        payment_log.flags.ignore_links = True
                        payment_log.submit()
                        queue_logs.append(dict(
                            transaction_number = transaction["refNum"],
                            payment_log = payment_log.name
                        ))
            if queue_logs:
                queue.set("logs", queue_logs)
                queue.submit()
            else:
                queue.delete()

