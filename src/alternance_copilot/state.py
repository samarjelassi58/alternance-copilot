from typing import TypedDict

from pydantic import BaseModel


class OfferAnalysis(BaseModel):
    job_title: str | None
    company: str | None
    responsibilities: list[str]
    required_skills: list[str]
    preferred_skills: list[str]
    keywords: list[str]


class State(TypedDict, total=False):
    offer_text: str
    offer: OfferAnalysis