import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # completely blank slide

    # Theme colors
    C_NAVY = RGBColor(15, 23, 42)      # Slate 900
    C_BLUE = RGBColor(37, 99, 235)     # Blue 600
    C_LIGHT_BG = RGBColor(248, 250, 252) # Slate 50
    C_CARD_BG = RGBColor(255, 255, 255)
    C_BORDER = RGBColor(226, 232, 240)
    C_TEXT = RGBColor(51, 65, 85)      # Slate 700
    C_MUTED = RGBColor(100, 116, 139)  # Slate 500
    C_WHITE = RGBColor(255, 255, 255)
    C_ACCENT = RGBColor(13, 148, 136)  # Teal 600
    C_RED = RGBColor(220, 38, 38)

    def add_bg(slide, dark=False):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_NAVY if dark else C_LIGHT_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="BRIEFPILOT • GLOBAL AI HACKATHON 2026", dark=False):
        # Category pill / banner
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.5), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_BLUE if not dark else RGBColor(147, 197, 253)

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.5), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = C_NAVY if not dark else C_WHITE

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide (Dark Theme)
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, dark=True)

    tbox1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(4.5))
    tf1 = tbox1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "GLOBAL AI HACKATHON 2026 • TAVILY TRACK"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(96, 165, 250)

    p1 = tf1.add_paragraph()
    p1.text = "BriefPilot"
    p1.font.size = Pt(50)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Autonomous Pre-Meeting Executive Intelligence Agent"
    p2.font.size = Pt(22)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(8)

    p3 = tf1.add_paragraph()
    p3.text = "Transforming 30-day temporal web search via Tavily into high-leverage, hallucination-free executive briefings in seconds."
    p3.font.size = Pt(14)
    p3.font.color.rgb = RGBColor(148, 163, 184)
    p3.space_before = Pt(14)

    p4 = tf1.add_paragraph()
    p4.text = "Developer: Aman Kumar Sah (Kris) • Solo Entry: shahaman098 • London, UK"
    p4.font.size = Pt(11)
    p4.font.color.rgb = RGBColor(203, 213, 225)
    p4.space_before = Pt(28)

    # -------------------------------------------------------------
    # SLIDE 2: The Problem: The Pre-Meeting Blindspot
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "The Pre-Meeting Blindspot in Modern Business")

    cards_data_2 = [
        ("Time Sink (4-6 hrs/week)", "Executives, sales leads, and investors spend hours manually clicking through LinkedIn, Google News, and corporate blogs before every critical call.", "fa-clock"),
        ("The Freshness Void", "Standard search engines bias towards months-old SEO articles. Breaking product launches, leadership exits, and funding rounds from the last 30 days are routinely missed.", "fa-bolt"),
        ("Hallucination Hazard", "Raw LLMs invent company milestones and confuse timelines. Entering a meeting with inaccurate claims destroys credibility and torpedoes deals.", "fa-shield-halved")
    ]
    for i, (title, desc, _) in enumerate(cards_data_2):
        left = Inches(1.0 + i * 3.8)
        top = Inches(2.2)
        width = Inches(3.6)
        height = Inches(4.2)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tb = s2.shapes.add_textbox(left + Inches(0.2), top + Inches(0.3), width - Inches(0.4), height - Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(16)
        pt.font.bold = True
        pt.font.color.rgb = C_BLUE

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(12)
        pd.font.color.rgb = C_TEXT
        pd.space_before = Pt(14)

    # -------------------------------------------------------------
    # SLIDE 3: The Solution: BriefPilot
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "BriefPilot: Autonomous Pre-Meeting Intelligence")

    intro_box = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(0.8))
    intro_tf = intro_box.text_frame
    intro_tf.word_wrap = True
    ip = intro_tf.paragraphs[0]
    ip.text = "BriefPilot is an autonomous agent that ingests a meeting subject and strategic objective, orchestrates multi-angle 30-day temporal searches on Tavily, and generates a structured, verified briefing dossier."
    ip.font.size = Pt(13)
    ip.font.color.rgb = C_TEXT

    sol_cards = [
        ("1. 30-Day Fresh Timeline", "Chronological list of verified product releases, funding rounds, partnerships, and executive announcements from the past month with verbatim URLs."),
        ("2. Objective Alignment", "Customized strategic value levers showing exactly how your offering maps to their current challenges and market expansion."),
        ("3. High-Leverage Talking Points", "Contextualized conversation starters with natural phrasing ready to steer the conversation and build instant rapport."),
        ("4. Sensitive Landmines & Risks", "Identifies controversies, recent setbacks, or competitive threats so you never step on a conversational landmine."),
    ]
    for i, (title, desc) in enumerate(sol_cards):
        row = i // 2
        col = i % 2
        left = Inches(1.0 + col * 5.8)
        top = Inches(2.8 + row * 2.1)
        width = Inches(5.5)
        height = Inches(1.8)

        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tb = s3.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = C_BLUE

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(11)
        pd.font.color.rgb = C_TEXT
        pd.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 4: The Core Engine: Tavily Search API
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "The Power of Tavily: Why General Search Fails for Agents")

    tavily_points = [
        ("Precision Temporal Filtering (time_range='month')", "Unlike general search APIs that return pages indexed years ago, Tavily's temporal filter guarantees only events from the last 30 days are surfaced."),
        ("Specialized News & Deep Extraction (topic='news')", "Extracts authoritative announcements and verified journalism while eliminating clickbait, forum noise, and duplicate aggregators."),
        ("Sub-Second Latency for Real-Time Prep", "Tavily returns structured context in under 800ms, enabling BriefPilot to fire 4 concurrent queries and deliver a complete briefing in seconds."),
        ("Clean LLM Markdown & Verified Citations", "Bypasses brittle web scraping; returns pre-cleaned text and raw snippets with exact URLs and published timestamps.")
    ]
    for i, (title, desc) in enumerate(tavily_points):
        left = Inches(1.0)
        top = Inches(2.0 + i * 1.25)
        width = Inches(11.3)
        height = Inches(1.05)

        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tb = s4.shapes.add_textbox(left + Inches(0.3), top + Inches(0.1), width - Inches(0.6), height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = f"• {title}"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = C_NAVY

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(11)
        pd.font.color.rgb = C_TEXT
        pd.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 5: Architecture & Data Pipeline
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "BriefPilot Technical Architecture")

    steps = [
        ("1. Input Context", "Target (Company/Person)\nMeeting Objective\nAttendees & Org", C_BLUE),
        ("2. Query Decomposer", "4 Parallel Queries:\n• Fresh News 30d\n• Executive Moves\n• Growth/Funding\n• Strategic Friction", C_NAVY),
        ("3. Tavily Engine", "Concurrent Execution\ntime_range='month'\nsearch_depth='advanced'\nClean Citations", C_ACCENT),
        ("4. Gemini Synthesis", "Fact Grounding\nStrict JSON Schema\nRisk & Talking Points\nCitation Mapping", C_BLUE),
        ("5. Output Channels", "Interactive Web UI\nOne-Page PDF Dossier\nMarkdown & REST API", C_NAVY)
    ]

    for i, (title, desc, color) in enumerate(steps):
        left = Inches(0.8 + i * 2.4)
        top = Inches(2.5)
        width = Inches(2.2)
        height = Inches(3.6)

        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(2)

        tb = s5.shapes.add_textbox(left + Inches(0.15), top + Inches(0.2), width - Inches(0.3), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = color

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(10.5)
        pd.font.color.rgb = C_TEXT
        pd.space_before = Pt(12)

    # -------------------------------------------------------------
    # SLIDE 6: Demo & Live Prototype
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Working Prototype & Multi-Format Delivery")

    demo_features = [
        ("Interactive Web Application (FastAPI + Tailwind)", "Fast, responsive web dashboard with instant presets (Tavily AI, Maxim AI, Anthropic), live progress tracker, tabbed sections, and query inspection.", Inches(1.0), Inches(2.0)),
        ("One-Page Printable PDF Dossier (ReportLab)", "Generates a styled, compact PDF ready to print or view on iPad/mobile before walking into the conference room or joining Zoom.", Inches(6.8), Inches(2.0)),
        ("Full Scriptable CLI Runner (src/cli.py)", "Enables developers and power users to run BriefPilot from terminal or cron: `python3 -m src.cli --target 'Maxim AI' --objective 'Partner pitch'`.", Inches(1.0), Inches(4.3)),
        ("REST API for Calendar & CRM Webhooks", "Clean JSON endpoints (`/api/brief`, `/api/brief/pdf`, `/api/sample`) ready to integrate into Slack bots, HubSpot, or Google Calendar triggers.", Inches(6.8), Inches(4.3))
    ]
    for title, desc, left, top in demo_features:
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.5), Inches(2.0))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tb = s6.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), Inches(5.0), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = C_BLUE

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(11)
        pd.font.color.rgb = C_TEXT
        pd.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 7: Future Expansion: Bifrost & Calendar Integration
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Ecosystem Synergy & Bifrost LLM Gateway")

    bifrost_box = s7.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(1.0))
    bif_tf = bifrost_box.text_frame
    bif_tf.word_wrap = True
    bp = bif_tf.paragraphs[0]
    bp.text = "In enterprise production, BriefPilot leverages Maxim AI's Bifrost gateway to achieve 99.99% briefing availability and cost governance across hundreds of simultaneous morning calendar events."
    bp.font.size = Pt(13)
    bp.font.color.rgb = C_TEXT

    synergy_cards = [
        ("High-Concurrency Morning Spikes", "At 8:30 AM, corporate teams generate briefings for entire daily calendars. Bifrost routes traffic across backup model providers with sub-millisecond overhead."),
        ("Latency & Cost Observability", "Bifrost logs every token and search latency metric, ensuring enterprise compliance and budget enforcement."),
        ("Automated Calendar Listeners", "Connecting BriefPilot to Google Calendar and Microsoft Graph to automatically deliver a one-page PDF brief to email 15 minutes before every external meeting.")
    ]
    for i, (title, desc) in enumerate(synergy_cards):
        left = Inches(1.0 + i * 3.8)
        top = Inches(3.0)
        width = Inches(3.6)
        height = Inches(3.4)

        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tb = s7.shapes.add_textbox(left + Inches(0.2), top + Inches(0.3), width - Inches(0.4), height - Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = C_BLUE

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(11)
        pd.font.color.rgb = C_TEXT
        pd.space_before = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 8: Hackathon Submission & Summary (Dark Theme)
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8, dark=True)

    tbox8 = s8.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(5.0))
    tf8 = tbox8.text_frame
    tf8.word_wrap = True

    p0 = tf8.paragraphs[0]
    p0.text = "GLOBAL AI HACKATHON 2026 • SUBMISSION SUMMARY"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(96, 165, 250)

    p1 = tf8.add_paragraph()
    p1.text = "BriefPilot is Ready to Ship"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    bullets = [
        "Track: Tavily Pre-Meeting Briefing Agent (AI Agents & Intelligent Systems)",
        "Core Tech: Tavily Search API (30-day temporal filters) + Google Gemini (grounded synthesis)",
        "Deliverables: Public GitHub repo, responsive web app, CLI tool, PDF export engine, and pitch deck",
        "Team: Aman Kumar Sah (Kris) • Solo (team 'shahaman098') • Brunel University London AI",
        "Repository: https://github.com/shahaman098/briefpilot"
    ]
    for b in bullets:
        pb = tf8.add_paragraph()
        pb.text = f"✓  {b}"
        pb.font.size = Pt(14)
        pb.font.color.rgb = RGBColor(226, 232, 240)
        pb.space_before = Pt(10)

    os.makedirs("docs", exist_ok=True)
    prs.save("docs/pitch-deck.pptx")
    print("Saved presentation to docs/pitch-deck.pptx")

if __name__ == "__main__":
    create_presentation()
