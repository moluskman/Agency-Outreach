from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base, validates

Base = declarative_base()


class Lead(Base):
    """Represents a sales lead with contact and website information."""

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    business_name = Column(String)
    website = Column(String, nullable=True)
    has_website = Column(Boolean)
    website_quality = Column(Float)
    contact_name = Column(String)
    email = Column(String, default="")
    phone = Column(String, default="")

    @validates("email", "phone")
    def validate_contact_info(self, key: str, value: object) -> str:
        """Normalize non-string or None values to an empty string."""
        if not isinstance(value, str):
            return ""
        return value

    def is_contactable(self) -> bool:
        """Return True when the lead has either an email or a phone number."""
        return bool((self.email or "").strip() or (self.phone or "").strip())

    def __repr__(self) -> str:
        return (
            f"Lead(business_name={self.business_name!r}, website={self.website!r}, "
            f"has_website={self.has_website}, website_quality={self.website_quality}, "
            f"contact_name={self.contact_name!r}, email={self.email!r}, phone={self.phone!r})"
        )
