import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
	create_parking_account_field()

def create_parking_account_field():
	print("In the Patch")
	custom_field = {
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
		]
	}
	create_custom_fields(custom_field, ignore_validate=frappe.flags.in_patch, update=True)