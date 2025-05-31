from frappe import _
import frappe
from frappe.utils import msgprint
from erpnext.accounts.party import get_party_details, set_address_details

@frappe.whitelist()
def custom_get_party_details_api(party_type, party, doctype, company):
    party_details = get_party_details(
        party=party,
        party_type=party_type,
        company=company,
        doctype=doctype,
    )

    party_details = set_address_details(
        party_details,
        party_type,
        party,
        doctype,
        company
    )
    return party_details
