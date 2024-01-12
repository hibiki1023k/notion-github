import os
import requests
from notion_client import Client
from dotenv import load_dotenv

# GitHub APIのトークンを環境変数から取得
load_dotenv()
github_token = os.getenv('GITHUB_TOKEN')

headers = {
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'notion-github',
    'Authorization': f'token {github_token}'
}

def get_issues(repo):
    """ 指定されたリポジトリのGitHub Issuesを取得 """
    url = f'https://api.github.com/repos/{repo}/issues'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch issues: {response.status_code}')

def connect_notion(token_v2):
    """ Notion APIに接続 """
    client = Client(auth=token_v2)
    return client

# 例: 'username/reponame' 形式のリポジトリ名を指定
repository = 'hibiki1023k/notion-github'
try:
    issues = get_issues(repository)
    print(issues)
    # Notion APIのトークンを環境変数から取得
    token_v2 = os.getenv('NOTION_TOKEN')
    # Notion APIに接続
    notion_client = connect_notion(token_v2)
    print("Successfully connected to Notion API")
except Exception as e:
    print(f'Error: {e}')