// Copyright (c) 2024, Ahmed Zaytoon and contributors
// For license information, please see license.txt

frappe.ui.form.on('Anb Log Queue', {
	setup: function(frm) {
		frm.ignore_doctypes_on_cancel_all = ['Anb Payment Log'];
		frappe.flags.ignore_links = true
	},
	refresh: function(frm) {
        frm.add_custom_button(__('Create succeeded Payments'), function() {
            // Add your custom action code here
            frappe.msgprint('functionality will be added soon!');
        }).removeClass("btn-default").css({'background-color': '#4e5a66', 'border-color': '#4e5a66', 'color':'#fff'});;
    }
});
