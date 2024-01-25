// Copyright (c) 2024, Ahmed Zaytoon and contributors
// For license information, please see license.txt

frappe.ui.form.on('Anb Payment Log', {
	refresh: function(frm) {
		if(frm.doc.status !== "Discarded"){
			frm.add_custom_button(__('Discard'), function() {
				frappe.call({
					method: "anb_api.anb_api.doctype.anb_payment_log.discard", 
					args: {
						doctype: frm.doctype,
						name: frm.docname
					},
					callback: function(){
						window.location.reload();
					}
				})
			}).removeClass("btn-default").css({'background-color': '#4e5a66', 'border-color': '#4e5a66', 'color':'#fff'});
    	}
	}
});
