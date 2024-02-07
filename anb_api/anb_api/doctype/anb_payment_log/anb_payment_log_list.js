frappe.listview_settings['Anb Payment Log'] = {
	add_fields: ['status'],
	get_indicator: function (doc) {
		if (doc.status === "Draft") {
			return [__("Draft"), "green", "status=Draft"];

		} else if (doc.status === "Failed") {
			return [__("Failed"), "red", "status=Failed"];

	    } else if (doc.status === "Pending") {
			return [__("Pending"), "gray", "status=Pending"];

	    } else if (doc.status === "Reported") {
			return [__("Reported"), "gray", "status=Reported"];

	    } else if (doc.status === "Reported") {
			return [__("Discarded"), "gray", "status=Discarded"];

	    }else if (doc.status === "Cleared") {
			return [__("Cleared"), "gray", "status=Cleared"];

	    } else if (doc.status === "Not Reported") {
			return [__("Not Reported"), "gray", "status=Not Reported"];

	    } else if (doc.status === "Discarded") {
			return [__("Discarded"), "gray", "status=Discarded"];

	    } else if (doc.status === "Discarded") {
			return [__("Discarded"), "gray", "status=Discarded"];

	    } else if (doc.status === "Discarded") {
			return [__("Discarded"), "gray", "status=Discarded"];

	    }
    }
}
