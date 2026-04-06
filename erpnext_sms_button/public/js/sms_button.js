function show_sms_dialog(frm) {
    // Field priority order per doctype — extend as needed
    const phone = frm.doc.mobile_no
        || frm.doc.customer_phone_number
        || frm.doc.phone
        || frm.doc.contact_mobile
        || '';

    const default_msg = frm.doc.doctype === 'Sales Invoice'
        ? `Invoice ${frm.doc.name} — Due: $${frm.doc.grand_total} by ${frm.doc.due_date}`
        : `Message from ${frappe.boot.sysdefaults.company}`;

    let d = new frappe.ui.Dialog({
        title: __('Send SMS'),
        fields: [
            {
                fieldname: 'mobile_no',
                fieldtype: 'Data',
                label: __('Mobile Number'),
                default: phone,
                reqd: 1
            },
            {
                fieldname: 'message',
                fieldtype: 'Small Text',
                label: __('Message'),
                default: default_msg,
                reqd: 1
            }
        ],
        primary_action_label: __('Send'),
        primary_action(values) {
            frappe.call({
                method: 'frappe.core.doctype.sms_settings.sms_settings.send_sms',
                args: {
                    receiver_list: [values.mobile_no],
                    msg: values.message
                },
                callback(r) {
                    if (!r.exc) {
                        frappe.show_alert({ message: __('SMS Sent'), indicator: 'green' });
                        // Log to Communication timeline
                        frappe.call({
                            method: 'frappe.client.insert',
                            args: {
                                doc: {
                                    doctype: 'Communication',
                                    communication_type: 'Communication',
                                    communication_medium: 'SMS',
                                    reference_doctype: frm.doc.doctype,
                                    reference_name: frm.doc.name,
                                    content: values.message,
                                    sent_or_received: 'Sent',
                                    phone_no: values.mobile_no
                                }
                            }
                        });
                        d.hide();
                    }
                }
            });
        }
    });
    d.show();
}

// Attach to each doctype
['Sales Invoice', 'Sales Order', 'Lead', 'Contact', 'Customer'].forEach(dt => {
    frappe.ui.form.on(dt, {
        refresh(frm) {
            frm.page.add_menu_item(__('Send SMS'), () => show_sms_dialog(frm));
        }
    });
});
