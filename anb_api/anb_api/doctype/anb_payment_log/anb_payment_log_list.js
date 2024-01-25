frappe.listview_settings['Anb Payment Log'] = {
	add_fields: ['status'],
	get_indicator: function (doc) {
		if (doc.status === "Success") {
			return [__("Success"), "green", "status=Success"];

		} else if (doc.status === "Failed") {
			return [__("Failed"), "red", "status=Failed"];

	    } else if (doc.status === "Discarded") {
			return [__("Discarded"), "gray", "status=Discarded"];
	    }
    },
	onload: function(list) {
		// list.page.add_inner_button(__('Discard'), function() {
				
        //     },"",'success' // Add your desired styles
        // );
		list.page.add_action_item(__('Discard Payments'), function() {
            var selected_docs = list.get_checked_items();
			frappe.confirm(
				__('Are you sure you want to perform this action?'),
				function() {
					frappe.call({
						method: "anb_api.anb_api.doctype.anb_payment_log.discard_all", 
						args: {
							items: selected_docs,
							doctype: list.doctype
						}
					});
				}
			);
		});
    }
}
