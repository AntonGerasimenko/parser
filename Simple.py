import urllib
from bs4 import BeautifulSoup
from DB import data_base as DB
import os

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
            'title': rows.h1.a["title"][7:],
            'date': rows.h1.a["title"][:6],
            'id': int (rows["id"][5:])
        })

    return list

def print_result(list):
     for entry in list:

        title = entry['title']
        date = entry['date']
        text = entry['text']
        image = entry['image']
        id = entry['id']

        print id
        print title
        print date
        print text
        print image

def main():

    html = get_html("http://www.graffiti.by/")
    events_list = parse(html)

    path = os.path.dirname(os.path.abspath(__file__)) + '\\events.db'

    DB.write(events_list,path)
    print_result(events_list)

if __name__ == '__main__':
        main()