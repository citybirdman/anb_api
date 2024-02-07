frappe.listview_settings['Anb Log Queue'] = {
	add_fields: ['status'],
	get_indicator: function (doc) {
		if (doc.status === "Complete") {
			return [__("Complete"), "green", "status,=,Complete"];

		} else if (doc.status === "Partially Complete") {
			return [__("Partially Complete"), "yellow", "status,=,Partially Complete"];
			
	    } else if (doc.status === "Discarded") {
			return [__("Discarded"), "gray", "status,=,Discarded"];

	    } else if (doc.status === "Failed") {
			return [__("Failed"), "red", "status,=,Failed"];
	    }
    },
	onload: function(list) {
		list.page.add_inner_button(__('↓ Request Last Statments'), function() {
                frappe.call("anb_api.tasks.enqueue_bank_logs")
				.then(function(frm){
					list.refresh();
				});
				
            },"",'success' // Add your desired styles
        );
    }
}
