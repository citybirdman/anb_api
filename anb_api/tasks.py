import frappe
import json
import requests
from frappe.utils import add_days, today, nowtime
def get_account_statment(account_number, settings, try_again=True, headers={}):
    from_date = add_days(today(), -7) 
    response = requests.get(f"https://test-api.anb.com.sa/v2/report/account/statement?accountNumber={account_number}&offset=Offset&type=JSON&fromDate={from_date}", headers=headers)
    if response.status_code != 200:
        if try_again:
            get_account_statment(account_number, settings, False)
        else:
            return {"account_number": account_number, "completed": False}
    else:
        return json.loads(response.text)

def get_statments():
    settings = frappe.get_doc("ANB Settings")
    response = json.loads(settings.start_connection().text)
    headers = {
        "Authorization": f"Bearer {response['access_token']}",
        "Accept": "application/json"
    }
    results = []
    for account in settings.accounts:
        results.append(get_account_statment(account.account_number, settings, True, headers))
    return results

@frappe.whitelist()
def make_bank_logs():
    bank_response = get_statments()
    if isinstance(bank_response, dict) and bank_response.get("statement").get("transactions"):
        transactions = bank_response.get("statement").get("transactions")
        logs = []
        for transaction in transactions:
            customer = frappe.db.get_value("Customer", [["anb_bank_account", "=", transaction["narrative"]["narr3"]]], ["name", "anb_bank_account"], as_dict=True)
            payment_log = frappe.get_doc(dict(
                doctype = "Anb Payment Log",
                transaction_number = transaction["refNum"],
                customer_name = customer.name if customer else "",
                bank_account_number = customer.anb_bank_account if customer else transaction["narrative"]["narr3"],
                date = transaction["valueDate"],
                time = transaction["postingTime"],
                amount = transaction["amount"].get("amount"),
                currency= transaction["amount"].get("currencyCode"),
                channel= transaction["channel"],
                network= transaction["network"],
                type = transaction["type"],
                log= str(transaction)
            )).insert()
            payment_log.save()
            logs.append(dict(
                transaction_number = transaction["refNum"],
                payment_log = payment_log.name
            ))
        
        queue = frappe.get_doc(dict(
            doctype = "Anb Log Queue",
            posting_date = today(),
            posting_time = nowtime(),
            logs = logs,
        )).insert()
        queue.save()

