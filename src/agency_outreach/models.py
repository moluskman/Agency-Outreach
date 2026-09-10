from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

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

    def __init__(self, **kwargs):
        if "email" in kwargs and not isinstance(kwargs["email"], str):
            kwargs["email"] = ""
        if "phone" in kwargs and not isinstance(kwargs["phone"], str):
            kwargs["phone"] = ""
        super().__init__(**kwargs)

    def is_contactable(self) -> bool:
        """Return True when the lead has either an email or a phone number."""
        has_email = bool(
            self.email and isinstance(self.email, str) and self.email.strip()
        )
        has_phone = bool(
            self.phone and isinstance(self.phone, str) and self.phone.strip()
        )
        return has_email or has_phone

    def __repr__(self) -> str:
        return (
            f"Lead(business_name={self.business_name!r}, website={self.website!r}, "
            f"has_website={self.has_website}, website_quality={self.website_quality}, "
            f"contact_name={self.contact_name!r}, email={self.email!r}, phone={self.phone!r})"
        )
