import pytest
from agency_outreach.models import Lead


@pytest.mark.parametrize(
    "email, phone, expected",
    [
        ("jane@test.com", "123-456-7890", True),
        ("jane@test.com", "", True),
        ("", "123-456-7890", True),
        ("", "", False),
        (None, None, False),
        (None, "123-456-7890", True),
        ("jane@test.com", None, True),
    ],
)
def test_is_contactable_edge_cases(email, phone, expected):
    lead = Lead(
        business_name="Test Business",
        website="https://test.com",
        has_website=True,
        website_quality=7,
        contact_name="Jane Smith",
        email=email,
        phone=phone,
    )
    assert lead.is_contactable() == expected
