from unittest.mock import patch

from alternance_copilot.graph import graph
from alternance_copilot.state import OfferAnalysis


def test_graph_returns_offer_analysis():
    expected = OfferAnalysis(
        job_title="Developer",
        company=None,
        responsibilities=[],
        required_skills=["Python"],
        preferred_skills=[],
        keywords=[],
    )

    with patch(
        "alternance_copilot.agents.offer_analyzer.ChatOllama"
    ) as mock_model:
        mock_model.return_value.with_structured_output.return_value.invoke.return_value = expected

        result = graph.invoke({"offer_text": "Python developer"})

    assert result["offer_text"] == "Python developer"
    assert result["offer"] == expected