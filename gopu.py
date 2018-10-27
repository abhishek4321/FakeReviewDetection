import nltk
from nltk.corpus import state_union
import collections
from nltk.tokenize import PunktSentenceTokenizer
import sys
train_text = state_union.raw("2005-GWBush.txt")#train text
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#training of nltk corpus


sample_text = open('sample1.txt','r').read()

def parts_of_speech(review)
    tokenized = custom_sent_tokenizer.tokenize(review)
    for i in tokenized:
        words = nltk.word_tokenize(i)
        print words
        print '//////'
        pos = nltk.pos_tag(words)
        print pos


    def process_content():
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                print(tagged)

        except Exception as e:
            print(str(e))


#process_content()

    str1 = 'Apoorv is chutiya.'
tokenized = custom_sent_tokenizer.tokenize(str1)
for i in tokenized:
    words = nltk.word_tokenize(i)
    print words
    print '//////'
    pos = nltk.pos_tag(words)
    print pos



print '*********'
x = nltk.pos_tag(str1)

print len(x)
l = []
for _,i in x:
    print i
    l.append(i)


c = collections.Counter(l)

print c
for i in sample_text:
    parts_of_speech (i)