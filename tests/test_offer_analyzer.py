from unittest.mock import patch
from alternance_copilot.state import OfferAnalysis
import pytest

from alternance_copilot.agents.offer_analyzer import analyze_offer


def test_missing_offer_is_rejected():
    with pytest.raises(ValueError, match="missing"):
        analyze_offer({})


def test_empty_offer_is_rejected():
    with pytest.raises(ValueError, match="empty"):
        analyze_offer({"offer_text": "   "})

def test_analyzer_returns_the_model_analysis():
    expected = OfferAnalysis(
        job_title="Python developer",
        company=None,
        responsibilities=["Build APIs"],
        required_skills=["Python"],
        preferred_skills=["Docker"],
        keywords=["Python", "API", "Docker"],
    )

    with patch(
        "alternance_copilot.agents.offer_analyzer.ChatOllama"
    ) as mock_model:
        mock_model.return_value.with_structured_output.return_value.invoke.return_value = expected

        result = analyze_offer({"offer_text": "A fictional job offer"})

    assert result["offer"] == expected