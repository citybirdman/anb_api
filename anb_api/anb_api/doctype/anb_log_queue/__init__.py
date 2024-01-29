import frappe, json
@frappe.whitelist()
def create_payments(logs: list, status: str):
    if status != "Failed":
        logs = json.loads(logs)
        for log in logs:
            if not frappe.db.get_value("Payment Entry", [["payment_log", "=", log["payment_log"]]], ["name"]):
                doc = frappe.db.get_value("Anb Payment Log", log["payment_log"], ["customer_name", "mode_of_payment", "currency", "amount", "transaction_number", "date", "status", "company"], as_dict=True)
                if doc.status == "Success":
                    payment = frappe.get_doc(dict(
                        doctype = "Payment Entry",
                        mode_of_payment = doc.mode_of_payment,
                        payment_type = "Receive",
                        party_type = "Customer",
                        party = doc.customer_name,
                        paid_amount = doc.amount,
                        source_exchange_rate = 1,
                        target_exchange_rate = 1,
                        received_amount = doc.amount,
                        reference_no = doc.transaction_number,
                        reference_date = doc.date,
                        paid_to = frappe.db.get_value("Mode of Payment Account", [["parent", "=", doc.mode_of_payment], ["company", "=", doc.company]], "default_account"),
                        paid_to_account_currency = doc.currency,
                        payment_log = log["payment_log"]
                    )).insert()
                    payment.submit()
        frappe.msgprint("Payments created successfully!")
    else:
        frappe.throw("There is no succeeded log in this queue!")