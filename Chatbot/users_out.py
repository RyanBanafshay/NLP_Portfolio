import pickle

class User:
    def __init__(self, name):
        self.name = name
        self.likes = []
        self.dislikes = []

user_list = pickle.load(open('user_list.p', 'rb'))

for user in user_list:
    print('User name: ', user.name)
    print('Likes: ', user.likes)
    print('Dislikes: ', user.dislikes)
    print('----------------------')
