import urllib
from bs4 import BeautifulSoup
def get_html(url):

    response = urllib.urlopen(url)
    return response.read()

def parse(html):

    soup = BeautifulSoup(html)
    table = soup.find('div',id='content')

    list = []

    for rows in table.find_all('div','post'):

        list.append({
            'text': rows.p.text,
            'image': rows.img["src"],
            'title': rows.h1.a["title"]
        })

    return list

def print_result(list):
     for entry in list:

        data = entry['title']
        titl = entry['text']
        title = entry['image']

        print(titl)
        print(title)
        print(data)

def main():

   html = get_html("http://www.graffiti.by/")
   list = parse(html)
   print_result(list)

if __name__ == '__main__':
        main()