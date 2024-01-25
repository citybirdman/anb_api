// Copyright (c) 2024, Ahmed Zaytoon and contributors
// For license information, please see license.txt

frappe.ui.form.on('Anb Log Queue', {
	setup: function(frm) {
		frm.ignore_doctypes_on_cancel_all = ['Anb Payment Log'];
		frappe.flags.ignore_links = true
	}
});
