import requests, bs4, lxml, time

url = "https://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/"

#Function to extract page content and grab link for next chapter
def get_page(link):
    request = requests.get(link)
    page_html = bs4.BeautifulSoup(request.content, 'lxml')
    page_header = page_html.find('h1', attrs = {'class': 'entry-title'})
    print(page_header.get_text(),"\n")
    page_content = page_html.find('div', attrs = {'class': 'entry-content'})
    for paragraph in page_content.find_all('p'):
        if paragraph.a == None:
            print(paragraph.get_text(),"\n")
    page_link = page_html.find('a', attrs = {'title': 'Next Chapter'})
    url = page_link.get('href')
    print(url)

for i in range(0,2):
	get_page(url)

