"""
Builds "Excel Module 3 (CUNEF style).pptx" from the approved outline at
`04-Course Redesign 2026-27/Slide Conversion Outlines/Excel Module 3 -
Outline.md`, using the cunef-pptx skill's builder library. Combines the two
small original framing decks ("Use of Excel for data analysis - Pivot
tables.pptx" and "...Conditional formats and sparklines.pptx") into one
deck, matching the folder's own name for the module.

No speaker notes, per this conversion project's standing decision
(Slide_Conversion_Plan.md). The real teaching content for PivotTables lives
in the separate, out-of-scope "Mastering PivotTables.pdf" (unmodified
third-party material with no editable source) - this deck only converts
the two genuinely-editable framing decks.
"""

import sys
import os

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_THIS_DIR, "..", "..", ".claude", "skills", "cunef-pptx"))
import cunef_pptx_builder as cb

prs = cb.new_presentation()

# ===========================================================================
# Title + Roadmap
# ===========================================================================

s = cb.add_title_slide(
    prs, "Excel Module 3",
    "PivotTables, Conditional Formatting & Sparklines",
)

s = cb.add_roadmap_slide(prs, "Roadmap", [
    ("1", "PivotTables"),
    ("2", "Formatting"),
])

# ===========================================================================
# Section: PivotTables
# ===========================================================================

s = cb.add_section_divider(prs, 1, "PivotTables")

s = cb.add_three_card_slide(
    prs, "What are PivotTables", "1 | PivotTables",
    [
        ("Faster", "Does everything you've already learned about analyzing data, just faster and more efficient."),
        ("Exploratory", "Aggregate and present data in many different ways, quickly - ideal for exploratory analysis."),
        ("Real limits", "Some options and charts available for Data Ranges or Tables don't work with PivotTables."),
    ],
)

s = cb.add_bullet_list_slide(
    prs, "Core PivotTable skills", "1 | PivotTables",
    [
        "Create a PivotTable to analyze worksheet data",
        "Use the Field List to arrange fields",
        "Filter data in a PivotTable",
        "Create a PivotChart",
    ],
)

s = cb.add_bullet_list_slide(
    prs, "Further reading", "1 | PivotTables",
    [
        "Video: Overview of PivotTables and PivotCharts - Microsoft Support",
        "Video: Basic tutorial on PivotTables and PivotCharts - YouTube",
    ],
)

s = cb.add_citation_slide(
    prs, "Practice files", "1 | PivotTables",
    "Penguins PivotTables.xlsx and Exercises PivotTables.xlsx",
    "In this folder - try each feature yourself",
)

s = cb.add_statement_slide(
    prs,
    "A PivotTable does everything you've already learned - just faster. "
    "The real skill is knowing when to reach for one.",
)

# ===========================================================================
# Section: Conditional Formatting & Sparklines
# ===========================================================================

s = cb.add_section_divider(prs, 2, "Formatting")

s = cb.add_two_column_slide(
    prs, "Add quick visual information to tables", "2 | Formatting",
    "Conditional formatting",
    [
        "Highlights information automatically, based on rules you set",
        "Official guide: Microsoft Support",
    ],
    "Sparklines",
    [
        "Tiny in-cell charts that show a data trend at a glance",
        "Official guides: Microsoft Support (create + use)",
    ],
)

s = cb.add_citation_slide(
    prs, "Video: replaced", "2 | Formatting",
    "Video: Conditional formatting & sparklines",
    "Replaced by an in-house screencast (2 Spanish/unofficial YouTube "
    "videos removed - see BUTI_2.0_Remaking_Plan.md §3.4, top "
    "production priority)",
)

s = cb.add_citation_slide(
    prs, "Practice file", "2 | Formatting",
    "Conditional formatting and sparklines.xlsx",
    "In this folder",
)

# ===========================================================================
# Closing
# ===========================================================================

s = cb.add_statement_slide(
    prs,
    "PivotTables and conditional formatting turn a spreadsheet into an "
    "at-a-glance dashboard - once you know the basics, the tool does the "
    "heavy lifting.",
)

s = cb.add_closing_slide(prs)

# ===========================================================================

out_pptx = os.path.join(_THIS_DIR, "Excel Module 3 (CUNEF style).pptx")
out_pdf = os.path.join(_THIS_DIR, "Excel Module 3 (CUNEF style).pdf")
cb.save(prs, out_pptx)
print("Saved:", out_pptx, "-", len(prs.slides), "slides")
cb.export_to_pdf(out_pptx, out_pdf)
print("Exported:", out_pdf)
