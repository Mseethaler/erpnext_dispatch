# ERPNext SMS Button

Adds a **Send SMS** menu item to CRM and selling doctypes in ERPNext, using the native Frappe SMS gateway configuration.

## What it does

- Adds "Send SMS" to the three-dot menu on: Lead, Contact, Customer, Sales Order, Sales Invoice
- Pre-fills the phone number from the appropriate field on each doctype
- Sends via whatever gateway is configured in **SMS Settings** (Selling > SMS Settings)
- Logs sent messages to the document's Communication timeline

## Requirements

- ERPNext v15
- SMS gateway configured in Frappe SMS Settings (supports any HTTP gateway — tested with n8n webhook)

## Installation

Add to `apps.json` at Docker build time:
```json
{
    "url": "https://github.com/Mseethaler/erpnext_sms_button",
    "branch": "master"
}
```

Then install on your site:
```bash
bench --site [your-site] install-app erpnext_sms_button
```

## SMS Gateway Setup

Go to **Selling > SMS Settings** and configure your gateway URL, message parameter, and receiver parameter. This app uses whatever is configured there — no additional settings required.
