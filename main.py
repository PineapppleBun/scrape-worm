import requests, bs4, lxml

#Function to seperate content div and extract text

def get_text(link):
    page = requests.get(link)
    doc = bs4.BeautifulSoup(page.content, 'html')
    divc = doc.find('div', attrs = {'class': 'entry-content'})
    for p in divc.find_all('p'):
        print(p.get_text(),"\n")

url = "https://parahumans.wordpress.com/table-of-contents/"
page = requests.get(url)
doc = bs4.BeautifulSoup(page.content, 'html')
divc = doc.find('div', attrs = {'class': 'entry-content'})
links = []


#Loop through ToC, grab links and add to array

for link in divc.find_all('a'):  
    links.append(link.get('href'))

#Loop through array and extract text

for link in links:
    get_text(link)
