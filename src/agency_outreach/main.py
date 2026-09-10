from agency_outreach.models import Lead


def main():
    lead = Lead(
        business_name="Example Business",
        website="https://example.com",
        has_website=True,
        website_quality=8,
        contact_name="John Doe",
        phone="123-456-7890",
    )
    print(f"lead.email value: {lead.email!r}")
    print(f"lead.is_contactable(): {lead.is_contactable()}")
    print(lead)


if __name__ == "__main__":
    main()
