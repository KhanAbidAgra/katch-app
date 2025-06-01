import frappe
from frappe import _
from erpnext.accounts.party import get_party_account

@frappe.whitelist()
def custom_get_party_details_api(party_type, party, doctype, company):
    # Build party details safely
    party_details = frappe._dict()

    party_details.account = get_party_account(party_type, party, company)
    
    # Fetch currency
    party_doc = frappe.get_doc(party_type, party)
    party_details.currency = party_doc.default_currency or frappe.get_cached_value("Company", company, "default_currency")

    # Optional: fetch and set address manually (excluding gstin)
    billing_address = frappe.db.get_value(
        "Dynamic Link",
        {
            "link_doctype": party_type,
            "link_name": party,
            "parenttype": "Address"
        },
        "parent"
    )

    if billing_address:
        address_doc = frappe.get_doc("Address", billing_address)
        party_details.address_display = address_doc.get("address_line1") or ""
        party_details.city = address_doc.get("city")

    return party_details


@frappe.whitelist()
def custom_get_company_address(company):
    address = frappe.db.get_all(
        "Address",
        filters={
            "link_doctype": "Company",
            "link_name": company,
            "is_primary_address": 1
        },
        fields=["name", "address_line1", "address_line2", "city", "state", "pincode", "country", "gstin"]
    )

    if address:
        return address[0]
    else:
        return {}

