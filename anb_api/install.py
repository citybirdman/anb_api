import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
	create_custom_fields()

def create_custom_fields():
	print("In the Patch")
	custom_fields = {
		"Customer": [
			dict(
				fieldname="anb_bank_account",
				label="ANB Bank Account",
				fieldtype="Data",
				insert_after="credit_limit_section",
				ignore_user_permissions=1,
				unique=1,
				no_copy=1
			)
		],
		"Payment Entry": [
			dict(
				fieldname="payment_log",
				label="Payment Log",
				fieldtype="Link",
				options="Anb Payment Log",
				insert_after="reference_no",
				ignore_user_permissions=1,
				read_only = 1,
				unique=1,
				no_copy=1
			)
		]
	}
	create_custom_fields(custom_fields, ignore_validate=frappe.flags.in_patch, update=True)