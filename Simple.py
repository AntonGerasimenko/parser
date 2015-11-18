import urllib
from bs4 import BeautifulSoup
def get_html(url):

    response = urllib.urlopen(url)
    return response.read()

def parse(html):

    soup = BeautifulSoup(html)
    table = soup.find('div',id='content')

    titles = []

    for rows in table.find_all('div','post'):

        titles.append({

            'image': rows.find('img').src
        })

    for title in titles: print(title)


def main():

   html = get_html("http://www.graffiti.by/")
   parse(html)


if __name__ == '__main__':
        main()





