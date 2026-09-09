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


def test_is_contactable_with_email_and_phone():
    lead = Lead("Biz", "site.com", True, 5, "Jane", "jane@test.com", "12345")
    assert lead.is_contactable() is True


def test_is_contactable_with_email_only():
    lead = Lead("Biz", "site.com", True, 5, "Jane", "jane@test.com", "")
    assert lead.is_contactable() is True


def test_is_contactable_with_phone_only():
    lead = Lead("Biz", "site.com", True, 5, "Jane", "", "12345")
    assert lead.is_contactable() is True


def test_is_contactable_without_contact_info():
    lead = Lead("Biz", "site.com", True, 5, "Jane", "", "")
    assert lead.is_contactable() is False
