from github_api.client import github_client

user = github_client.get_user()

print("Connected to GitHub as:", user.login)