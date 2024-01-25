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
        results.append(get_account_statment(account.account_number, settings, True, headers))
    return results

@frappe.whitelist()
def check_latest_failed_logs():
    last_doc = frappe.get_list("Anb Log Queue", fields=['name', 'status'], order_by='creation desc', limit=1)
    failed_transactions = []
    if isinstance(last_doc, list) and len(last_doc) == 1:
        failed_payments = []
        if last_doc[0].status != "Completed":
            failed_payments = frappe.get_list("Anb Payment Log", filters={"status": "Failed", "log_queue": last_doc[0].name}, fields=["transaction_number"])
        if failed_payments:
            for payment in failed_payments:
                failed_transactions.append(payment.transaction_number)
    return failed_transactions

@frappe.whitelist()
def make_bank_logs():
    # bank_responses = get_statments()
    bank_responses = []
    bank_responses.append({
  "accountNumber": "0108095164500016",
  "fromDate": "2023-12-27",
  "toDate": "2024-01-03",
  "numberOfRecords": 11,
  "completed": True,
  "offset": "28-12-2023SDC226508      1   28-12-202314:50:370000000014965439.60",
  "broughtFrwdBalance": {
    "amount": 14965741.6,
    "currencyCode": "SAR"
  },
  "openingClrBalance": {
    "amount": 14965741.6
  },
  "pageOpenBalance": {
    "amount": 14965741.6,
    "currencyCode": "SAR"
  },
  "closingBalance": {
    "amount": 14965439.6,
    "currencyCode": "SAR"
  },
  "statement": {
    "transactions": [
    	{
      "postDate": "2023-12-27",
      "postingTime": "16:22:38",
      "valueDate": "2023-12-27",
      "type": "56",
      "amount": {
        "amount": -7.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063216-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703683353177"
      },
      "refNum": "SDC226308",
      "counter": "1",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965734.15,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063216-مدفوعات تجاريةANB To ANB Transfer1703683353177",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "11:47:08",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -6.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063528-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703753226234"
      },
      "refNum": "SDC226371",
      "counter": "2",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965727.7,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063528-مدفوعات تجاريةANB To ANB Transfer1703753226234",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "11:47:22",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -7.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063529-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703753239641"
      },
      "refNum": "SDC226372",
      "counter": "3",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965720.25,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063529-مدفوعات تجاريةANB To ANB Transfer1703753239641",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "11:47:24",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -4.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063530-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703753242597"
      },
      "refNum": "SDC226373",
      "counter": "4",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965715.8,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063530-مدفوعات تجاريةANB To ANB Transfer1703753242597",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "11:47:46",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -8.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063531-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703753262966"
      },
      "refNum": "SDC226374",
      "counter": "5",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965707.35,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063531-مدفوعات تجاريةANB To ANB Transfer1703753262966",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "11:47:51",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -4.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063532-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703753266723"
      },
      "refNum": "SDC226375",
      "counter": "6",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965702.9,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063532-مدفوعات تجاريةANB To ANB Transfer1703753266723",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "11:51:38",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -6.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063533-مدفوعات تجارية",
        "narr2": "ANB To ANB Transfer",
        "narr3": "1703753493195"
      },
      "refNum": "SDC226378",
      "counter": "7",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965696.45,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063533-مدفوعات تجاريةANB To ANB Transfer1703753493195",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "14:11:04",
      "valueDate": "2023-12-28",
      "type": "59",
      "amount": {
        "amount": -211.5,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "/PAYROLL/  12030",
        "narr2": "elPss9DwSeq6ObqT",
        "narr3": "/PAYROLL/  QAANBPAYROL"
      },
      "refNum": "SDC226406",
      "counter": "8",
      "stmt": "Y",
      "srcAcctNum": "I013253901600001",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965484.95,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "/PAYROLL/  12030elPss9DwSeq6ObqT/PAYROLL/  QAANBPAYROL",
      "network": "02",
      "channel": "SARIE",
      "prtclrsCode": "16001"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "14:37:44",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -36.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063862-تحويل أموال",
        "narr2": "B2B OUTGOING - 88261900112",
        "narr3": "88261900112"
      },
      "refNum": "SDC226501",
      "counter": "9",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965448.5,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063862-تحويل أموالB2B OUTGOING - 8826190011288261900112",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "14:50:20",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -4.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063869-خدمات أو مدفوعات",
        "narr2": "B2B OUTGOING - 88261910113",
        "narr3": "88261910113"
      },
      "refNum": "SDC226505",
      "counter": "10",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965444.05,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063869-خدمات أو مدفوعاتB2B OUTGOING - 8826191011388261910113",
      "network": "01",
      "channel": "ANB"
    }, {
      "postDate": "2023-12-28",
      "postingTime": "14:50:37",
      "valueDate": "2023-12-28",
      "type": "56",
      "amount": {
        "amount": -4.45,
        "currencyCode": "SAR"
      },
      "narrative": {
        "narr1": "BT00063875-خدمات أو مدفوعات",
        "narr2": "B2B OUTGOING - 88261910115",
        "narr3": "88261910115"
      },
      "refNum": "SDC226508",
      "counter": "11",
      "stmt": "Y",
      "partTrnType": "DEBIT",
      "partTrnSrlNum": "1",
      "runningBalance": {
        "amount": 14965439.6,
        "currencyCode": "SAR"
      },
      "orderingParty": "CORPORATE_NAME",
      "samaNarr": "BT00063875-خدمات أو مدفوعاتB2B OUTGOING - 8826191011588261910115",
      "network": "01",
      "channel": "ANB"
    }]
  }
})
    failed_transactions = check_latest_failed_logs() if bank_responses else []
    for bank_response in bank_responses:
        if isinstance(bank_response, dict) and bank_response.get("statement").get("transactions"):
            transactions = bank_response.get("statement").get("transactions")
            queue = frappe.get_doc(dict(
                doctype = "Anb Log Queue",
                posting_date = today(),
                posting_time = nowtime()
            )).insert()
            queue_logs = []
            for transaction in transactions:
                if (not frappe.db.get_value("Anb Payment Table", [["transaction_number", "=", transaction["refNum"]]]) 
                    or transaction["refNum"] in failed_transactions
                ):
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
                        log_queue = queue.name,
                        log= str(transaction)
                    )).insert()
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

