import gitlab
import requests
from urllib.parse import quote_plus, urljoin

from config import GITLAB_API_URL, GITLAB_APP_ID, GITLAB_SECRET, GITLAB_GOD_LOGIN, GITLAB_GOD_PASSWORD
#gl = gitlab.Gitlab(url=GITLAB_API_URL, oauth_token=GITLAB_SECRET)

def git_login_as_god():
    data = {'grant_type': 'password', 'username': GITLAB_GOD_LOGIN, 'password': GITLAB_GOD_PASSWORD}
    resp = requests.post(urljoin(GITLAB_API_URL, "oauth/token"), data=data)
    resp_data = resp.json()
    gitlab_oauth_token = resp_data["access_token"]
    gitlab_instance = git_get_instance(gitlab_oauth_token)
    return gitlab_instance

def git_login_as_user(username, password):
    data = {'grant_type': 'password', 'username': username, 'password': password}
    resp = requests.post(urljoin(GITLAB_API_URL, "oauth/token"), data=data)
    resp_data = resp.json()
    gitlab_oauth_token = resp_data["access_token"]
    gitlab_instance = git_get_instance(gitlab_oauth_token)
    return gitlab_instance

def git_get_instance(oauth_token):
    gitlab_instance = gitlab.Gitlab(url=GITLAB_API_URL, oauth_token=gitlab_oauth_token)
    gitlab_instance.auth()
    gitlab_instance.enable_debug()
    return gitlab_instance