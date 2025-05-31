
# your_app/api.py

@frappe.whitelist()
def custom_set_company_address(docname):
    # Your own logic to fetch address for KSA
    # Don't include gstin
    doc = frappe.get_doc("Sales Invoice", docname)
    if not doc.company_address:
        address = frappe.get_all("Address", filters={"company": doc.company}, fields=["name"])
        if address:
            doc.company_address = address[0].name
            doc.save()
