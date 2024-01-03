import frappe
import json
import requests
from frappe.utils import add_days, today
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