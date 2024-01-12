import requests
import os

from dotenv import load_dotenv

# 環境変数からGitHubトークンを取得
load_dotenv()
github_token = os.getenv('GITHUB_TOKEN')

# GitHub APIヘッダーにトークンを設定
headers = {
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

# 例: 'username/reponame' 形式のリポジトリ名を指定
repository = 'hibiki1023k/notion-github'
try:
    issues = get_issues(repository)
    print(issues)

    # Issuesのデータを表示（例）
    for issue in issues:
        print(f'Issue Title: {issue["title"]}, Number: {issue["number"]}')
except Exception as e:
    print(f'Error: {e}')
