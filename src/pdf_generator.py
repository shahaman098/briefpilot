import io
from typing import Union
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from src.schemas import BriefResponse

class BriefPDFGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._init_custom_styles()

    def _init_custom_styles(self):
        # Palette: Deep Navy, Electric Blue, Slate Grey, Dark Charcoal
        self.c_primary = colors.HexColor("#0F172A")    # Slate 900
        self.c_accent = colors.HexColor("#2563EB")     # Blue 600
        self.c_teal = colors.HexColor("#0D9488")       # Teal 600
        self.c_muted = colors.HexColor("#64748B")      # Slate 500
        self.c_light_bg = colors.HexColor("#F8FAFC")   # Slate 50
        self.c_border = colors.HexColor("#E2E8F0")     # Slate 200
        self.c_red = colors.HexColor("#DC2626")        # Red 600

        self.styles.add(ParagraphStyle(
            name="DocHeader",
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=self.c_primary
        ))
        self.styles.add(ParagraphStyle(
            name="DocSubHeader",
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=self.c_muted
        ))
        self.styles.add(ParagraphStyle(
            name="SectionTitle",
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=self.c_accent,
            spaceAfter=4,
            spaceBefore=8
        ))
        self.styles.add(ParagraphStyle(
            name="BodyTextCustom",
            fontName="Helvetica",
            fontSize=8.5,
            leading=11.5,
            textColor=colors.HexColor("#334155")
        ))
        self.styles.add(ParagraphStyle(
            name="OneLinerText",
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12.5,
            textColor=self.c_primary
        ))
        self.styles.add(ParagraphStyle(
            name="ItemTitle",
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=11,
            textColor=self.c_primary
        ))
        self.styles.add(ParagraphStyle(
            name="ItemSub",
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            textColor=self.c_muted
        ))
        self.styles.add(ParagraphStyle(
            name="RedFlagText",
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            textColor=colors.HexColor("#991B1B")
        ))
        self.styles.add(ParagraphStyle(
            name="SourceLink",
            fontName="Helvetica",
            fontSize=7.5,
            leading=9.5,
            textColor=self.c_accent
        ))

    def generate(self, brief: BriefResponse, output: Union[str, io.BytesIO] = None) -> Union[str, io.BytesIO]:
        if output is None:
            output = io.BytesIO()

        doc = SimpleDocTemplate(
            output,
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        story = []

        # 1. Top Header Banner
        header_text = f"<b>BRIEFPILOT</b> &nbsp;|&nbsp; Executive Pre-Meeting Intelligence Dossier"
        meta_text = f"Target: <b>{brief.target_name}</b> ({brief.target_type.upper()}) &nbsp;•&nbsp; Objective: <i>{brief.meeting_objective}</i> &nbsp;•&nbsp; Generated: {brief.generated_at[:10]}"
        audit_text = f"<b>Audit Status:</b> {brief.audit_status} &nbsp;|&nbsp; <b>Grounding Score:</b> {int(brief.grounding_score * 100)}% &nbsp;|&nbsp; <b>Verified Claims:</b> {brief.verified_claims_count} &nbsp;|&nbsp; <b>Tavily 30d Citations:</b> {len(brief.sources)}"
        
        story.append(Paragraph(header_text, self.styles["DocHeader"]))
        story.append(Paragraph(meta_text, self.styles["DocSubHeader"]))
        story.append(Paragraph(audit_text, self.styles["ItemSub"]))
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width="100%", thickness=1.5, color=self.c_accent, spaceAfter=8))

        # 2. Executive One-Liner Box
        one_liner_p = Paragraph(f"<b>Key Takeaway:</b> {brief.one_liner}", self.styles["OneLinerText"])
        one_liner_table = Table([[one_liner_p]], colWidths=[540])
        one_liner_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), self.c_light_bg),
            ('BOX', (0,0), (-1,-1), 1, self.c_border),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(one_liner_table)
        story.append(Spacer(1, 8))

        # 3. Key Metrics Table (if any)
        if brief.key_metrics:
            story.append(Paragraph("ORGANIZATION SNAPSHOT", self.styles["SectionTitle"]))
            metrics_data = []
            keys = list(brief.key_metrics.keys())
            # 2 columns per row
            for i in range(0, len(keys), 2):
                k1 = keys[i]
                v1 = brief.key_metrics[k1]
                cell1 = Paragraph(f"<b>{k1}:</b> {v1}", self.styles["BodyTextCustom"])
                if i + 1 < len(keys):
                    k2 = keys[i+1]
                    v2 = brief.key_metrics[k2]
                    cell2 = Paragraph(f"<b>{k2}:</b> {v2}", self.styles["BodyTextCustom"])
                else:
                    cell2 = Paragraph("", self.styles["BodyTextCustom"])
                metrics_data.append([cell1, cell2])

            m_table = Table(metrics_data, colWidths=[270, 270])
            m_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
                ('INNERGRID', (0,0), (-1,-1), 0.5, self.c_border),
                ('BOX', (0,0), (-1,-1), 0.5, self.c_border),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ]))
            story.append(m_table)
            story.append(Spacer(1, 6))

        # 4. Executive Summary
        story.append(Paragraph("EXECUTIVE SUMMARY & CURRENT STANDING", self.styles["SectionTitle"]))
        story.append(Paragraph(brief.executive_summary, self.styles["BodyTextCustom"]))
        story.append(Spacer(1, 8))

        # 5. Last 30-Day Intelligence Timeline
        if brief.timeline_30d:
            story.append(Paragraph("30-DAY FRESH INTELLIGENCE TIMELINE (TAVILY VERIFIED)", self.styles["SectionTitle"]))
            t_data = []
            for item in brief.timeline_30d[:5]:
                badge = f"[{item.category.upper()}]"
                date_str = item.date
                headline = f"<b>{date_str} • {badge} {item.headline}</b>"
                summary = item.summary
                t_p = Paragraph(f"{headline}<br/>{summary}", self.styles["BodyTextCustom"])
                t_data.append([t_p])

            t_table = Table(t_data, colWidths=[540])
            t_table.setStyle(TableStyle([
                ('LINEBELOW', (0,0), (-1,-1), 0.5, self.c_border),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('LEFTPADDING', (0,0), (-1,-1), 2),
                ('RIGHTPADDING', (0,0), (-1,-1), 2),
            ]))
            story.append(t_table)
            story.append(Spacer(1, 8))

        # 6. Strategic Opportunities & Talking Points
        if brief.strategic_opportunities or brief.talking_points:
            story.append(Paragraph("STRATEGIC LEVERS & HIGH-IMPACT TALKING POINTS", self.styles["SectionTitle"]))
            st_data = []
            for tp in brief.talking_points[:3]:
                p1 = Paragraph(f"<b>• {tp.topic}:</b> {tp.context}", self.styles["BodyTextCustom"])
                p2 = Paragraph(f"<i>Suggested Phrasing:</i> \"{tp.suggested_phrasing}\"", self.styles["OneLinerText"])
                st_data.append([p1])
                st_data.append([p2])

            for so in brief.strategic_opportunities[:2]:
                p = Paragraph(f"<b>• Leverage {so.area}:</b> {so.actionable_lever} (Observation: {so.observation})", self.styles["BodyTextCustom"])
                st_data.append([p])

            st_table = Table(st_data, colWidths=[540])
            st_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), self.c_light_bg),
                ('BOX', (0,0), (-1,-1), 0.5, self.c_border),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ]))
            story.append(st_table)
            story.append(Spacer(1, 8))

        # 7. Red Flags & Sensitivities
        if brief.red_flags:
            story.append(Paragraph("RISKS & TOPICS TO NAVIGATE CAREFULLY", self.styles["SectionTitle"]))
            rf_data = []
            for rf in brief.red_flags[:2]:
                p = Paragraph(f"<b>⚠️ {rf.concern}:</b> {rf.detail} — <i>Strategy: {rf.handling_advice}</i>", self.styles["RedFlagText"])
                rf_data.append([p])
            rf_table = Table(rf_data, colWidths=[540])
            rf_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
                ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#FCA5A5")),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ]))
            story.append(rf_table)
            story.append(Spacer(1, 8))

        # 8. Sourced Reference Citations
        if brief.sources:
            story.append(KeepTogether([
                Paragraph("VERIFIED SOURCED DOSSIER (TAVILY CITATIONS)", self.styles["SectionTitle"]),
                *[
                    Paragraph(f"[{i+1}] <b>{s.title}</b> ({s.published_date or 'Recent'}) — <font color='#2563EB'><u>{s.url}</u></font>", self.styles["SourceLink"])
                    for i, s in enumerate(brief.sources[:6])
                ]
            ]))

        doc.build(story)
        return output
