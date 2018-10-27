import nltk
import codecs
from nltk.corpus import state_union
import collections
import sys
from nltk.tokenize import PunktSentenceTokenizer
train_text = state_union.raw("2005-GWBush.txt")#training text

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#training of data

sample_text = open('data.json','r').read()
sample_text = unicode(sample_text,errors='ignore')
    
#print sample_text


def parts_of_speech(i):

        print "******************************"
        tokenized = custom_sent_tokenizer.tokenize(i)
        l=[]
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                #print(tagged)
                for _,j in tagged:
                    l.append(j)
                

        except Exception as e:
            print(str(e))
      
        c= collections.Counter(l)
        print c

for i in sample_text.split('\n'):
    parts_of_speech(i)

'''
print len(x)
l = []
for _,i in x:
    print i
    l.append(i)


c = collections.Counter(l)

print c'''