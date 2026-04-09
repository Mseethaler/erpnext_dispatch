app_name = "erpnext_dispatch"
app_title = "ERPNext Dispatch"
app_publisher = "Digital Soveriengty"
app_description = "Field service dispatch workflow for ERPNext"
app_version = "0.0.1"
app_email = "info@digital-sovereignty.cc"
app_license = "MIT"

# Fixtures to export/import with the app
fixtures = [
    # Custom fields on core doctypes
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "in", ["Opportunity", "Sales Order", "Sales Invoice", "Quotation"]],
            ["module", "=", "ERPNext Dispatch"]
        ]
    },
    # Workspace
    {
        "dt": "Workspace",
        "filters": [["name", "=", "Dispatch Tecs"]]
    },
    # Calendar View
    {
        "dt": "Calendar View",
        "filters": [["name", "=", "Opportunities"]]
    },
    # Notification configs
    {
        "dt": "Notification",
        "filters": [["module", "=", "ERPNext Dispatch"]]
    },
]

# JS includes per doctype
doctype_js = {
    "Opportunity"   : "public/js/dispatch.js",
    "Sales Order"   : "public/js/dispatch.js",
}

# Webhooks or doc events can go here later
# doc_events = {}
