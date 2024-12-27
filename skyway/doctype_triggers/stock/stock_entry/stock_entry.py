from __future__ import unicode_literals
import frappe
from frappe import _


@frappe.whitelist()
def before_insert(doc, method=None):
    pass
@frappe.whitelist()
def after_insert(doc, method=None):
    pass
@frappe.whitelist()
def onload(doc, method=None):
    pass
@frappe.whitelist()
def before_validate(doc, method=None):
    pass
@frappe.whitelist()
def validate(doc, method=None):
    if doc.ticket:
        frappe.db.set_value('Ticket Items', doc.ticket_item, "stock_entry", doc.name)
        if doc.docstatus == 0:
            frappe.db.set_value('Ticket Items', doc.ticket_item, "stock_entry_status", "Draft")
        if doc.docstatus == 1:
            frappe.db.set_value('Ticket Items', doc.ticket_item, "stock_entry_status", "Submitted")
@frappe.whitelist()
def on_submit(doc, method=None):
    pass
@frappe.whitelist()
def on_cancel(doc, method=None):
    if doc.ticket:
        frappe.db.set_value('Ticket Items', doc.ticket_item, "stock_entry", "")
        frappe.db.set_value('Ticket Items', doc.ticket_item, "stock_entry_status", "")
@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update(doc, method=None):
    pass
