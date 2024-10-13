# user_service.py
class UserService:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = {"email": email}

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("User does not exist")
        del self.users[username]

    def update_user(self, username, new_email=None):
        if username not in self.users:
            raise ValueError("User does not exist")
        if new_email:
            self.users[username]["email"] = new_email

    def check_court(self, username):
        return username.lower() == "john"  # Simple check, could be replaced with actual logic

