# Automated Outreach Pipeline

## Overview

This project automates the B2B outreach process by discovering decision-makers from a target company, generating personalized outreach emails, and sending emails automatically.

The system integrates Prospeo, EazyReach, and Brevo APIs to create an end-to-end outreach workflow.

---

# Workflow

## Step 1: Input Company Domain

The user enters a target company domain.

Example:

```
openai.com
google.com
microsoft.com
salesforce.com
```

---

## Step 2: Decision Maker Discovery (Prospeo API)

The system uses the Prospeo Search Person API to find professionals associated with the target company.

Example:

```
google.com
↓
Google Employees
↓
Decision Makers
```

Information collected:

* Full Name
* Job Title
* LinkedIn URL
* Company

Example output:

```
Yixuan Su
Jenna Cook
Dennis Chun
Shauna Nehra
```

---

## Step 3: Email Enrichment (EazyReach API)

The system integrates with EazyReach API to enrich contacts using LinkedIn profile URLs.

Workflow:

```
LinkedIn URL
↓
EazyReach Authentication
↓
Email Lookup
↓
Verified Email Address
```

Authentication is implemented using:

* Client ID
* Client Secret

Current status:

* Authentication API is working successfully.
* Email lookup endpoint is integrated.
* Email enrichment requires available EazyReach credits.

---

## Step 4: Email Generation

The system automatically generates personalized outreach emails.

Example:

```
Subject: Partnership Opportunity

Hi Yixuan Su,

I came across your company and was impressed by your work.

We help companies automate outreach and lead generation workflows.

Would love to connect and explore opportunities.

Best Regards,
Ganesh
```

---

## Step 5: Safety Check

Before sending emails, the system displays:

* Total contacts found
* Email previews
* Generated outreach content

This allows the user to verify all outreach content before sending.

---

## Step 6: Email Delivery (Brevo API)

The system uses Brevo SMTP API for email delivery.

Workflow:

```
Generated Email
↓
Brevo API
↓
Verified Domain
↓
Recipient Inbox
```

Features:

* Verified sender domain
* API-based delivery
* Delivery confirmation
* Real email sending

Testing confirmed successful email delivery using Brevo.

---

# System Architecture

```
Company Domain
      │
      ▼
Prospeo API
      │
      ▼
Decision Makers
      │
      ▼
LinkedIn URLs
      │
      ▼
EazyReach API
      │
      ▼
Email Discovery
      │
      ▼
Email Generator
      │
      ▼
Safety Check
      │
      ▼
Brevo API
      │
      ▼
Email Delivery
```

---

# Technologies Used

## Programming Language

* Python 3

## APIs

* Prospeo API
* EazyReach API
* Brevo API

## Development Tools

* Git
* GitHub
* VS Code

---

# Project Structure

```
automated-outreach-clean/
│
├── main.py
├── company_discovery.py
├── prospeo_client.py
├── eazyreach_client.py
├── email_generator.py
├── brevo_client.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Environment Variables

Create a `.env` file:

```env
PROSPEO_API_KEY=your_prospeo_api_key

BREVO_API_KEY=your_brevo_api_key

EAZYREACH_CLIENT_ID=your_client_id

EAZYREACH_CLIENT_SECRET=your_client_secret
```

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

Example:

```bash
Enter company domain: google.com
```

---

# Current Status

| Module                   | Status             |
| ------------------------ | ------------------ |
| Prospeo Integration      | ✅ Working          |
| Decision Maker Discovery | ✅ Working          |
| EazyReach Authentication | ✅ Working          |
| EazyReach Email Lookup   | ⚠ Requires Credits |
| Email Generation         | ✅ Working          |
| Brevo Integration        | ✅ Working          |
| Real Email Sending       | ✅ Working          |
| GitHub Repository        | ✅ Working          |

---

# Author

Ganesh

Automated Outreach Pipeline
