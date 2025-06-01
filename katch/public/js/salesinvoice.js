frappe.ui.form.on('Sales Invoice', {
    refresh: function (frm) {
        if (frm.doc.customer && frm.doc.company) {
            frappe.call({
                method: "katch.katch.api.custom_get_party_details_api",
                args: {
                    party_type: "Customer",
                    party: frm.doc.customer,
                    doctype: frm.doc.doctype,
                    company: frm.doc.company
                },
                callback: function (r) {
                    if (r.message) {
                        if (r.message.account) {
                            frm.set_value("debit_to", r.message.account);
                        }

                        if (r.message.currency) {
                            frm.set_value("currency", r.message.currency);
                        }

                        if (r.message.address_display) {
                            frm.set_value("customer_address", r.message.address_display);
                        }
                    }
                }
            });
        }
    }
});

frappe.ui.form.on('Sales Invoice', {
    refresh(frm) {
        if (frm.doc.company) {
            frappe.call({
                method: "katch.katch.api.custom_get_company_address",
                args: {
                    company: frm.doc.company
                },
                callback: function(r) {
                    if (r.message) {
                        console.log(r.message);
                        frm.set_value("company_address", r.message.company_address);
                        // You can create a custom read-only field for address display if needed
                        // frm.set_value("company_address_display", r.message.address_display);
                        frm.refresh_field("company_address");
                    }
                }
            });
        }
    }
});

