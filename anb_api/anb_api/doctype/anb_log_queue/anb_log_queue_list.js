frappe.listview_settings['Anb Log Queue'] = {
	add_fields: ['status'],
	get_indicator: function (doc) {
		if (doc.status === "Complete") {
			return [__("Complete"), "green", "status,=,Complete"];

		} else if (doc.status === "Partially Complete") {
			return [__("Partially Complete"), "yellow", "status,=,Partially Complete"];
			
	    } else if (doc.status === "Failed") {
			return [__("Failed"), "red", "status,=,Failed"];
	    }
    }
}
