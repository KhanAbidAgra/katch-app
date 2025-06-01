from frappe import _
import frappe
from erpnext.accounts.party import get_party_details, set_address_details

@frappe.whitelist()
def custom_get_party_details_api(party_type, party, doctype, company):
    print("Testing")
    party_details = get_party_details(
        party=party,
        party_type=party_type,
        company=company,
        doctype=doctype,
    )

    return party_details
    # set_address_details
