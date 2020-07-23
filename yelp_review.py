import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.yelp.com/biz/bar-karaoke-lounge-toronto'
r = requests.get(url)
soup = BeautifulSoup(r.content , features = 'lxml')
#print(soup)


#divs1 = soup.find_all('div', class_ = 'lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT arrange-unit-grid-column--8__373c0__2dUx_ padding-r6__373c0__2Qlev border-color--default__373c0__3-ifU')
#reviewList1= []  
#for div1 in divs1:
        #rev1 = {
            #'name' : div1.find('span', class_ = 'lemon--span__373c0__3997G text__373c0__2Kxyz fs-block text-color--blue-dark__373c0__1jX7S text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz').a.text,
            #'city' : div1.find('div', class_ = 'lemon--div__373c0__1mboc responsive-hidden-small__373c0__2vDff border-color--default__373c0__3-ifU').span.text,
            #'review' : div1.find('p', class_ ='lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-').span.text,
        #}
        #reviewList1.append(rev1,'*')
#print(reviewList1)

csv_file = open('yelp_feedback.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['User','Date','City','review'])


feedbacks = soup.find_all('div', class_ = 'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU')
                                     #lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT arrange-unit-fill__373c0__3Sfw1 border-color--default__373c0__3-ifU
                                     #lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU  
reviewList= []  
for feedback in feedbacks:
    rev = {
        'user' : feedback.find('span', class_ = 'lemon--span__373c0__3997G text__373c0__2Kxyz fs-block text-color--blue-dark__373c0__1jX7S text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz').get_text('a'),
        'date' : feedback.find('span', class_ = 'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-').text,
        'city' : feedback.find('div', class_ ='lemon--div__373c0__1mboc responsive-hidden-small__373c0__2vDff border-color--default__373c0__3-ifU').get_text('span'),
        #'rating': feedback.find('div', class_ = 'lemon--div__373c0__1mboc i-stars__373c0__1T6rz i-stars--regular-5__373c0__N5JxY border-color--default__373c0__3-ifU overflow--hidden__373c0__2y4YK').get_text('aria-label'),
        'review' : feedback.find('p', class_ = 'lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-').get_text('span')
    }
    
    

    reviewList.append(rev)
    csv_writer.writerow([rev['user'], rev['date'],rev['city'], rev['review']])

csv_file.close    
print(reviewList)

