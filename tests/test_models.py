from agency_outreach.models import Lead


def test__repr__():
    lead = Lead(
        business_name="Test Business",
        website="https://test.com",
        has_website=True,
        website_quality=7,
        contact_name="Jane Smith",
        email="",
        phone="987-654-3210",
    )
    assert repr(lead) == (
        "Lead(business_name='Test Business', website='https://test.com', "
        "has_website=True, website_quality=7, contact_name='Jane Smith', email='', phone='987-654-3210')"
    )
