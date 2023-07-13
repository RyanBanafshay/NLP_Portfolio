import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import numpy
import random
import json
import pickle
import sklearn

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
stopwords = stopwords - set(['no', 'not', 'can', 'are'])

with open('../intents.json') as json_data:
    intents = json.load(json_data)

words = [] #holds all words derived from patterns (lemmatized)
classes = []
documents = [] #corpus of words under specific intents
ignore_punct = ['?', '.', '!']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        #print(f"working on intent '{intent['tag']}'")
        pattern_words = word_tokenize(pattern)

        words.extend(pattern_words)

        documents.append((pattern_words, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#stem and lowercase each word
stemmer = LancasterStemmer()
words = [stemmer.stem(pattern_words.lower()) for pattern_words in words if pattern_words not in ignore_punct and pattern_words not in stopwords]

#remove duplicates
words = sorted(set(words))
classes = sorted(set(classes))

#print(f'number of documents {len(documents)}')
#print(f'number of classes {len(classes)} ', classes)
#print(f'unique lemmas {len(words)}', words)

training = []
training_out = []

empty_arr = [0] * len(classes)

for document in documents:

    bag_of_words = []
    pattern_words = document[0]

    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words if word not in list(stopwords)]

    for word in words:
        if word in pattern_words:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)

    output_row = list(empty_arr)
    output_row[classes.index(document[1])] = 1

    training.append([bag_of_words, output_row])


#shuffle
random.shuffle(training)
training = numpy.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

neural = MLPClassifier(hidden_layer_sizes=(10,8), max_iter=10000)
neural.fit(train_x, train_y)

pickle.dump(neural,open('sklearn_neural_model', 'wb'))

pickle.dump({'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open("training_data", "wb"))

#----
def clean_sentence(sent):
    sent_words = word_tokenize(sent)

    stemmer = LancasterStemmer()
    sent_words = [stemmer.stem(word.lower()) for word in sent_words if word.isalpha() and word not in stopwords]

    return sent_words

#clean sentence, mark which words are present in the input
def bag_of_words(sent, words):
    sent_words = clean_sentence(sent)
    bag = [0] * len(words)
    for s in sent_words:
        for i,word in enumerate(words):
            if word == s:
                bag[i] = 1

    return(numpy.array(bag))

#predict the intent using a bag of words, return a descending list of probable responses
def classify(sent):
    print(f'sent: {sent}')
    err_margin = 0.25

    model_results = neural.predict_proba([bag_of_words(sent,words)])[0]
    model_results = [[i,r] for i,r in enumerate(model_results) if r > err_margin]

    model_results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for result in model_results:
        return_list.append((classes[result[0]], result[1]))
    print(f'return list: {return_list}')
    return return_list

debug = True
if (debug):
    classify('thanks')
    classify('uh')
    classify('what')
    classify('teach me')
    classify('hi')
    classify('what is your name')
    classify('tell me more about galaxies')
    classify('what are you')
    classify('goodbye')
    classify('yes')
    classify('sure')
    classify('what can i learn')

    while True:
        user_in = input('>>')
        classify(user_in)
