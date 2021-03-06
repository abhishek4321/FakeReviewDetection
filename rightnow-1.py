from BeautifulSoup import BeautifulSoup
import urllib2
import re
import json
import sys 
import time
import random
import pickle as pickle




text = re.compile('[0-9].*[a-z].*')
print __doc__
YELP_COM_URL = 'http://www.yelp.com'
dataset = 'data.pickle'
pos_count=0
neg_count=0
neut_count=0
print sys.stdout.encoding
page_iter = 0  
#page = urllib2.urlopen(url).read()
#print page
data_list = []
id=0
#print soup
def save_data(star_var,usefulvote_var,funnvote_var,coolvote_var,friendcount_var,reviewcount_var,wordcount_var,photocount_var,noofcheckin_var,review_var):
    global id
    
    data={
            
                'Ratings':star_var,
                'Usefulvote':usefulvote_var,
                'funnyvote': funnvote_var,
                'coolvote': coolvote_var,
                'No_of_checkin':noofcheckin_var,
                'Friendcount':friendcount_var,
                'Reviewcount':reviewcount_var,
                'No_of_Photos':photocount_var,
                'Review_length':wordcount_var,
                'Review ':review_var.decode('utf-8'),
                'Id':id
       
     }
    id=id+1
   
    global data_list
    
    data_list.append(data)
    
    #json.dump(data, f)
    
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

                save_data(star_var,usefulvote_var,funnvote_var,coolvote_var,friendcount_var,reviewcount_var,wordcount_var,photocount_var,noofcheckin_var,review_var)

get_yelp_page = \
    lambda zipcode, page_num: \
        'http://www.yelp.com/search?find_desc=&find_loc={0}' \
        '&ns=1#cflt=restaurants&start={1}'.format(zipcode, page_num)


def getSoupsForZip(zipcode, max_count=1):
    try:
        soups = []
        page_num = 0
        count = -1
        while True:
            page_url = get_yelp_page(zipcode, page_num)
            print page_url
            soup = BeautifulSoup(urllib2.urlopen(page_url).read())
            if soup:
                soups.append(soup)
            page_num = page_num + 11
            #print soup
            if count < 0:
                count = 11 * min(max_count, int(re.findall(r'\d+', str(soup.findAll('div', attrs={'class':re.compile(r'page-of-pages')})[0]))[1]))
            if count <= page_num:
                break
        return soups
    except Exception, e:
        print str(e)
        return None





def crawl_page(zipcode, verbose=False):
    global page_iter
    global pos_count,neg_count,neut_count
    soups = getSoupsForZip(zipcode)
    for zipPage in soups:
        for rl in zipPage.findAll('a', attrs={'class':re.compile('^biz-name')}):
            restaurantMainPage = YELP_COM_URL + re.findall('href=[\'"]?([^\'" >]+)', str(rl))[0]
            print restaurantMainPage + "***********" 
            print page_iter
            
            #crawl(restaurantMainPage)
            crawl_notrecommended(restaurantMainPage)
            #save_data(scraps.crawl_notrecommended(restaurantMainPage))         

            #return True
            page_iter=0
            pos_count=0
            neg_count=0
            neut_count=0

         
    return True        

def zip_crawl(zipcode=None):
    flag = True
    some_zipcodes = [zipcode] if zipcode else get_zips()
    if zipcode is None:
        print '\n**Attempting to extract all zipcodes in the U.S'
        
    for zipcode in some_zipcodes:
        #print '\n===== Attempting extraction for zipcode <', zipcode, '>=====\n'
        try:
            while flag:
                flag = crawl_page(zipcode)
                if not flag:
                    print 'Extraction stopped or broke at zipcode'
                else:
                    break
                time.sleep(random.randint(1, 2) * .931467298)
        except Exception, e:
                print zipcode, e
                time.sleep(random.randint(1, 4) * .931467298)            
         

if __name__ == '__main__':
   
    

    
    nyc_zip_code_start= zip_code = 10001
    nyc_zip_code_end = 10002

    while zip_code <= nyc_zip_code_end:
        try :
            zip_crawl(zip_code)
        except KeyboardInterrupt:
            with open('final.json','w') as f1:
                json.dump(data_list,f1)
            
            sys.exit()


              
                    
          
    


        
    with open(dataset,"a") as f:
        json.dump(data_list,f)    
    
