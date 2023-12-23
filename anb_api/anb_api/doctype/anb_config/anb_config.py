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