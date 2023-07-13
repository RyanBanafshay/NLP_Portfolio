import pickle

class User:
    def __init__(self, name, likes, dislikes):
        self.name = name
        self.likes = likes
        self.dislikes = dislikes

user1 = User("john", ['singularity', 'galaxy', 'horizon'], ['gravastars', 'magnetic'])
user2 = User("kyle", ['shadow', 'magnetic'],['interstellar', 'wormhole'])
user3 = User("ryan", ['interstellar', 'wormhole'], ['singularity', 'galaxy'])

user_list = [user1, user2, user3]

pickle.dump(user_list, open('user_list.p', 'wb'))
