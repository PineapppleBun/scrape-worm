import requests, bs4, lxml, time

#Function to seperate content div and extract and print text for individual page

def get_page(link):
    request = requests.get(link)
    page_html = bs4.BeautifulSoup(request.content, 'lxml')
    page_header = page_html.find('h1', attrs = {'class': 'entry-title'})
    print(page_header.get_text(),"\n")
    page_content = page_html.find('div', attrs = {'class': 'entry-content'})
    for paragraph in page_content.find_all('p'):
        if paragraph.a == None:
            print(paragraph.get_text(),"\n")

url = "https://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/"

links = []

get_page(url)
