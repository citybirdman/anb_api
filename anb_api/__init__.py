import frappe, requests
__version__ = '1.0.0'
@frappe.whitelist()
def get_public_ip():
    try:
        # Use a reliable service to get your public IP
        response = requests.get("https://api64.ipify.org?format=json")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and print the public IP
            public_ip = response.json()["ip"]
            frappe.msgprint(f"Your public IP address is: {public_ip}")
        else:
            print(f"Failed to retrieve public IP. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")