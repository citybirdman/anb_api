// Copyright (c) 2023, Ahmed Zaytoon and contributors
// For license information, please see license.txt

frappe.ui.form.on('ANB Settings', {
	before_save: function(frm){
		frm.doc.url = frm.doc.url.replace("https://", "").replace("http://", "")
		if(frm.doc.url[cur_frm.doc.url.length - 1] == "/")
			frm.doc.url = frm.doc.url.slice(0, -1)
		frm.refresh_field("url")
	}
});
