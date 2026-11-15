from src.schemas import BriefResponse, TimelineItem, StrategicOpportunity, TalkingPoint, RedFlag, SourceCitation

SAMPLE_BRIEF = BriefResponse(
    id="brief_20261115_sample_tavily",
    target_name="Tavily AI",
    target_type="company",
    meeting_objective="Explore embedding Tavily Search API into enterprise pre-meeting workflow",
    generated_at="2026-11-15T04:50:00Z",
    one_liner="Acquired by Nebius for up to $400M and powering over 3M developers with 350M+ monthly queries, Tavily AI provides sub-second, LLM-optimized real-time search infrastructure ideal for powering BriefPilot's automated pre-meeting intelligence workflow.",
    executive_summary="Tavily AI has cemented its position as the de facto search engine built specifically for autonomous AI agents, LLM pipelines, and retrieval-augmented generation (RAG). Operating with sub-second response times, Tavily replaces slow, scraping-heavy web crawlers with unified endpoints that return clean, LLM-ready markdown, structured entity context, and temporal filters.\n\nOver the past 30 days, Tavily's ecosystem expansion has accelerated post-acquisition by Nebius, with integrations across major enterprise agent platforms and deep research workflows. The platform now supports multi-modal query routing, domain weighting, and specialized news topic extraction that enable hyper-fresh meeting intelligence without hallucination.",
    key_metrics={
        "Primary Focus": "Search & Intelligence Infrastructure for AI Agents",
        "Parent / Acquirer": "Nebius Group ($400M acquisition)",
        "Monthly Query Volume": "350M+ API requests",
        "Active Developer Base": "3,000,000+ AI engineers & researchers",
        "Key Differentiator": "Sub-second temporal filtering (30-day freshness) & LLM markdown extraction"
    },
    timeline_30d=[
        TimelineItem(
            date="2026-11-13",
            headline="Tavily Deep Search & Research Optimization Upgrades",
            summary="Rolled out enhanced temporal precision filters and high-concurrency rate limits, enabling multi-agent workflows to synthesize deep research briefs with zero latency degradation.",
            category="Product",
            source_url="https://docs.tavily.com"
        ),
        TimelineItem(
            date="2026-11-08",
            headline="Nebius AI Cloud Deepens Tavily Native Integration",
            summary="Announced turnkey deployment of Tavily MCP server and agent tools across Nebius Cloud compute nodes, offering enterprise AI developers bundled compute and search.",
            category="Partnership",
            source_url="https://nebius.com"
        ),
        TimelineItem(
            date="2026-10-29",
            headline="Tavily Reaches 3 Million Active AI Builders Milestone",
            summary="Crossed 350M monthly queries as leading AI frameworks (LangChain, LlamaIndex, AutoGen, CrewAI) standardize on Tavily for real-time web retrieval.",
            category="Growth",
            source_url="https://tavily.com"
        ),
        TimelineItem(
            date="2026-10-22",
            headline="Launch of Remote MCP Server for Agentic Web Search",
            summary="Released hosted Remote Model Context Protocol (MCP) endpoints allowing instant zero-install agent connectivity across Cursor, Claude, and custom enterprise agents.",
            category="Product",
            source_url="https://docs.tavily.com/documentation/mcp"
        )
    ],
    strategic_opportunities=[
        StrategicOpportunity(
            area="Pre-Meeting Autonomous Intelligence",
            observation="Enterprise knowledge workers spend 4-6 hours weekly manually researching upcoming meetings; existing search engines return outdated SEO spam rather than 30-day verified milestones.",
            actionable_lever="Position BriefPilot as the flagship enterprise application of Tavily's temporal search, demonstrating clear executive ROI and developer API consumption."
        ),
        StrategicOpportunity(
            area="Bifrost & Maxim AI Gateway Synergy",
            observation="Enterprises deploying pre-meeting agents require strict latency governance, fallback providers, and cost observability across LLM and search calls.",
            actionable_lever="Combine Tavily's search precision with Bifrost's routing layer to deliver a zero-downtime, audited intelligence workflow for financial and corporate clients."
        )
    ],
    talking_points=[
        TalkingPoint(
            topic="30-Day Freshness vs Traditional Web Crawlers",
            context="Traditional search APIs often index cached or stale pages, causing agents to cite months-old events as breaking news.",
            suggested_phrasing="How does Tavily's time_range='month' algorithm filter out re-indexed stale content to guarantee our executive briefings only surface verifiable 30-day intelligence?"
        ),
        TalkingPoint(
            topic="High-Concurrency Enterprise Burst Routing",
            context="Corporate calendars experience heavy spikes at 8:00 AM across hundreds of executives generating briefings simultaneously.",
            suggested_phrasing="We're designing BriefPilot for enterprise morning sync spikes. What are your recommended architectural best practices for concurrency and batch query multiplexing?"
        ),
        TalkingPoint(
            topic="Tavily Remote MCP Adoption",
            context="Tavily recently launched remote MCP endpoints for direct agent consumption.",
            suggested_phrasing="We loved your new Remote MCP release—are there plans to introduce specialized schemas for structured pre-meeting entity dossiers directly in MCP?"
        )
    ],
    red_flags=[
        RedFlag(concern="Treating Tavily as a Generic Google/Bing Wrapper", detail="Tavily is custom-built for AI agents with proprietary aggregation, extraction, and ranking algorithms, not a simple pass-through.", handling_advice="Focus technical discussion on LLM-optimized extraction, clean markdown, and agentic workflows rather than raw consumer search comparison."),
        RedFlag(concern="Ignoring Strict Rate Limits on Free / Dev Tiers", detail="Attempting 20 concurrent deep searches on entry tiers can trigger 429 throttling during live demonstrations.", handling_advice="Ensure query concurrency is gracefully throttled, cached, and backed by error handling.")
    ],
    sources=[
        SourceCitation(
            title="Tavily AI Official Platform & Documentation",
            url="https://tavily.com",
            snippet="The search engine built specifically for AI agents and LLMs. Delivering factual, real-time, clean web intelligence in seconds.",
            published_date="2026-11-14",
            score=0.98
        ),
        SourceCitation(
            title="Nebius Closes Strategic Acquisition of Tavily AI",
            url="https://nebius.com/news/tavily-acquisition",
            snippet="Nebius expands its full-stack AI cloud with the acquisition of search platform Tavily to empower next-generation autonomous agents.",
            published_date="2026-11-05",
            score=0.95
        ),
        SourceCitation(
            title="Tavily Model Context Protocol (MCP) Guide",
            url="https://docs.tavily.com/documentation/mcp",
            snippet="Connect AI agents to real-time search with Tavily's official MCP server. Supports Cursor, Claude Code, and Antigravity.",
            published_date="2026-10-25",
            score=0.92
        )
    ],
    tavily_search_queries=[
        "Tavily AI latest news announcements product launches 2026",
        "Tavily AI executive leadership strategy interviews hiring",
        "Tavily AI funding revenue growth customers partnerships",
        "Tavily AI pre-meeting intelligence pain points competitors market expansion"
    ]
)
