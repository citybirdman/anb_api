import frappe
import json
@frappe.whitelist()
def discard(doctype: str, name: str):
    doc = frappe.get_doc(doctype, name)
    doc.status = "Discarded"
    doc.save("update")

@frappe.whitelist()
def discard_all(items: list, doctype: str):
    failed_ops = ""
    for doc in json.loads(items):
        if doc["status"] == "Discarded":
            frappe.msgprint(f"Cannot Discard <a href='app/anb-payment-log/{doc['name']}'>{doc['name']}</a>", title="Error", indicator="red")
        else:
            discard(doctype, doc["name"])