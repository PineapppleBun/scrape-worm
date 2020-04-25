import requests, bs4, lxml

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

for link in divc.find_all('a'): 
    print(link.get('href')) 
    links.append(link.get('href'))

for link in links:
    get_text(link)
