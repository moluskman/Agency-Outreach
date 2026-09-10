class Lead:

    def __init__(
        self,
        business_name: str,
        website: str | None,
        has_website: bool,
        website_quality: float,
        contact_name: str,
        email: str,
        phone: str,
    ) -> None:
        self.business_name = business_name
        self.website = website
        self.has_website = has_website
        self.website_quality = website_quality
        self.contact_name = contact_name
        self.email = email
        self.phone = phone

    def is_contactable(self) -> bool:
        has_email = bool(self.email and self.email.strip())
        has_phone = bool(self.phone and self.phone.strip())
        return has_email or has_phone

    def __repr__(self) -> str:
        return (
            f"Lead(business_name={self.business_name!r}, website={self.website!r}, "
            f"has_website={self.has_website}, website_quality={self.website_quality}, "
            f"contact_name={self.contact_name!r}, email={self.email!r}, phone={self.phone!r})"
        )
