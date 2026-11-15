import io
import logging
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, Response, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.schemas import BriefRequest, BriefResponse
from src.tavily_agent import TavilyResearchAgent
from src.synthesizer import BriefSynthesizer
from src.pdf_generator import BriefPDFGenerator
from src.sample_data import SAMPLE_BRIEF

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("briefpilot")

app = FastAPI(
    title="BriefPilot API",
    description="Autonomous Pre-Meeting Executive Intelligence Agent powered by Tavily Search & Google Gemini",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    index_file = BASE_DIR / "templates" / "index.html"
    return HTMLResponse(content=index_file.read_text(encoding="utf-8"))

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "app": "BriefPilot",
        "tavily_configured": bool(settings.TAVILY_API_KEY),
        "gemini_configured": bool(settings.GEMINI_API_KEY),
        "gemini_model": settings.GEMINI_MODEL
    }

@app.get("/api/sample", response_model=BriefResponse)
async def get_sample():
    return SAMPLE_BRIEF

@app.post("/api/brief", response_model=BriefResponse)
async def generate_brief(req: BriefRequest):
    if not settings.TAVILY_API_KEY:
        raise HTTPException(status_code=500, detail="TAVILY_API_KEY is not configured on the server.")
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured on the server.")

    try:
        logger.info(f"Initiating research for target='{req.target_name}' type='{req.target_type}'")
        agent = TavilyResearchAgent()
        research_data = agent.conduct_research(req)
        
        logger.info(f"Retrieved {len(research_data.get('citations', []))} citations from Tavily. Synthesizing...")
        synthesizer = BriefSynthesizer()
        brief = synthesizer.synthesize(req, research_data)
        
        return brief
    except Exception as e:
        logger.error(f"Error generating brief: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/brief/pdf")
async def generate_pdf(brief: BriefResponse):
    try:
        generator = BriefPDFGenerator()
        buffer = io.BytesIO()
        generator.generate(brief, buffer)
        buffer.seek(0)
        
        filename = f"BriefPilot_{brief.target_name.replace(' ', '_')}.pdf"
        return Response(
            content=buffer.getvalue(),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=\"{filename}\""}
        )
    except Exception as e:
        logger.error(f"Error rendering PDF: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host=settings.HOST, port=settings.PORT, reload=True)
