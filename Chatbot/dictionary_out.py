import pickle

file = 'knowledge_base.p'
dict = pickle.load(open('knowledge_base.p', 'rb'))

for key in dict.keys():
    print('Term: ', key)
    print(dict[key])
    print('-----------------------')
