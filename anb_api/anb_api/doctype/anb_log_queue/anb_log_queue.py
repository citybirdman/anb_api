# Copyright (c) 2024, Ahmed Zaytoon and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AnbLogQueue(Document):
	def validate(self):
		self.flags.ignore_links = True
		self.ignore_linked_doctypes = ("Anb Payment Log",)
		self.set_status()

	def set_status(self):
		count_of_failed = frappe.db.get_value("Anb Payment Log", [["log_queue", "=", self.name], ["status", "=", "Failed"]], "count(name)")
		if count_of_failed != 0:
			if count_of_failed < len(self.logs):
				self.status = "Partially Complete"
			else:
				self.status = "Failed"
	
	def on_cancel(self):
		for log in self.get("logs"):
			pl = frappe.get_doc("Anb Payment Log", log.payment_log)
			pl.cancel()

	def on_trash(self):
		for log in self.get("logs"):
			pl = frappe.get_doc("Anb Payment Log", log.payment_log)
			pl.delete(force=True, ignore_permissions=True, delete_permanently=True)