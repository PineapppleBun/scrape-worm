import requests, bs4, lxml, time

#Function to seperate content div and extract and print text for individual page

def get_text(link):
    page = requests.get(link)
    doc = bs4.BeautifulSoup(page.content, 'lxml')
    divc = doc.find('div', attrs = {'class': 'entry-content'})
    for p in divc.find_all('p'):
        print(p.get_text(),"\n")

url = "https://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/"

links = []

get_text(url)
