# Copyright (c) 2023, Ahmed Zaytoon and contributors
# For license information, please see license.txt
import json
import frappe
import requests
import frappe.utils.password as psswd
from frappe.model.document import Document

class ANBSettings(Document):
	def validate(self):
		ci = self.get_password("client_secret")
		self.validate_connection(self.url, self.client_id, ci)
		
	def validate_connection(self, url, ci, cs):
		protocol = "https://"
		server_url = f"{protocol}{url}/b2b-auth/oauth/accesstoken"
		payload = {
			"grant_type": "client_credentials",
			"client_id": ci,
			"client_secret": cs
		}
		encoded_payload = "&".join([f"{key}={value}" for key, value in payload.items()])
		headers = {"Content-Type": "application/x-www-form-urlencoded"}
		# making response text
		response = requests.post(server_url, data=encoded_payload, headers=headers)
		if response.status_code == 401:
			frappe.throw(json.loads(response.text)['error']['message'] + f"\nerror code:{response.status_code}", title="Error Connecting To The Bank Server!")
		elif response.status_code == 200:
			frappe.msgprint("Connection Accepted!", alert=True)
		elif response.status_code == 400:
			frappe.throw(json.loads(response.text)['message'] + f"\nerror code:{response.status_code}", title="Error Connecting To The Bank Server!")
