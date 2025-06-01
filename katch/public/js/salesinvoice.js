frappe.ui.form.on('Sales Invoice', {
    refresh: function (frm) {
        frappe.msgprint("Custom party details loaded");
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

                        // Optional address field updates
                        if (r.message.address_display) {
                            frm.set_value("customer_address", r.message.address_display);
                        }
                    }
                }
            });
        }
    }
});
