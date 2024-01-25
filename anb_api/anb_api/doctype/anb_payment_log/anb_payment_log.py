# Copyright (c) 2024, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AnbPaymentLog(Document):
	def before_submit(self):
		self.flags.ignore_links = True
		self.ignore_linked_doctypes = ("Anb Payment Table", "Anb Log Queue")
		self.validate_status()

	def validate_status(self):
		if not self.customer_name:
			self.status = "Failed"
			self.error = "The account number is not right or not linked to a customer"
		
	def create_payments(self):
		frappe.get_doc("Payment Entry", dict(
			payment_type = "Recieve",
			party_type = "Customer",
			party = self.customer_name,
			amount = self.amount,
			reference_number = self.transaction_number,
			reference_date = self.date
		)).insert()