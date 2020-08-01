import requests
from bs4 import BeautifulSoup
import csv
from random import randint
 
r = requests.get('https://www.yelp.com/biz/bar-karaoke-lounge-toronto')
soup = BeautifulSoup(r.content , features = 'lxml')
#print(soup)

#creating csv file to store data
csv_file = open('yelp_feedback.csv', 'w')
csv_writer = csv.writer(csv_file)
headerofcsv= ['User','Date','City','Rating','Review']
#headerofcsv= ['Rating']
csv_writer.writerow(headerofcsv)


#getting total number of reviews from bar-karaoke-lounge-toronto
url_for_pages = soup.find('div' , class_ = 'lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU nowrap__373c0__35McF').p.text
total_reveiw= (url_for_pages.split( )[0]) 
total_reveiw= int(total_reveiw)

#getting url list of each pages.
url_page_list=[]
#(0,105,20): here 20 is step size, because each page contain 20 reviews only
for i in range(0,total_reveiw,20): 
    url_page_list.append('https://www.yelp.com/biz/bar-karaoke-lounge-toronto?start='+str(i))
#print(url_page_list)    

def eachpage_scrape(feedbacks, csv_writer):
    reviewList= []  
    for feedback in feedbacks:
        rev = {
            'user' : feedback.find('span', class_ = 'lemon--span__373c0__3997G text__373c0__2Kxyz fs-block text-color--blue-dark__373c0__1jX7S text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz').get_text('a'),
            'date' : feedback.find('span', class_ = 'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-').text,
            'city' : feedback.find('div', class_ ='lemon--div__373c0__1mboc responsive-hidden-small__373c0__2vDff border-color--default__373c0__3-ifU').get_text('span'),
            'rating': feedback.find('span',  class_ = 'lemon--span__373c0__3997G display--inline__373c0__3JqBP border-color--default__373c0__3-ifU').div['aria-label'].split( )[0],
            'review' : feedback.find('p', class_ = 'lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-').get_text('span')
        }  
        reviewList.append(rev)
        
        #loading above loop of each review to csv according to it's data type(i.e. dict)
        csv_writer.writerow([rev['user'], rev['date'],rev['city'], rev['rating'], rev['review']])
        #csv_writer.writerow([rev['rating']])
        csv_file.close 

    #printing entire 105 review list   
    print(reviewList)    

#for loop to cover all revies from each page.
for index, url in enumerate(url_page_list):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        
        #Here, 'feedbacks' is the main gateway line, which contain other code to fetch their date, user, city and review 
        feedbacks = soup.find_all('div', class_ = 'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU')
        
        #calling scrapping function
        eachpage_scrape(feedbacks, csv_writer)
        print('Completed page :'+str(index+1))

#feedbacks = soup.find_all('div', class_ = 'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU')  
#reviewList= []
#for feedback in feedbacks:  
    #rating = feedback.find('span',  class_ = 'lemon--span__373c0__3997G display--inline__373c0__3JqBP border-color--default__373c0__3-ifU').div['aria-label'].split( )[0]
    #reviewList.append(rating)
#print(reviewList)  