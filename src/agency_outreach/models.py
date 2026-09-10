from dataclasses import dataclass


@dataclass
class Lead:
    """Represents a sales lead with contact and website information."""

    business_name: str
    website: str | None
    has_website: bool
    website_quality: float
    contact_name: str
    email: str = ""
    phone: str = ""

    def __post_init__(self) -> None:
        # Normalize non-string/None input (e.g. NaN from pandas) to ""
        if not isinstance(self.email, str):
            self.email = ""
        if not isinstance(self.phone, str):
            self.phone = ""

    def is_contactable(self) -> bool:
        """Return True when the lead has either an email or a phone number."""
        return bool(self.email.strip() or self.phone.strip())


@dataclass
class CategoryScore:
    name: str
    score: float
    max_score: float
    findings: list[str]  # e.g. ["No clear booking CTA"]


@dataclass
class WebsiteAnalysis:
    categories: list[CategoryScore]
    strengths: list[str]
    weaknesses: list[str]

    @property
    def overall_score(self) -> float:
        return sum(c.score for c in self.categories)
