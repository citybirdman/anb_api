import frappe
import json
import requests
from frappe.utils import add_days, today
@frappe.whitelist(try_again=True)
def get_balance():
    settings = frappe.get_doc("ANB Settings")
    response = json.loads(settings.start_connection().text)
    headers = {
        "Authorization": f"Bearer {response['access_token']}",
        "Accept": "application/json"
    }
    account_number = "0108095164500016"
    from_date = add_days(today(), -7) 
    response = requests.get(f"https://test-api.anb.com.sa/v2/report/account/statement?accountNumber={account_number}&offset=Offset&type=JSON&fromDate={from_date}", headers=headers)
    if response.status_code != 200:
        if try_again:
            try_again = False
            get_balance()
    else:
        return response.text
