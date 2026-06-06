# Automated Outreach Pipeline

## Project Overview

This project automates the B2B outreach process by discovering potential target companies, finding decision-makers, generating personalized outreach emails, and sending emails automatically.

The system integrates multiple APIs to create an end-to-end outreach workflow.

---

# Workflow

## Step 1: Input Company Domain

The user enters a target company domain.

Example:

```
openai.com
```

---

## Step 2: Company Discovery

The system identifies similar companies related to the target company.

Example:

```
openai.com
↓
anthropic.com
cohere.com
perplexity.ai
```

This module acts as an alternative to Ocean.io company discovery.

---

## Step 3: Decision Maker Discovery (Prospeo API)

The system uses the Prospeo Search Person API to find decision-makers from the discovered companies.

Example:

```
anthropic.com
↓
Yixuan Su
Jenna Cook
Dennis Chun
...
```

Information collected:

- Full Name
- Job Title
- LinkedIn URL
- Company

---

## Step 4: Email Enrichment (EazyReach API)

The system integrates with EazyReach API.

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

Authentication was successfully implemented using:

- Client ID
- Client Secret

Note:

The current EazyReach account has zero lookup credits, therefore email enrichment cannot be completed until credits are added.

---

## Step 5: Email Generation

The system automatically generates personalized outreach emails.

Example:

```
Subject: Partnership Opportunity

Hi Yixuan Su,

I came across anthropic.com and was impressed by your work.

We help companies automate outreach and lead generation workflows.

Would love to connect and explore opportunities.

Best Regards,
Ganesh
```

---

## Step 6: Safety Check

Before sending emails, the system displays:

- Number of companies discovered
- Number of contacts found
- Generated email previews

This allows the user to verify outreach content before sending.

---

## Step 7: Email Delivery (Brevo API)

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

- Verified sender domain
- API-based email delivery
- Delivery status tracking

Testing confirmed successful email delivery.

---

# System Architecture

```
Target Company Domain
            │
            ▼
   Company Discovery
            │
            ▼
     Similar Companies
            │
            ▼
      Prospeo API
            │
            ▼
    Decision Makers
            │
            ▼
     EazyReach API
            │
            ▼
      Email Lookup
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

- Python 3

## APIs

- Prospeo API
- EazyReach API
- Brevo API

## Development Tools

- Git
- GitHub
- VS Code

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
PROSPEO_API_KEY=your_prospeo_key

BREVO_API_KEY=your_brevo_key

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
Enter company domain: openai.com
```

---

# Current Status

| Module | Status |
|----------|----------|
| Company Discovery | ✅ Working |
| Prospeo Integration | ✅ Working |
| Decision Maker Discovery | ✅ Working |
| EazyReach Authentication | ✅ Working |
| EazyReach Email Lookup | ⚠ Requires Credits |
| Email Generation | ✅ Working |
| Brevo Integration | ✅ Working |
| Email Sending | ✅ Working |
| GitHub Repository | ✅ Working |

---

# Author

Ganesh

Automated Outreach Pipeline Project