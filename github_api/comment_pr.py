from github_api.client import github_client

def post_comment(repo_name, pr_number, comment):

    repo = github_client.get_repo(repo_name)

    pr = repo.get_pull(pr_number)

    pr.create_issue_comment(comment)

    print("Comment posted successfully!")