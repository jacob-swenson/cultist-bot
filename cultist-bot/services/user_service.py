import json

users = []


class User:
    node = None
    data = {}

    def __init__(self, uid, data=None, node=None):
        if data is None:
            data = {}
        self.data = data
        self.uid = uid
        self.node = node

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node
        persist_users()

    def get_data(self, key):
        if key not in self.data:
            return None
        return self.data[key]

    def set_data(self, key, value):
        self.data[key] = value
        persist_users()


def get_user(uid):
    user = None

    for stored_user in users:
        if stored_user.uid == uid:
            user = stored_user

    if user is None:
        user = User(uid)
        users.append(user)
        persist_users()

    return user


def persist_users():
    out_data = {}
    for user in users:
        out_data[user.uid] = {}
        out_data[user.uid]['data'] = user.data
        out_data[user.uid]['node'] = user.node
    with open('data/users/user-data.json', 'w') as out_file:
        json.dump(out_data, out_file)


def load_users():
    with open('data/users/user-data.json', 'r') as in_file:
        in_data = json.load(in_file)
        for user in in_data:
            print(user)
            print(in_data[user])
            data = in_data[user]['data']
            node = in_data[user]['node']
            users.append(User(user, data, node))


load_users()
