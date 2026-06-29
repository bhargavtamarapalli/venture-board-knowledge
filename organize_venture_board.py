
import shutil
from pathlib import Path

# ------------------------------------------------------------------
# Venture Board Knowledge Base Organizer
# Place this script in the folder containing all downloaded .md files.
# ------------------------------------------------------------------

ROOT = Path.cwd()

FOLDERS = {
    "00_System": [
        "00_Master_Index.md",
        "GPT_Operating_System.md",
        "Scoring_Model.md",
        "Decision_Committee.md",
    ],
    "01_Frameworks": [
        "Framework_Lean_Canvas.md",
        "Framework_Business_Model_Canvas.md",
        "Framework_Value_Proposition_Canvas.md",
        "Framework_Jobs_To_Be_Done.md",
        "Framework_SWOT.md",
        "Framework_Porters_Five_Forces.md",
        "Framework_Blue_Ocean.md",
        "Framework_MoSCoW.md",
        "Framework_RICE.md",
        "Framework_Kano.md",
    ],
    "02_Market": [
        "Market_TAM_SAM_SOM.md",
        "Market_Sizing.md",
        "Market_Trends.md",
        "Market_Validation.md",
        "Market_Entry.md",
    ],
    "03_Competition": [
        "Competition_Competitor_Analysis.md",
        "Competition_Competitive_Positioning.md",
        "Competition_Pricing_Analysis.md",
        "Competition_Market_Gaps.md",
        "Competition_Moat_Analysis.md",
    ],
    "04_Customer": [
        "Customer_ICP.md",
        "Customer_Buyer_Personas.md",
        "Customer_Interviews.md",
        "Customer_Journey.md",
        "Customer_Willingness_To_Pay.md",
    ],
    "05_Product": [
        "Product_MVP.md",
        "Product_Feature_Prioritization.md",
        "Product_Roadmap.md",
        "Product_Product_Market_Fit.md",
        "Product_Product_Metrics.md",
    ],
    "06_GTM": [
        "GTM_Positioning.md",
        "GTM_Strategy.md",
        "GTM_Marketing.md",
        "GTM_Growth.md",
        "GTM_Launch.md",
    ],
    "07_Finance": [
        "Finance_Business_Model.md",
        "Finance_SaaS_Metrics.md",
        "Finance_Unit_Economics.md",
        "Finance_Financial_Model.md",
        "Finance_Pricing_Strategy.md",
    ],
    "08_RedTeam": [
        "RedTeam_Risk_Assessment.md",
        "RedTeam_Startup_Failure_Patterns.md",
        "RedTeam_Assumption_Testing.md",
        "RedTeam_Validation_Playbook.md",
        "RedTeam_Kill_Criteria.md",
    ],
    "09_Investor": [
        "Investor_VC_Due_Diligence.md",
        "Investor_Investment_Memo.md",
        "Investor_Defensibility.md",
        "Investor_Moat_Evaluation.md",
        "Investor_Funding_Readiness.md",
    ],
    "10_Templates": [
        "Report_Template.md",
        "Executive_Dashboard.md",
        "Template_Investment_Memo.md",
        "Template_Competitor_Matrix.md",
        "Template_Persona.md",
        "Template_Validation_Plan.md",
    ],
    "11_CaseStudies": [
        "CaseStudy_Airbnb.md",
        "CaseStudy_Stripe.md",
        "CaseStudy_Canva.md",
        "CaseStudy_Figma.md",
        "CaseStudy_Notion.md",
        "CaseStudy_Dropbox.md",
        "CaseStudy_Uber.md",
        "CaseStudy_Duolingo.md",
        "CaseStudy_Zoom.md",
        "CaseStudy_Shopify.md",
    ],
}

available = []
missing = []

print("=" * 70)
print("VENTURE BOARD KNOWLEDGE BASE ORGANIZER")
print("=" * 70)

for folder, files in FOLDERS.items():
    dest = ROOT / folder
    dest.mkdir(exist_ok=True)

    for filename in files:
        src = ROOT / filename
        dst = dest / filename

        if src.exists():
            shutil.move(str(src), str(dst))
            available.append(f"{folder}/{filename}")
            print(f"[OK] {filename} -> {folder}")
        elif dst.exists():
            available.append(f"{folder}/{filename}")
            print(f"[SKIP] Already exists: {folder}/{filename}")
        else:
            missing.append(f"{folder}/{filename}")
            print(f"[MISSING] {folder}/{filename}")

print("\n" + "=" * 70)
print(f"AVAILABLE : {len(available)}")
print(f"MISSING   : {len(missing)}")
print("=" * 70)

print("\nAVAILABLE FILES")
for f in available:
    print("  ✓", f)

print("\nMISSING FILES")
for f in missing:
    print("  ✗", f)

report = ROOT / "knowledgebase_audit_report.txt"
with report.open("w", encoding="utf-8") as fp:
    fp.write("VENTURE BOARD KNOWLEDGE BASE AUDIT\n")
    fp.write("=" * 60 + "\n\n")
    fp.write(f"Available: {len(available)}\n")
    fp.write(f"Missing: {len(missing)}\n\n")

    fp.write("AVAILABLE FILES\n")
    fp.write("-" * 40 + "\n")
    for f in available:
        fp.write(f + "\n")

    fp.write("\nMISSING FILES\n")
    fp.write("-" * 40 + "\n")
    for f in missing:
        fp.write(f + "\n")

print(f"\nAudit report saved to: {report}")
