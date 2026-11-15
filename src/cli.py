import argparse
import json
import sys
from pathlib import Path
from src.schemas import BriefRequest
from src.tavily_agent import TavilyResearchAgent
from src.synthesizer import BriefSynthesizer
from src.pdf_generator import BriefPDFGenerator

def brief_to_markdown(brief) -> str:
    md = []
    md.append(f"# Executive Briefing: {brief.target_name} ({brief.target_type.upper()})\n")
    md.append(f"**Meeting Objective:** {brief.meeting_objective}  ")
    md.append(f"**Generated:** {brief.generated_at}  ")
    md.append(f"**Brief ID:** `{brief.id}`\n")
    md.append("---\n")
    md.append(f"## Key Takeaway\n> {brief.one_liner}\n")
    
    if brief.key_metrics:
        md.append("## Organization Snapshot\n")
        for k, v in brief.key_metrics.items():
            md.append(f"- **{k}:** {v}")
        md.append("")

    md.append(f"## Executive Summary & Standing\n{brief.executive_summary}\n")

    if brief.timeline_30d:
        md.append("## 30-Day Fresh Intelligence Timeline\n")
        for item in brief.timeline_30d:
            src = f" ([Source]({item.source_url}))" if item.source_url else ""
            md.append(f"### {item.date} — [{item.category.upper()}] {item.headline}")
            md.append(f"{item.summary}{src}\n")

    if brief.strategic_opportunities:
        md.append("## Strategic Opportunities & Value Levers\n")
        for so in brief.strategic_opportunities:
            md.append(f"- **{so.area}**: {so.observation}")
            md.append(f"  *Actionable Lever:* {so.actionable_lever}\n")

    if brief.talking_points:
        md.append("## High-Impact Talking Points\n")
        for tp in brief.talking_points:
            md.append(f"- **{tp.topic}**: {tp.context}")
            md.append(f"  *Suggested Phrasing:* \"{tp.suggested_phrasing}\"\n")

    if brief.red_flags:
        md.append("## Red Flags & Sensitivities to Avoid\n")
        for rf in brief.red_flags:
            md.append(f"- ⚠️ **{rf.concern}**: {rf.detail}")
            md.append(f"  *Handling Advice:* {rf.handling_advice}\n")

    if brief.sources:
        md.append("## Grounded Tavily Sources\n")
        for i, s in enumerate(brief.sources, 1):
            d = f" ({s.published_date})" if s.published_date else ""
            md.append(f"{i}. [{s.title}]({s.url}){d}")
        md.append("")

    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="BriefPilot: Autonomous Pre-Meeting Intelligence Agent")
    parser.add_argument("--target", required=True, help="Target company or executive name")
    parser.add_argument("--type", choices=["company", "person"], default="company", help="Target type")
    parser.add_argument("--objective", required=True, help="Meeting objective / goal")
    parser.add_argument("--org", default=None, help="Your organization name")
    parser.add_argument("--attendees", default=None, help="Names of key attendees")
    parser.add_argument("--focus", default=None, help="Custom focus areas")
    parser.add_argument("--out-md", help="Path to save markdown output")
    parser.add_argument("--out-pdf", help="Path to save PDF output")
    parser.add_argument("--out-json", help="Path to save JSON output")

    args = parser.parse_args()

    req = BriefRequest(
        target_name=args.target,
        target_type=args.type,
        meeting_objective=args.objective,
        user_organization=args.org,
        attendees=args.attendees,
        custom_focus=args.focus
    )

    print(f"[*] BriefPilot starting research on '{args.target}' ({args.type})...")
    agent = TavilyResearchAgent()
    research = agent.conduct_research(req)
    print(f"[✓] Retrieved {len(research['citations'])} verified sources across {len(research['queries'])} queries.")

    print("[*] Synthesizing executive intelligence with Gemini...")
    synthesizer = BriefSynthesizer()
    brief = synthesizer.synthesize(req, research)
    print(f"[✓] Executive Brief generated: {brief.one_liner}")

    md_content = brief_to_markdown(brief)

    if args.out_md:
        Path(args.out_md).write_text(md_content, encoding="utf-8")
        print(f"[✓] Saved Markdown to {args.out_md}")

    if args.out_pdf:
        pdf_gen = BriefPDFGenerator()
        pdf_gen.generate(brief, args.out_pdf)
        print(f"[✓] Saved PDF to {args.out_pdf}")

    if args.out_json:
        Path(args.out_json).write_text(brief.model_dump_json(indent=2), encoding="utf-8")
        print(f"[✓] Saved JSON to {args.out_json}")

    if not (args.out_md or args.out_pdf or args.out_json):
        print("\n" + md_content)

if __name__ == "__main__":
    main()
