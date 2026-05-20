# Privacy notice (family / household use)

**Controller:** Mihail Barbascumpa (`devbmv`) — personal / family projects only.

## Scope

This software is **not** offered as a commercial service. It is intended for **private household** use on your own network and devices.

## Data processed

Depending on the project, the app may process:

- Account login (username, session cookies)
- Device names, room names, sensor readings
- Optional contact details if you configure email/WhatsApp integrations locally

We do **not** sell data. Do not expose admin panels to the public internet without HTTPS, strong passwords, and firewall rules.

## Legal basis (GDPR)

For purely personal/household activity, GDPR Article 2(2)(c) may apply. Where family members have individual logins, apply proportionate privacy practices: minimal collection, access control, and clear notices in the web UI where provided.

## Cookies

Session and security cookies only unless you enable optional analytics/fonts in your deployment. See in-app Cookie Policy where implemented.

## Your responsibilities

1. Keep secrets in local `.env` — never commit `.env`.
2. Rotate WiFi, MQTT, API, and database passwords if they ever appeared in old git history.
3. Back up your own databases; the author provides no hosted SLA.

## Contact

Open a GitHub Issue on the **specific repository** for code questions only — not for access to private deployments.
