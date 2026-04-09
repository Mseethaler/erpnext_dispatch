app_name = "erpnext_dispatch"
app_title = "ERPNext Dispatch"
app_publisher = "Digital Sovereignty"
app_description = "Field service dispatch workflow for ERPNext"
app_version = "0.0.1"
app_email = "info@digital-sovereignty.cc"
app_license = "MIT"

after_install = "erpnext_dispatch.setup.install.after_install"

# Fixtures to export/import with the app
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "in", ["Opportunity", "Sales Order", "Sales Invoice", "Quotation"]],
            ["fieldname", "in", [
                "custom_scheduled_start",
                "custom_scheduled_end",
                "custom_customer_signature"
            ]],
        ]
    },
    {
        "dt": "Workspace",
        "filters": [["name", "in", ["Dispatched Tecs", "Dispatch Officer", "Quick Routes"]]]
    },
    {
        "dt": "Calendar View",
        "filters": [["name", "=", "Opportunities"]]
    },
    {
        "dt": "Notification",
        "filters": [["name", "like", "Dispatch%"]]
    },
]

# JS includes per doctype
doctype_js = {
    "Opportunity": "public/js/dispatch.js",
    "Sales Order": "public/js/dispatch.js",
}
