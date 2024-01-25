# Copyright (c) 2024, Ahmed Zaytoon and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class AnbPaymentTable(Document):
	def validate(self):
		self.flags.ignore_links = True
