import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

github_client = Github(github_token)