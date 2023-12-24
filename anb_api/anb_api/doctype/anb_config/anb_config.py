# Copyright (c) 2023, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document

class AnbConfig(Document):
	def validate(self):
		# Set your server URL
		server_url = "https://test-api.anb.com.sa/v1/b2b-auth/oauth/accesstoken"

		# Set your payload (adjust accordingly)
		payload = {
			"grant_type": "client_credentials",
			"client_id": "Fo4Qaom8ydJHGzrUMMRGGBx2zHIQ3p1V",
			"client_secret": "fu9yf4ojqPhd6pgk"
		}

		# convert the payload to acceptable value
		encoded_payload = "&".join([f"{key}={value}" for key, value in payload.items()])

		# Set the headers
		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
		}

		response = requests.post(server_url, data=encoded_payload, headers=headers)


		# Print the response
		if self.sc:
			self.get_public_ip()
		else:
			self.make_payment()

	def get_public_ip(self):
		try:
			# Use a reliable service to get your public IP
			response = requests.get("https://api64.ipify.org?format=json")

			# Check if the request was successful (status code 200)
			if response.status_code == 200:
				# Parse the JSON response and print the public IP
				public_ip = response.json()["ip"]
				frappe.throw(f"Your public IP address is: {public_ip}")
			else:
				print(f"Failed to retrieve public IP. Status code: {response.status_code}")
		except Exception as e:
			print(f"An error occurred: {e}")

	def make_payment(self):
		headers = {
			"Accept": "application/json",
			"Content-Type": "application/json",
			"Authorization": (f"Bearer {self.access_token}"),
		}
		api_endpoint = "https://test-api.anb.com.sa/v1/payment/json"
		data = {
			"sequenceNumber": "200000879",
			"valueDate": "1702534805",
			"currency": "SAR",
			"amount": "1900",
			"orderingParty": "SWAGGER",
			"feeIncluded": False,
			"orderingPartyAddress1": "An Nafel",
			"orderingPartyAddress2": "Riyadh",
			"orderingPartyAddress3": "Saudi Arabia",
			"debitAccount": "0108057386290014",
			"destinationBankBIC": "ARNBSARI",
			"channel": "ANB",
			"creditAccount": "0108061198800019",
			"beneficiaryName": "Saud",
			"beneficiaryAddress1": "KSA",
			"beneficiaryAddress2": "Riyadh",
			"narrative": "ANB To ANB Transfer",
			"transactionComment": "ANB to ANB works",
			"purposeOfTransfer": "38",
		}

		# # Make a POST request using frappe.post_request
		auth = requests.post(api_endpoint, headers=headers,json=data)
		frappe.throw(str(auth.text))