from agency_outreach.models import Lead


def main():
    lead = Lead(
        business_name="Example Business",
        website="https://example.com",
        has_website=True,
        website_quality=8,
        contact_name="John Doe",
        email="john.doe@example.com",
        phone="123-456-7890",
    )
    print(f"Lead created: {lead.business_name}")


if __name__ == "__main__":
    main()
