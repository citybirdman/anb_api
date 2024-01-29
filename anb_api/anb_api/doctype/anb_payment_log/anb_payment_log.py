# Copyright (c) 2024, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AnbPaymentLog(Document):
	def before_submit(self):
		self.flags.ignore_links = True
		self.ignore_linked_doctypes = ("Anb Payment Table", "Anb Log Queue")
		self.update_status()
		if self.validate_status() and frappe.db.get_value("Anb Settings", "Anb Settings", "auto_create_payment") == "1":
			self.create_payment()
	def update_status(self):
		if self.status != "Failed":
			if not self.customer_name:
				self.status = "Failed"
				self.error = "The account number is not right or not linked to a customer"

	def validate_status(self):
		if self.status == "Success":
			return True
		return False

	def create_payment(self):
		payment = frappe.get_doc(dict(
			doctype = "Payment Entry",
			mode_of_payment = self.mode_of_payment,
			payment_type = "Receive",
			party_type = "Customer",
			party = self.customer_name,
			paid_amount = self.amount,
			source_exchange_rate = 1,
			target_exchange_rate = 1,
			received_amount = self.amount,
			reference_no = self.transaction_number,
			reference_date = self.date,
			paid_to = frappe.db.get_value("Mode of Payment Account", [["parent", "=", self.mode_of_payment], ["company", "=", self.company]], "default_account"),
			paid_to_account_currency = self.currency,
			payment_log = self.name
		)).insert()
		payment.submit()