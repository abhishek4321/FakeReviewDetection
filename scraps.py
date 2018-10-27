from BeautifulSoup import BeautifulSoup
import urllib2
import re
import json
import sys 
import time
import random
data_list = []



def crawl_notrecommended(url):
    pos_count=0
    neg_count=0
    neut_count=0
    r = re.compile('[0-9]\.[0-9]') 
    r1 = re.compile('[0-9]*')
    
    
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    for not_recommended in soup.findAll('div',attrs={'class':'not-recommended ysection'}):
        print "*****************************"
        #print not_recommended
        for h in not_recommended.findAll('a',attrs={'class':'subtle-text inline-block js-expander-link'}):
            not_recomendpage =  'http://www.yelp.com' +  h['href']
            #print h['href']
            print not_recomendpage + "       for non recommended"
            soup_notrec =  BeautifulSoup(urllib2.urlopen(not_recomendpage).read())
            #print soupnotrec
            for j in soup_notrec.findAll('div',attrs={'class' : 'review review--with-sidebar'}):
                star_var=0
                usefulvote_var=0
                funnvote_var=0
                coolvote_var=0
                wordcount_var=0
                friendcount_var=0
                noofcheckin_var=0
                reviewcount_var=0
                photocount_var=0
        
                #print j
                for image in j.findAll("img",{"class":"offscreen"}):
                    star = image.get('alt','')
                    star = r.search(star).group()
                    #print(type(star))
                    print 'no of stars ' + r.search(star).group()
                    #float(u'star'.encode('ascii'))
                    star_var=star.encode('utf-8')
                    star_var = float(star_var)
            
                    if star_var >=4:
                            print "Positive"
                            pos_count+=1
                    if star_var <=2 :
                            print "Negative"
                            neg_count+=1
                    if star_var >2 and star_var<4:
                            print "Neutral"
                            neut_count+=1
                    #print    type(star_var)

                    break
                '''
                usefulvote = j.findAll("span",{"class":"count"})
                #print usefulvote.
                usefulvote_var=usefulvote[0].text
                funnvote_var=usefulvote[1].text
                coolvote_var=usefulvote[2].text
                #print 'useful votes ' + usefulvote[0].text
                #print 'funny votes  ' + usefulvote[1].text
                #print 'cool votes ' + usefulvote[2].text
                
                '''
                
                
                
                for k in j.findAll(("ul",{"class":"user-passport-stats"})):
                    friendcount = k.findAll("li",{"class":"friend-count responsive-small-display-inline-block" }) 
                    for  b in friendcount:
                        x =  b.findAll("b")
                        for x1 in x:
                            print 'freindcount ' +  x1.text 
                            friendcount_var=x1.text
                    reviewcount = k.findAll("li",{"class":"review-count responsive-small-display-inline-block" }) 
                    for  b in reviewcount:
                        x =  b.findAll("b")
                        for x1 in x:
                            print 'NoOfReviews '+ x1.text
                            reviewcount_var=x1.text
                    photocount = k.findAll("li",{"class":"photo-count responsive-small-display-inline-block" })
                    print photocount 
                    for  b in photocount:
                        x =  b.findAll("b")
                        print x 
                        for x1 in x:
                            
                            print 'NoOfPhotos '+x1.text
                            photocount_var=x1.text        
                for noofcheckin in j.findAll("li",{"class":"review-tags_item"}):

                    print 'NoOfCheckins '+ r1.search(noofcheckin.text).group()
                    noofcheckin_var=r1.search(noofcheckin.text).group()

                
                

                for reviewduration in j.findAll("p"):
                    review =  reviewduration.text.encode('ascii', 'ignore').decode('ascii') 
                    review_var=review
                    print review
                    words = []
                    count = 0
                    for word in review.split():
                        count+=1
                        #print  'WORDCOUNT'+ count
                        wordcount_var=count
                        #print review 
                        #print "//////////////////////////////////////"
                        count = 0 
                    break  
    return star_var,usefulvote_var,funnvote_var,coolvote_var,friendcount_var,reviewcount_var,wordcount_var,photocount_var,noofcheckin_var,review_var
                    










