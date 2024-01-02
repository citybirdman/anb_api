import frappe
import requests
@frappe.whitelist()
def get_balance():
    settings = frappe.get_doc("ANB Settings")
    settings.start_connection()
    headers = {
        "Authorization": f"Bearer {settings['access_token']}",
        "Accept": "application/json"
    }
    account_number = "0108095164500016"
    from_date = "2023-12-25"
    auth = requests.get(f"https://test-api.anb.com.sa/v2/report/account/statement?accountNumber={account_number}&offset=Offset&type=JSON&fromDate={from_date}", headers=headers)
    return auth