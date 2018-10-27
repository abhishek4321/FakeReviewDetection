import nltk
from nltk.corpus import state_union
import collections
from nltk.tokenize import PunktSentenceTokenizer
import sys
train_text = state_union.raw("2005-GWBush.txt")#train text
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#training of nltk corpus


#sample_text = open('sample1.txt','r').read()

#print sample_text

def parts_of_speech(review):
    tokenized = custom_sent_tokenizer.tokenize(review)
    for i in tokenized:
        words = nltk.word_tokenize(i)
        #print words
        #print '//////'
        pos = nltk.pos_tag(words)
        return pos



#for i in sample_text:
#parts_of_speech(sample_text)