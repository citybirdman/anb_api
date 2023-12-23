# Copyright (c) 2023, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document

class AnbConfig(Document):
	def validate(self):
		# Set your server URL
		server_url = "https://test-api.anb.com.sa/v1/b2b-auth/oauth/accesstoken"

		# Set the IP address for X-Forwarded-For header
		custom_ip_address = "15.184.183.167"

		# Set your payload (adjust accordingly)
		payload = {
			"grant_type": "client_credentials",
			"client_id": "Fo4Qaom8ydJHGzrUMMRGGBx2zHIQ3p1V",
			"client_secret": "fu9yf4ojqPhd6pgk"
		}
		encoded_payload = "&".join([f"{key}={value}" for key, value in payload.items()])
		# Set headers including X-Forwarded-For
		headers = {
			"X-Forwarded-For": custom_ip_address,
			"Content-Type": "application/x-www-form-urlencoded",
		}

		# Add any additional headers you may need
		# headers["Another-Header"] = "header_value"

		# Make the POST request
		response = requests.post(server_url, data=encoded_payload, headers=headers)


		# Print the response
		if self.sc:
			self.get_public_ip()
		else:
			frappe.throw(str(response.text))
		# # try:
		# # if True:
		# api_endpoint = "https://test-api.anb.com.sa/v1/b2b-auth/oauth/accesstoken"
		# data = {
		# 	"grant_type": "client_credentials",
		# 	"client_id": "Fo4Qaom8ydJHGzrUMMRGGBx2zHIQ3p1V",
		# 	"client_secret": "fu9yf4ojqPhd6pgk",
		# 	"X-Forwarded-For": "15.184.183.167"
		# }
		# headers= {
		# 	"X-Forwarded-For": "15.184.183.167"
			
		# }
		
		# # Make a POST request using frappe.post_request
		# frappe.throw(str(frappe.get_server()))
		# # response = frappe.make_post_request(api_endpoint,headers=headers, data=data)
		# # except:
		# # 	frappe.throw(str(frappe.request.headers))

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