import gitlab
from auth import git_login_as_user, git_login_as_god

class GitUser:
    def __init__(self, username, password):
      self.gl = git_login_as_user(username, password)

    @staticmethod
    def generate_password():
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(0,10))
    @staticmethod
    def create(email, username, name):
        gl = git_login_as_god()
        password = generate_password()
        git_user = gl.users.create({'email': email,
                                    'password': password,
                                    'username': username,
                                    'name': username})
        return GitUser(username, password)