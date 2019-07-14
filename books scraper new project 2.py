import requests
from bs4 import BeautifulSoup
import csv
f = csv.writer(open('booksname.csv', 'w'))
f.writerow(['Title', 'Author'])
pages=[]
for i in range(1,2):
    url='https://thegreatestbooks.org/?page='+str(i)
    pages.append(url)

print(pages)
tit=[]
auth=[]
#for loop for 100 pages

for urls in pages:
        
    page=requests.get(urls)
    soup=BeautifulSoup(page.text,'html.parser')
    #last_link=soup.find(class_='tab')
    #last_link.decompose()
    book=soup.find(class_='list-unstyled')
    book_a=book.find_all('a')
##    for i in range(len(book_a)):
##        print(i)
##        print(book_a[i])
    k=""

    
    for i in range(0,len(book_a),4):
        b=str(book_a[i]).partition('>')[2]
        for m in range(len(b)):
                if b[m]=='<':
                    break
                k=k+b[m]
        print(k)
        tit.append(k)
        k=""

        
    p=""  
    for y in range(1,len(book_a),4):
        a=str(book_a[y]).partition('>')[2]
        for v in range(len(a)):
            if a[v]=='<':
                break
            p=p+a[v]
        print(p)
        auth.append(p)
        p=""
for (Title,Author) in zip(tit,auth):
    f.writerow([Title,Author])
f = csv.writer(open('bo.csv', 'w'))
f.writerow([Title,Author])


