
__version__ = '0.1.0'
import frappe
import json
import requests
from frappe.utils import add_days, today
@frappe.whitelist()
def get_account_statment(account_number, settings, try_again=True, offset="", headers={}, days = 7):
    from_date = add_days(today(), -days) 
    response = requests.get(f"https://test-api.anb.com.sa/v2/report/account/statement?accountNumber={account_number}&offset={offset}&type=JSON&fromDate={from_date}", headers=headers)
    if response.status_code != 200:
        if try_again:
            get_account_statment(account_number, settings, False, offset, headers, days)
        else:
            return {"account_number": account_number, "completed": False}
    else:
        return json.loads(response.text)
    