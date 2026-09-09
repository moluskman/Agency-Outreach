class Lead:

    def __init__(
        self,
        business_name,
        website,
        has_website,
        website_quality,
        contact_name,
        email,
        phone,
    ):
        self.business_name = business_name
        self.website = website
        self.has_website = has_website
        self.website_quality = website_quality
        self.contact_name = contact_name
        self.email = email
        self.phone = phone

    def is_contactable(self):
        return bool(self.email or self.phone)

    def __repr__(self):
        return (
            f"Lead(business_name={self.business_name!r}, website={self.website!r}, "
            f"has_website={self.has_website}, website_quality={self.website_quality}, "
            f"contact_name={self.contact_name!r}, email={self.email!r}, phone={self.phone!r})"
        )
