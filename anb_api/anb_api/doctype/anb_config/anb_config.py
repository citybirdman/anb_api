# Copyright (c) 2023, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AnbConfig(Document):
	def validate(self):
		try:
		# if True:
			api_endpoint = "https://test-api.anb.com.sa/v1/b2b-auth/oauth/accesstoken"
			data = {
				"grant_type": "client_credentials",
				"client_id": "Fo4Qaom8ydJHGzrUMMRGGBx2zHIQ3p1V",
				"client_secret": "fu9yf4ojqPhd6pgk",
				"X-Forwarded-For": "15.184.183.167"
			}
			headers= {
				"X-Forwarded-For": "15.184.183.167"
				
			}
			
			# Make a POST request using frappe.post_request
			response = frappe.make_post_request(api_endpoint,headers=headers, data=data)
		except:
			frappe.throw(str(frappe.request.headers))