class ChatUser:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.inbox = []

    def send(self, receiver, message):
        receiver.inbox.append(f"{self.name}: {message}")

    def show_inbox(self):
        return "\n".join(self.inbox)


class ChatSystem:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, name):
        for u in self.users:
            if u.name == name:
                return u
        return None
