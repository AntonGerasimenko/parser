import urllib
from bs4 import BeautifulSoup
import _sqlite3

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
            'title': rows.h1.a["title"],
            'id': rows["id"]
        })

    return list

def print_result(list):
     for entry in list:

        title = entry['title']
        text = entry['text']
        image = entry['image']
        id = entry['id']

        print(title)
        print(text)
        print(image)
        print(id)



def db(events_list):

    conn = _sqlite3.connect('events.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS EVENTS
       (ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
       TITLE           TEXT    NOT NULL,
       _TEXT            TEXT     NOT NULL,
       IMAGE        TEXT NOT NULL );''')
    print "Table created successfully"

    for event in events_list:

        title = "'" + event['title'] +"'"
        _text = "'" + event['text'] +"'"
        image = "'" + event['image'] +"'"

        string = "INSERT INTO EVENTS (TITLE,_TEXT,IMAGE) VALUES ("+title+","+_text+","+image+")"
        conn.execute(string)

    conn.commit()
    print "Records created successfully"
    conn.close()

def main():

   html = get_html("http://www.graffiti.by/")
   events_list = parse(html)
   #db(events_list)

   print_result(events_list)

if __name__ == '__main__':
        main()