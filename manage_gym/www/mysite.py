import frappe
def get_context(context):
       context.u = frappe.get_list("Gym Trainer", fields=["first_name", "last_name"])
       context.plan = frappe.get_list("Gym Workout Plan", fields=["plan_name"])

    # context.mysite= frappe.get_doc("Gym Trainer")
    # return context

