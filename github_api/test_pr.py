from github_api.fetch_pr import get_pr

pr = get_pr(
    "manikandanmcodes-dev/reviewflow-ai",
    1
)

print(pr)