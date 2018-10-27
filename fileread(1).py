import json
from collections import Counter
from pos_tagging import * 
f=open ('final.json') 
data=json.load(f)
for i in data:
    cnt=Counter()
    print "***********************"
    #print i["Review "]
    r =  parts_of_speech(i["Review "])
    l= []
    #print r
    for j in r :
        l.append(j[1])
    for j in l:
        cnt [j]+=1
    print cnt       
    i["POS"]=cnt
#parts_of_speech('review')
with open('POS.json',"a") as f:
        json.dump(data,f) 
    



 