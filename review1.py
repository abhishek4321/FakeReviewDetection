from BeautifulSoup import BeautifulSoup
import urllib2
import re
import json
import codecs
import io
import sys 
import time
import random
YELP_COM_URL = 'http://www.yelp.com'

print sys.stdout.encoding
page_iter = 0  
x = 0
#page = urllib2.urlopen(url).read()
#print page
data_list = []
#print soup
def save_data(review_var):
    global x
    x+=1
    data={
            
                'review':review_var
                
                
        
       
     }
    global data_list
  

    data_list.append(data)
    with open('data.json', 'a') as f:
        f.write(review_var + "\n")
      

    if x > 50:
         
         sys.exit()
def crawl(url):
    global pos_count,neg_count,neut_count
    #url="https://www.yelp.com/biz/nopa-san-francisco"

    page = urllib2.urlopen(url).read()
    #page = open("nopaYelp.html","r").read() 

    soup = BeautifulSoup(page)
    r = re.compile('[0-9]\.[0-9]') 
    r1 = re.compile('[0-9]*')
    r3 = re.compile('[0-9].*')
    r4 = re.compile('f [0-9].*')

    for pageno in soup.findAll("div",{"class":"page-of-pages arrange_unit arrange_unit--fill"}):
        print pageno.text
        l=pageno.text
        s = r4.search(l)
        s = r3.search(s.group())
        no_of_pages=s.group()
        
        #print "*************"
        
    
    s1 = soup.findAll("div",{"class":"review review--with-sidebar"})
    
    for i  in s1:
        
        star_var=0
        usefulvote_var=0
        funnvote_var=0
        coolvote_var=0
        wordcount_var=0
        friendcount_var=0
        noofcheckin_var=0
        reviewcount_var=0
        photocount_var=0
        
        
        
            
     
        for reviewduration in i.findAll("p"):
            review =  reviewduration.text.encode(sys.stdout.encoding, errors='replace') 
            review_var=review
            print review 
            #print "//////////////////////////////////////"
            count = 0 
            break  

        

        save_data(review)         
        
        print star_var
        print "******************************" 
    for nextpage in soup.findAll("a",{ "class":"u-decoration-none next pagination-links_anchor"}):
        nextUrl= nextpage['href']
    global page_iter 
    page_iter+=1
    if page_iter < 3 :    #no_of_pages:
        print nextUrl
        crawl(nextUrl)

  


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
            crawl(restaurantMainPage)
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
    #parser = argparse.ArgumentParser(description='Extracts all yelp restaurant \
      #  data from a specified zip code (or all American zip codes if nothing \
       # is provided)')
    #parser.add_argument('-z', '--zipcode', type=int, help='Enter a zip code \
     #   you\'t like to extract from.')
    #args = parser.parse_args()
                     
    

    
    nyc_zip_code_start= zip_code = 10001
    nyc_zip_code_end = 10002

    while zip_code <= nyc_zip_code_end:
        try :
            zip_crawl(zip_code)
        except KeyboardInterrupt:
            with codecs.open("data.json",encoding='utf-8') as f:
                json.dump(data_list,f)   
                print json.load(f).read() 
    


        
    with open("data.json","a") as f:
        json.dump(data_list,f)    
    