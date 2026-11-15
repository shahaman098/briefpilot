import io
import pytest
from fastapi.testclient import TestClient
from src.schemas import BriefRequest, BriefResponse, TimelineItem, StrategicOpportunity, TalkingPoint, RedFlag, SourceCitation
from src.sample_data import SAMPLE_BRIEF
from src.pdf_generator import BriefPDFGenerator
from src.tavily_agent import TavilyResearchAgent
from src.main import app
from src.cli import brief_to_markdown

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["app"] == "BriefPilot"
    assert data["tavily_configured"] is True
    assert data["gemini_configured"] is True

def test_root_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "BriefPilot" in response.text
    assert "Tavily" in response.text

def test_sample_api():
    response = client.get("/api/sample")
    assert response.status_code == 200
    data = response.json()
    assert data["target_name"] == "Tavily AI"
    assert len(data["timeline_30d"]) > 0
    assert len(data["talking_points"]) > 0

def test_pdf_generation():
    generator = BriefPDFGenerator()
    buffer = io.BytesIO()
    generator.generate(SAMPLE_BRIEF, buffer)
    buffer.seek(0)
    pdf_bytes = buffer.getvalue()
    assert len(pdf_bytes) > 1000
    assert pdf_bytes.startswith(b"%PDF")

def test_pdf_api_endpoint():
    response = client.post("/api/brief/pdf", json=SAMPLE_BRIEF.model_dump())
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert len(response.content) > 1000
    assert response.content.startswith(b"%PDF")

def test_query_decomposition():
    req_company = BriefRequest(
        target_name="Maxim AI",
        target_type="company",
        meeting_objective="Bifrost enterprise integration"
    )
    agent = TavilyResearchAgent(api_key="tvly-mock-key")
    queries = agent.generate_search_queries(req_company)
    assert len(queries) >= 3
    assert any("Maxim AI" in q["query"] for q in queries)
    assert any(q.get("time_range") == "month" for q in queries)

def test_markdown_export():
    md = brief_to_markdown(SAMPLE_BRIEF)
    assert "# Executive Briefing: Tavily AI" in md
    assert "30-Day Fresh Intelligence Timeline" in md
    assert "High-Impact Talking Points" in md
    assert "Grounded Tavily Sources" in md
