import gitlab

class GitLabGlobal:

    def __init__(self):
        self.gl = gitlab.Gitlab(url=GITLAB_API_URL, private_token=GITLAB_SECRET)