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
        ("   ", "   ", False),
        ("   ", "", False),
        ("", "   ", False),
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


@pytest.mark.parametrize(
    "input_email, input_phone, expected_email, expected_phone",
    [
        (None, None, "", ""),
        (float("nan"), float("nan"), "", ""),
        (123, 456, "", ""),
        ("jane@test.com", "123-456-7890", "jane@test.com", "123-456-7890"),
    ],
)
def test_lead_normalization(input_email, input_phone, expected_email, expected_phone):
    lead = Lead(
        business_name="Test Business",
        website="https://test.com",
        has_website=True,
        website_quality=7,
        contact_name="Jane Smith",
        email=input_email,
        phone=input_phone,
    )
    assert lead.email == expected_email
    assert lead.phone == expected_phone
