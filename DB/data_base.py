import _sqlite3

def write(events_list, DBname):

    conn = _sqlite3.connect(DBname)
    conn.execute('''CREATE TABLE IF NOT EXISTS EVENTS
       (ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
       ID_EVENT INTEGER NOT NULL,
       TITLE           TEXT    NOT NULL,
       _TEXT            TEXT     NOT NULL,
       IMAGE        TEXT NOT NULL );''')
    print "Table created successfully"

    for event in events_list:

        id_event = str(event['id'])
        title = "'" + event['title'] +"'"
        _text = "'" + event['text'] +"'"
        image = "'" + event['image'] +"'"

        string = "INSERT INTO EVENTS (ID_EVENT,TITLE,_TEXT,IMAGE) VALUES ("+id_event+","+title+","+_text+","+image+")"
        conn.execute(string)

    conn.commit()
    print "Records created successfully"
    conn.close()

def read(DBname):

     conn = _sqlite3.connect(DBname)
     cursor = conn.cursor()
     cursor.execute("SELECT DISTINCT ID_EVENT, TITLE, _TEXT, IMAGE FROM EVENTS")

     one_row ={}
     result = list()

     for row in cursor:
         one_row["id"] = row[0]
         one_row["title"] = row[1]
         one_row["text"] = row[2]
         one_row["image"] = row[3]
         result.append(dict(one_row))

     conn.close()
     return result