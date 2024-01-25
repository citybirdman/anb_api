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
    return [{'accountNumber': '0108095164500016', 'fromDate': '2024-01-18', 'toDate': '2024-01-25', 'numberOfRecords': 20, 'completed': False, 'offset': '18-01-2024SDC230700      2   18-01-202403:01:030000000014963026.46', 'broughtFrwdBalance': {'amount': 14965741.6, 'currencyCode': 'SAR'}, 'openingClrBalance': {'amount': 14965741.6}, 'pageOpenBalance': {'amount': 14965741.6, 'currencyCode': 'SAR'}, 'closingBalance': {'amount': 14963026.46, 'currencyCode': 'SAR'}, 'statement': {'transactions': [{'postDate': '2024-01-18', 'postingTime': '10:20:13', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -5.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072112-هدايا وجوائز', 'narr2': 'Referral reward from Cashee', 'narr3': '3532402469631238'}, 'refNum': 'SDC230446', 'counter': '1', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14965736.15, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072112-هدايا وجوائزReferral reward from Cashee3532402469631238', 'network': '01', 'channel': 'ANB'}, {'postDate': '2024-01-18', 'postingTime': '12:58:43', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 100, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072139-تحويل استثماري', 'narr2': 'B2B OUTGOING - 916', 'narr3': '916'}, 'refNum': 'SDC230489', 'counter': '2', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14965836.15, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00072139-تحويل استثماريB2B OUTGOING - 916916', 'network': '01', 'channel': 'ANB'}, {'postDate': '2024-01-18', 'postingTime': '13:25:30', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -5.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072142-هدايا وجوائز', 'narr2': 'Referral reward from Cashee', 'narr3': '1852216723825285'}, 'refNum': 'SDC230493', 'counter': '3', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14965830.7, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072142-هدايا وجوائزReferral reward from Cashee1852216723825285', 'network': '01', 'channel': 'ANB'}, {'postDate': '2024-01-18', 'postingTime': '14:07:27', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -508.57, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072148', 'narr2': 'CSO20240118-2RIF1I7J', 'narr3': '2024011895205121'}, 'refNum': 'SDC230496', 'counter': '4', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14965322.13, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072148CSO20240118-2RIF1I7J2024011895205121', 'network': '01', 'channel': 'ANB', 'prtclrsCode': '16IPI'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '14:08:15', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 508, 'currencyCode': 'SAR'}, 'narrative': {'narr1': '20240118SAARNBARNB1B21911404236810', 'narr2': 'BT00072148', 'narr3': 'AC02'}, 'refNum': 'SDC230497', 'counter': '5', 'stmt': 'Y', 'srcAcctNum': 'I011660104991051', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14965830.13, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'iban': 'I011660104991051', 'samaNarr': '20240118SAARNBARNB1B21911404236810BT00072148AC02', 'network': '01', 'channel': 'ANB', 'category': '000SJ', 'subCategory': 'SJBB6', 'prtclrsCode': 'SJBB6'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '14:14:59', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -5.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072150-هدايا وجوائز', 'narr2': 'Referral reward from Cashee', 'narr3': '2183349660911047'}, 'refNum': 'SDC230498', 'counter': '6', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14965824.68, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072150-هدايا وجوائزReferral reward from Cashee2183349660911047', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '16:36:22', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -28.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072173-خدمات أو مدفوعات', 'narr2': 'CSO20240118-9FN4FCIA', 'narr3': '2024011897274595'}, 'refNum': 'SDC230546', 'counter': '7', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14965796.23, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072173-خدمات أو مدفوعاتCSO20240118-9FN4FCIA2024011897274595', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '16:38:22', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -28.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072174-خدمات أو مدفوعات', 'narr2': 'CSO20240118-KKISJVTY', 'narr3': '2024011809918502'}, 'refNum': 'SDC230547', 'counter': '8', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14965767.78, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072174-خدمات أو مدفوعاتCSO20240118-KKISJVTY2024011809918502', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '16:49:13', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 200, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072180-تحويل استثماري', 'narr2': 'B2B OUTGOING - 923', 'narr3': '923'}, 'refNum': 'SDC230554', 'counter': '9', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14965967.78, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00072180-تحويل استثماريB2B OUTGOING - 923923', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '17:00:42', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -1000.57, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072188', 'narr2': 'CSO20240118-F82HGR03', 'narr3': '2024011879202703'}, 'refNum': 'SDC230562', 'counter': '10', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14964967.21, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072188CSO20240118-F82HGR032024011879202703', 'network': '01', 'channel': 'ANB', 'prtclrsCode': '16IPI'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '22:04:50', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -3503.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072221-تحويل استثماري', 'narr2': 'B2B OUTGOING - 915', 'narr3': '915'}, 'refNum': 'SDC230610', 'counter': '11', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14961463.76, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072221-تحويل استثماريB2B OUTGOING - 915915', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '22:05:20', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -83.95, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072222-تحويل استثماري', 'narr2': 'B2B OUTGOING - 916', 'narr3': '916'}, 'refNum': 'SDC230611', 'counter': '12', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14961379.81, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072222-تحويل استثماريB2B OUTGOING - 916916', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '22:08:15', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 1500, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072223-تحويل استثماري', 'narr2': 'B2B OUTGOING - 919', 'narr3': '919'}, 'refNum': 'SDC230612', 'counter': '13', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14962879.81, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00072223-تحويل استثماريB2B OUTGOING - 919919', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '02:05:21', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -53.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072224-تحويل استثماري', 'narr2': 'B2B OUTGOING - 904', 'narr3': '904'}, 'refNum': 'SDC230660', 'counter': '14', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14962826.36, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072224-تحويل استثماريB2B OUTGOING - 904904', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '02:36:00', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -1003.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072225-تحويل استثماري', 'narr2': 'B2B OUTGOING - 908', 'narr3': '908'}, 'refNum': 'SDC230695', 'counter': '15', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14961822.91, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072225-تحويل استثماريB2B OUTGOING - 908908', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '02:58:53', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': -26.45, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072226-تحويل استثماري', 'narr2': 'B2B OUTGOING - 11412412129909', 'narr3': '11412412129909'}, 'refNum': 'SDC230696', 'counter': '16', 'stmt': 'Y', 'partTrnType': 'DEBIT', 'partTrnSrlNum': '1', 'runningBalance': {'amount': 14961796.46, 'currencyCode': 'SAR'}, 'orderingParty': 'CORPORATE_NAME', 'samaNarr': 'BT00072226-تحويل استثماريB2B OUTGOING - 1141241212990911412412129909', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '03:00:02', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 100, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072144-مدفوعات تجارية', 'narr2': '01080910016', 'narr3': '1100893130'}, 'refNum': 'SDC230697', 'counter': '17', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14961896.46, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00072144-مدفوعات تجارية010809100161100893130', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '03:00:08', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 100, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072145-مدفوعات تجارية', 'narr2': '01080910016', 'narr3': '1100893131'}, 'refNum': 'SDC230698', 'counter': '18', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14961996.46, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00072145-مدفوعات تجارية010809100161100893131', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '03:00:30', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 30, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00071703-مدفوعات تجارية', 'narr2': '0108095164500016', 'narr3': '1100893124'}, 'refNum': 'SDC230699', 'counter': '19', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14962026.46, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00071703-مدفوعات تجارية01080951645000161100893124', 'network': '01', 'channel': 'ANB'}, {'uniqueId': 'SDC23049718-01-2024   2', 'postDate': '2024-01-18', 'postingTime': '03:01:03', 'valueDate': '2024-01-18', 'type': '56', 'amount': {'amount': 1000, 'currencyCode': 'SAR'}, 'narrative': {'narr1': 'BT00072227-تحويل استثماري', 'narr2': 'B2B OUTGOING - 4856071888910', 'narr3': '4856071888910'}, 'refNum': 'SDC230700', 'counter': '20', 'stmt': 'Y', 'partTrnType': 'CREDIT', 'partTrnSrlNum': '2', 'runningBalance': {'amount': 14963026.46, 'currencyCode': 'SAR'}, 'beneficiaryName': 'CORPORATE_NAME', 'samaNarr': 'BT00072227-تحويل استثماريB2B OUTGOING - 48560718889104856071888910', 'network': '01', 'channel': 'ANB'}]}}]
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
    bank_responses = get_statments()
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
                        amount = - transaction["amount"].get("amount"),
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

