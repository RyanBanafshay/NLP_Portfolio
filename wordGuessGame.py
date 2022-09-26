import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import collections
import random


#return total tokens as well as total nouns in data file
def preProcessText():
    file_content = open("anat19.txt").read()
    tokens = nltk.word_tokenize(file_content)
    setU = set(tokens)
    print("\nLexical diversity: %.2f" % (len(setU) / len(tokens)))

    lowerTokens = nltk.word_tokenize(file_content)
    lowerTokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]
    lowerTokens = [t.lower() for t in lowerTokens]

    wnl = WordNetLemmatizer()
    lowerTokensLemmas = [wnl.lemmatize(t) for t in lowerTokens]
    lowerTokens_unique = list(set(lowerTokensLemmas))

    tags = nltk.pos_tag(lowerTokens_unique)
    print(tags[:20])
    nouns = [a for (a, b) in tags if b[1] == 'N']

    print("The number of total tokens is " + (str(len(lowerTokens))))
    print("The number of noun tokens is " + (str(len(nouns))))

    return lowerTokens, nouns

def main():
    tokens, nouns = preProcessText()
    my_dictionary = {}

    for x in nouns:
        count = 1
        for y in tokens:
            if (x == y):
                count += 1
        my_dictionary[x] = count

    #put top 50 nouns into a list
    cnt = collections.Counter(my_dictionary)
    list1 = []
    for k, v in cnt.most_common(50):
        list1.append(k)

    #guessing game
    score = 5
    win = True
    while score > -1:
        print("Your score is ", score)
        if (win == True):
            word = random.choice(list1)
            totalGuess = ""
            print(word)
            win = False
        guess = input("Enter a letter to guess or ! to quit: ")
        if guess not in word:
            print("Letter not in word. Guess again.")
            score -= 1
        if guess == "!":
            break
        if guess in word:
            score += 1
            check = 0
            totalGuess += guess
            for char in word:
                if char in totalGuess:
                    print(char)
                    check += 1
                else:
                    print("_")
            if check == len(word):
                print("You Win! Your score is ", score)
                con = input("Play again? Y for yes and N for no: ")
                if con == "N" or "n":
                    win = False
                    break





if __name__ == "__main__":
    main()