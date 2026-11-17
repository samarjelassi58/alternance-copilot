import pytest
from pydantic import ValidationError

from alternance_copilot.state import OfferAnalysis


def test_required_skills_must_be_a_list():
    with pytest.raises(ValidationError):
        OfferAnalysis.model_validate({
            "job_title": "Developer",
            "company": None,
            "responsibilities": [],
            "required_skills": "Python",
            "preferred_skills": [],
            "keywords": [],
        })