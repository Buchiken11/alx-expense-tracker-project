from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        return users.get(user_id)

    @staticmethod
    def get_or_create(user_info):
        user_id = user_info['sub']
        if user_id in users:
            return users[user_id]
        else:
            user = User(user_id, user_info['name'], user_info['email'])
            users[user_id] = user
            return user

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

# In-memoryuser store
users = {}
