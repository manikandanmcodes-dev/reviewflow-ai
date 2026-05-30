from fastapi import APIRouter
from github_api.fetch_pr import get_pr
from diff_processing.parser import process_files
from risk_analysis.analyzer import analyze_risks

router = APIRouter()

@router.post("/github")
async def github_webhook(payload: dict):

    pr_number = payload["pull_request"]["number"]

    pr_data = get_pr(
        "manikandanmcodes-dev/reviewflow-ai",
        pr_number
    )

    processed_files = process_files(pr_data["files"])

    risks = analyze_risks(pr_data["files"])

    return {
        "success": True,
        "pr": pr_data,
        "processed_files": processed_files,
        "risks": risks
    }