# ERPNext Dispatch

A Frappe/ERPNext app that installs a complete field service dispatch workflow, 
including custom fields, workspaces, and calendar views.

## What it installs

**Custom Fields**
- Opportunity: `Scheduled Start` and `Scheduled End` (Datetime) for dispatch scheduling
- Quotation, Sales Order, Sales Invoice: `Customer Signature` (Signature) for on-site sign-off

**Workspaces**
- `Dispatched Tecs` — Tech-facing workspace: ToDos, Opportunities, Quotations, Sales Orders, Projects, Invoices, Payments
- `Dispatch Officer` — Dispatcher-facing workspace: Leads, Opportunities, calendar, full job lifecycle
- `Quick Routes` — Route-based delivery workflow shortcuts

**Calendar View**
- `Opportunities` — Calendar view of scheduled jobs using Scheduled Start/End fields

**Setup ToDo Checklist**
On install, creates a ToDo list guiding the admin through:
- ERPNext SMS Settings configuration
- N8n workflow imports (dispatch SMS, en-route notification, Twilio call routing)
- Twilio credential wiring
- Tech photo setup on Employee records

## Dispatch Flow

**Office-dispatched jobs:**
`Opportunity → assign to tech → tech notified via SMS → tech visits → Quotation → customer signs → Sales Order → Invoice → Payment`

**Route-based jobs:**
`Sales Order → Delivery Note → Delivery List → tech checks in/out`

## Requirements

- ERPNext v15
- SMS gateway configured in Frappe SMS Settings
- N8n instance with Twilio for SMS notifications and call routing

## Installation

Add to `apps.json` at Docker build time:
```json
{
    "url": "https://github.com/Mseethaler/erpnext_dispatch",
    "branch": "main"
}
```

Then install on your site:
```bash
bench --site [your-site] install-app erpnext_dispatch
```

## N8n Workflows Required

Copy from master N8n instance and wire credentials:
- `dispatch_sms` — Notifies tech via SMS when assigned a job
- `enroute_notification` — Sends customer SMS with tech photo when en route
- `call_routing` — Routes inbound Twilio calls to on-duty dispatcher
