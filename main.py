from company_discovery import find_similar_companies
from prospeo_client import find_decision_makers
from eazyreach_client import find_email
from email_generator import generate_email
from brevo_client import send_email


def main():
    print("=" * 50)
    print("AUTOMATED OUTREACH PIPELINE")
    print("=" * 50)

    domain = input("Enter company domain: ")

    print("\n[1] Finding similar companies...")
    companies = find_similar_companies(domain)

    for company in companies:
        print(f"  - {company}")

    print("\n[2] Finding decision makers...")

    all_contacts = []

    for company in companies:
        contacts = find_decision_makers(company)

        for contact in contacts:
            print(f"  - {contact['name']} ({contact['title']})")
            all_contacts.append(contact)

    print("\n[3] Finding emails...")

    for contact in all_contacts:
        contact["email"] = find_email(contact["linkedin"])
        print(f"  - {contact['email']}")

    print("\n[4] Generating outreach emails...")

    for contact in all_contacts:
        email_content = generate_email(
            contact["name"],
            contact["company"]
        )

        contact["email_content"] = email_content

        print("\n" + "-" * 50)
        print(f"To: {contact['email']}")
        print(email_content)

    print("\n[5] Safety Check")
    print(f"Companies Found : {len(companies)}")
    print(f"Contacts Found  : {len(all_contacts)}")

    choice = input("\nSend emails? (y/n): ")

    if choice.lower() == "y":

        print("\nSending emails...")

        # TEST MODE: sends only one email
        test_email = input(
            "\nEnter your email for testing: "
        )

        if all_contacts:

            status = send_email(
                test_email,
                "Partnership Opportunity",
                all_contacts[0]["email_content"]
            )

            print(
                f"\nEmail sent to {test_email}"
            )
            print(f"Status Code: {status}")

    else:
        print("\nEmail sending cancelled.")


if __name__ == "__main__":
    main()