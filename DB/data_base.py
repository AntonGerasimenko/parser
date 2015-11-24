import _sqlite3

def write(events_list, DBname):

    conn = _sqlite3.connect(DBname)
    conn.execute('''CREATE TABLE IF NOT EXISTS EVENTS
       (ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
       ID_EVENT INTEGER NOT NULL,
       DATE_EVENT            TEXT    NOT NULL,
       TITLE           TEXT    NOT NULL,
       _TEXT            TEXT     NOT NULL,
       IMAGE        TEXT NOT NULL );''')
    print "Table created successfully"

    for event in events_list:

        id_event = str(event['id'])
        date  = "'" + event['date']  +"'"
        title = "'" + event['title'] +"'"
        _text = "'" + event['text']  +"'"
        image = "'" + event['image'] +"'"

        string = "INSERT INTO EVENTS (ID_EVENT,DATE_EVENT,TITLE,_TEXT,IMAGE) VALUES ("+id_event+","+date+","+title+","+_text+","+image+")"
        conn.execute(string)

    conn.commit()
    print "Records created successfully"
    conn.close()

def read(DBname, except_ids=None):

    resp_str = "SELECT DISTINCT ID_EVENT, DATE_EVENT , TITLE, _TEXT, IMAGE FROM EVENTS"
    if except_ids!=None:
        resp_str += " WHERE "
        for id in except_ids:
            resp_str += " ID_EVENT != "+ str(id) + " AND "
        resp_str = resp_str[:-4]

    print resp_str
    conn = _sqlite3.connect(DBname)
    cursor = conn.cursor()
    cursor.execute(resp_str)

    one_row ={}
    result = list()

    for row in cursor:
        one_row["id"] = row[0]
        one_row["date"] = row[1]
        one_row["title"] = row[2]
        one_row["text"] = row[3]
        one_row["image"] = row[4]
        result.append(dict(one_row))

    conn.close()
    return result