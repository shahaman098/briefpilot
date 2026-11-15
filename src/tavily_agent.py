import logging
from typing import List, Dict, Any
from tavily import TavilyClient
from src.config import settings
from src.schemas import SourceCitation, BriefRequest

logger = logging.getLogger(__name__)

class TavilyResearchAgent:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.TAVILY_API_KEY
        if not self.api_key:
            raise ValueError("Tavily API key is missing. Set TAVILY_API_KEY in .env.")
        self.client = TavilyClient(api_key=self.api_key)

    def generate_search_queries(self, req: BriefRequest) -> List[Dict[str, Any]]:
        target = req.target_name.strip()
        t_type = req.target_type.lower()
        obj = req.meeting_objective.strip()

        queries = []

        if t_type == "person":
            queries.append({
                "query": f"{target} recent announcements news talks interviews",
                "topic": "news",
                "time_range": "month",
                "search_depth": "advanced"
            })
            queries.append({
                "query": f"{target} career updates initiatives strategic quotes",
                "topic": "general",
                "time_range": "month",
                "search_depth": "advanced"
            })
            if obj:
                queries.append({
                    "query": f"{target} {obj} perspective background",
                    "topic": "general",
                    "time_range": "month",
                    "search_depth": "advanced"
                })
        else:
            # Company / Organization
            queries.append({
                "query": f"{target} latest news announcements product launches 2026",
                "topic": "news",
                "time_range": "month",
                "search_depth": "advanced"
            })
            queries.append({
                "query": f"{target} executive leadership strategy interviews hiring",
                "topic": "news",
                "time_range": "month",
                "search_depth": "advanced"
            })
            queries.append({
                "query": f"{target} funding revenue growth customers partnerships",
                "topic": "general",
                "time_range": "month",
                "search_depth": "advanced"
            })
            if obj:
                queries.append({
                    "query": f"{target} {obj} pain points competitors market expansion",
                    "topic": "general",
                    "time_range": "month",
                    "search_depth": "advanced"
                })

        return queries

    def conduct_research(self, req: BriefRequest) -> Dict[str, Any]:
        query_configs = self.generate_search_queries(req)
        executed_queries = []
        raw_results = []
        tavily_answers = []
        seen_urls = set()
        citations: List[SourceCitation] = []

        for q_cfg in query_configs:
            query = q_cfg["query"]
            executed_queries.append(query)
            try:
                search_response = self.client.search(
                    query=query,
                    topic=q_cfg.get("topic", "news"),
                    time_range=q_cfg.get("time_range", "month"),
                    search_depth=q_cfg.get("search_depth", "advanced"),
                    include_answer=True,
                    max_results=5
                )

                if search_response.get("answer"):
                    tavily_answers.append({
                        "query": query,
                        "answer": search_response["answer"]
                    })

                for item in search_response.get("results", []):
                    url = item.get("url", "").strip()
                    if not url or url in seen_urls:
                        continue
                    seen_urls.add(url)
                    citation = SourceCitation(
                        title=item.get("title", "Untitled Source"),
                        url=url,
                        snippet=item.get("content", ""),
                        published_date=item.get("published_date"),
                        score=item.get("score")
                    )
                    citations.append(citation)
                    raw_results.append(item)

            except Exception as e:
                logger.error(f"Tavily search failed for query '{query}': {e}")
                # Continue with other queries if one encounters an issue
                continue

        return {
            "target_name": req.target_name,
            "target_type": req.target_type,
            "queries": executed_queries,
            "tavily_answers": tavily_answers,
            "citations": citations,
            "raw_count": len(citations)
        }
