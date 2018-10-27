import json
import codecs
from pos_tagging import *
import sys
review_block = []
input_file = file('sample1.txt','r').read().decode('utf-8')

f=json.loads(input_file)

for i in f:
     #print type(i)
     #print i['Review ']
     parts_of_speech(i['Review '])

   

