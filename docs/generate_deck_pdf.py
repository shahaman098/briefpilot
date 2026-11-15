import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable

def generate_pdf_deck():
    os.makedirs("docs", exist_ok=True)
    pdf_path = "docs/pitch-deck.pdf"
    
    # Landscape letter format (11 x 8.5 in)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(letter),
        leftMargin=40,
        rightMargin=40,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    c_navy = colors.HexColor("#0F172A")
    c_blue = colors.HexColor("#2563EB")
    c_slate = colors.HexColor("#334155")
    c_light = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#CBD5E1")

    styles.add(ParagraphStyle('DeckCategory', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=c_blue))
    styles.add(ParagraphStyle('DeckSlideTitle', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=c_navy, spaceAfter=8))
    styles.add(ParagraphStyle('DeckBody', fontName='Helvetica', fontSize=10.5, leading=15, textColor=c_slate))
    styles.add(ParagraphStyle('DeckCardTitle', fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=c_blue, spaceAfter=4))
    styles.add(ParagraphStyle('DeckCoverPre', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=c_blue))
    styles.add(ParagraphStyle('DeckCoverTitle', fontName='Helvetica-Bold', fontSize=34, leading=40, textColor=c_navy, spaceAfter=8))
    styles.add(ParagraphStyle('DeckCoverSub', fontName='Helvetica', fontSize=16, leading=22, textColor=colors.HexColor("#475569")))

    story = []

    # Slide 1: Cover
    story.append(Spacer(1, 40))
    story.append(Paragraph("GLOBAL AI HACKATHON 2026 • TAVILY TRACK", styles['DeckCoverPre']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("BriefPilot", styles['DeckCoverTitle']))
    story.append(Paragraph("Autonomous Pre-Meeting Executive Intelligence Agent", styles['DeckCoverSub']))
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=2, color=c_blue, spaceAfter=15))
    story.append(Paragraph("Transforming 30-day temporal web search via <b>Tavily</b> into high-leverage, hallucination-free executive briefings in seconds.<br/><br/><b>Developer:</b> Aman Kumar Sah (Kris) &nbsp;•&nbsp; <b>Solo Team:</b> shahaman098 &nbsp;•&nbsp; <b>Institution:</b> Brunel University London AI", styles['DeckBody']))
    story.append(PageBreak())

    # Slide 2: Problem
    story.append(Paragraph("BRIEFPILOT • PROBLEM STATEMENT", styles['DeckCategory']))
    story.append(Paragraph("The Pre-Meeting Blindspot in Modern Business", styles['DeckSlideTitle']))
    story.append(Paragraph("High-stakes meetings frequently stall or fail due to asymmetric, stale, or hallucinated intelligence:", styles['DeckBody']))
    story.append(Spacer(1, 10))
    
    col1 = [
        Paragraph("<b>1. Time Sink (4-6 Hours/Week)</b>", styles['DeckCardTitle']),
        Paragraph("Executives, sales reps, and founders spend hours manually combing LinkedIn, Google News, and corporate blogs before critical calls.", styles['DeckBody'])
    ]
    col2 = [
        Paragraph("<b>2. The Freshness Void</b>", styles['DeckCardTitle']),
        Paragraph("General search engines bias towards months-old SEO articles. Product releases, funding rounds, and leadership exits from the past 30 days are missed.", styles['DeckBody'])
    ]
    col3 = [
        Paragraph("<b>3. Hallucination Hazard</b>", styles['DeckCardTitle']),
        Paragraph("Raw LLMs invent company milestones and confuse timelines. Citing inaccurate facts during partner or investor discussions destroys deal credibility.", styles['DeckBody'])
    ]
    t2 = Table([[col1, col2, col3]], colWidths=[230, 230, 230])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light),
        ('BOX', (0,0), (-1,-1), 0.5, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t2)
    story.append(PageBreak())

    # Slide 3: Solution
    story.append(Paragraph("BRIEFPILOT • THE SOLUTION", styles['DeckCategory']))
    story.append(Paragraph("Autonomous Multi-Query Temporal Intelligence", styles['DeckSlideTitle']))
    story.append(Paragraph("BriefPilot decomposes meeting context into targeted 30-day temporal queries, aggregates verified sources via Tavily, and synthesizes an executive briefing dossier in seconds.", styles['DeckBody']))
    story.append(Spacer(1, 10))

    s_items = [
        [
            Paragraph("<b>• 30-Day Fresh Timeline:</b> Chronological list of verified product releases, funding rounds, partnerships, and executive moves with verbatim URLs.", styles['DeckBody']),
            Paragraph("<b>• Objective Alignment:</b> Strategic value levers showing exactly how your offering maps to their current challenges and market expansion.", styles['DeckBody'])
        ],
        [
            Paragraph("<b>• High-Impact Talking Points:</b> Contextualized conversation starters with natural phrasing ready to steer conversation and build rapport.", styles['DeckBody']),
            Paragraph("<b>• Sensitive Landmines & Risks:</b> Identifies controversies, recent setbacks, or competitive threats to avoid embarrassing conversational missteps.", styles['DeckBody'])
        ]
    ]
    t3 = Table(s_items, colWidths=[345, 345])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light),
        ('BOX', (0,0), (-1,-1), 0.5, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t3)
    story.append(PageBreak())

    # Slide 4: Why Tavily
    story.append(Paragraph("BRIEFPILOT • CORE TECHNOLOGY", styles['DeckCategory']))
    story.append(Paragraph("Why Tavily Search API is the Foundational Engine", styles['DeckSlideTitle']))
    story.append(Spacer(1, 6))

    tav_items = [
        [Paragraph("<b>Precision Temporal Filtering (time_range='month')</b><br/>Guarantees only events published within the last 30 days are retrieved, eliminating stale historical search noise.", styles['DeckBody'])],
        [Paragraph("<b>Specialized News & Deep Extraction (topic='news')</b><br/>Pulls authoritative corporate announcements, verified journalism, and executive commentary directly.", styles['DeckBody'])],
        [Paragraph("<b>Sub-Second Latency for Real-Time Execution</b><br/>Enables BriefPilot to dispatch 4 concurrent queries and synthesize a full multi-dimensional briefing in under 5 seconds.", styles['DeckBody'])],
        [Paragraph("<b>LLM-Optimized Clean Markdown & Grounded Citations</b><br/>Bypasses brittle web scrapers and paywall junk by delivering clean markdown context ready for reasoning models.", styles['DeckBody'])]
    ]
    t4 = Table(tav_items, colWidths=[690])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light),
        ('BOX', (0,0), (-1,-1), 0.5, c_border),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t4)
    story.append(PageBreak())

    # Slide 5: Architecture
    story.append(Paragraph("BRIEFPILOT • ARCHITECTURE", styles['DeckCategory']))
    story.append(Paragraph("End-to-End Intelligence Pipeline", styles['DeckSlideTitle']))
    story.append(Spacer(1, 6))

    pipe_steps = [
        Paragraph("<b>1. Ingestion Layer</b><br/>Accepts Target Entity, Type, Meeting Objective, Attendees, and User Org.", styles['DeckBody']),
        Paragraph("<b>2. Query Decomposer</b><br/>Spawns 4 parallel queries targeting 30d news, executive quotes, funding, and pain points.", styles['DeckBody']),
        Paragraph("<b>3. Tavily API Search</b><br/>Concurrent temporal search with topic='news', search_depth='advanced', and answer generation.", styles['DeckBody']),
        Paragraph("<b>4. Gemini Grounding</b><br/>Synthesizes verified timeline, strategic levers, talking points, and red flags in strict JSON.", styles['DeckBody']),
        Paragraph("<b>5. Multi-Output Delivery</b><br/>Interactive web dashboard, downloadable 1-page PDF, CLI script, and REST API.", styles['DeckBody'])
    ]
    t5 = Table([[p] for p in pipe_steps], colWidths=[690])
    t5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_light),
        ('BOX', (0,0), (-1,-1), 0.5, c_border),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t5)
    story.append(PageBreak())

    # Slide 6: Summary & Delivery
    story.append(Paragraph("BRIEFPILOT • HACKATHON SUMMARY", styles['DeckCategory']))
    story.append(Paragraph("Shipped Prototype & Evaluation Details", styles['DeckSlideTitle']))
    story.append(Spacer(1, 10))

    summary_items = [
        ("Hackathon", "Global AI Hackathon 2026 (HackCulture / Geek Room)"),
        ("Theme / Track", "Tavily: Pre-Meeting Briefing Agent (AI Agents & Intelligent Systems)"),
        ("Developer", "Aman Kumar Sah (Kris) • Solo (team 'shahaman098')"),
        ("Repository", "https://github.com/shahaman098/briefpilot (Public)"),
        ("Deliverables", "FastAPI Web UI, ReportLab 1-Page PDF Generator, Scriptable CLI, Pitch Deck"),
        ("Verification", "100% grounded in live 30-day Tavily search results with verbatim URL attribution")
    ]
    t6_data = [[Paragraph(f"<b>{k}</b>", styles['DeckBody']), Paragraph(v, styles['DeckBody'])] for k, v in summary_items]
    t6 = Table(t6_data, colWidths=[200, 490])
    t6.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.5, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t6)

    doc.build(story)
    print("Saved PDF deck to docs/pitch-deck.pdf")

if __name__ == "__main__":
    generate_pdf_deck()
