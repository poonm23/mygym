// Copyright (c) 2024, vinod and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer Subscription", {
	refresh(frm) {

        frm.add_custom_button("Accept", () =>{
            frappe.show_alert('its working')
        })

	},
});
