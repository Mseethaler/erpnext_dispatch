import frappe

def after_install():
    create_setup_tasks()

def create_setup_tasks():
    tasks = [
        "Configure SMS Settings in ERPNext",
        "Add Twilio credentials to site_config.json",
        "Import N8n workflow: dispatch_sms",
        "Import N8n workflow: enroute_notification", 
        "Import N8n workflow: call_routing",
        "Configure N8n Twilio credentials",
        "Activate N8n workflows",
        "Set tech photos on Employee records",
        "Configure dispatcher call routing logic",
        "Test end-to-end dispatch flow",
    ]
    
    for task in tasks:
        frappe.get_doc({
            "doctype": "ToDo",
            "description": task,
            "status": "Open",
            "owner": frappe.session.user
        }).insert(ignore_permissions=True)
