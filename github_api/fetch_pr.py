from github_api.client import github_client

def get_pr(repo_name, pr_number):

    repo = github_client.get_repo(repo_name)

    pr = repo.get_pull(pr_number)

    files = []

    for file in pr.get_files():

        files.append({
            "filename": file.filename,
            "status": file.status,
            "additions": file.additions,
            "deletions": file.deletions,
            "patch": file.patch
        })

    return {
        "title": pr.title,
        "number": pr.number,
        "author": pr.user.login,
        "state": pr.state,
        "files": files
    }