import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tensorflow.python.ops 
import random
import json
import string
import unicodedata
import sys
from tensorflow.contrib.rnn import static_bidirectional_rnn
import tflearn as tflearn
from slackclient import SlackClient
import re





# initialize the stemmer
stemmer = LancasterStemmer()
# variable to hold the Json data read from the file
data = None

# read the json file and load the training data
with open('data.json') as json_data:
    data = json.load(json_data)
    print(data)

# method to remove punctuations from sentences.
def remove_punctuation(text):
    return text.translate(data)


categories = list(data.keys())


words = []
# a list of tuples with words in the sentence and category name
docs = []

for each_category in data.keys():
    for each_sentence in data[each_category]:
        # remove any punctuation from the sentence
        each_sentence = remove_punctuation(each_sentence)
        print(each_sentence)
        # extract words from each sentence and append to the word list
        w = nltk.word_tokenize(each_sentence)
        print("tokenized words: ", w)
        words.extend(w)
        docs.append((w, each_category))

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))


training = []
output = []
output_empty = [0] * len(categories)


for doc in docs:
    bow = []
    token_words = doc[0]
    token_words = [stemmer.stem(word.lower()) for word in token_words]
    for w in words:
        bow.append(1) if w in token_words else bow.append(0)

    output_row = list(output_empty)
    output_row[categories.index(doc[1])] = 1

    # our training set will contain a the bag of words model and the output row that tells
    # which catefory that bow belongs to.
    training.append([bow, output_row])

# shuffle our features and turn into np.array as tensorflow  takes in numpy array
random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

print(train_x)

class mlmodel:
    net = tflearn.input_data(shape=[None, len(train_x[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(train_y[0]),activation='softmax')
    net = tflearn.regression(net)

    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
    model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
    model.save('model.tflearn')





def get_tf_record(sentence):
    global words
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    #one hot
    bow = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bow[i] = 1

    return(np.array(bow))


