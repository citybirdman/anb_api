# Copyright (c) 2024, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AnbPaymentLog(Document):
	def before_submit(self):
		self.flags.ignore_links = True
		self.ignore_linked_doctypes = ("Anb Payment Table", "Anb Log Queue")
		if self.validate_status():
			pass
			# self.create_payment()

	def validate_status(self):
		if self.status != "Failed":
			if not self.customer_name:
				self.status = "Failed"
				self.error = "The account number is not right or not linked to a customer"
				return False
		return True
		
	def create_payment(self):
		payment = frappe.get_doc("Payment Entry", dict(
			mode_of_payment = self.mode_of_payment,
			payment_type = "Recieve",
			party_type = "Customer",
			party = self.customer_name,
			amount = self.amount,
			reference_number = self.transaction_number,
			reference_date = self.date
		)).insert()
		payment.submit()