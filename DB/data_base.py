import _sqlite3
import datetime

start_time = datetime.datetime(1970,1,1)

def write(events_list, DBname):

    conn = _sqlite3.connect(DBname)
    conn.execute('''CREATE TABLE IF NOT EXISTS EVENTS
       (ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
       TIME_ADD   INTEGER NOT NULL,
       ID_EVENT INTEGER NOT NULL,
       DATE_EVENT            TEXT    NOT NULL,
       TITLE           TEXT    NOT NULL,
       _TEXT            TEXT     NOT NULL,
       IMAGE        TEXT NOT NULL );''')
    print "Table created successfully"

    for event in events_list:
        if check_add(DBname,event['id']):

            id_event = str(event['id'])
            date  = "'" + event['date']  +"'"
            title = "'" + event['title'] +"'"
            _text = "'" + event['text']  +"'"
            image = "'" + event['image'] +"'"
            curr_time = str(get_mills())

            string = "INSERT INTO EVENTS (ID_EVENT,TIME_ADD,DATE_EVENT,TITLE,_TEXT,IMAGE) VALUES ("+id_event+","+curr_time+","+date+","+title+","+_text+","+image+")"
            print string
            conn.execute(string)
    conn.commit()
    conn.close()

def read(DBname, except_ids=None, add_time=None):

    resp_str = "SELECT DISTINCT ID_EVENT, TIME_ADD, DATE_EVENT, TITLE, _TEXT, IMAGE FROM EVENTS"

    if len(except_ids) > 0 or add_time > 0:
        resp_str += " WHERE "
    if add_time > 0:
        resp_str += " TIME_ADD > "+str(add_time)
    if len(except_ids) > 0:
        if add_time > 0:
            resp_str += " AND "
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
        one_row["time_add"] = row[1]
        one_row["date"] = row[2]
        one_row["title"] = row[3]
        one_row["text"] = row[4]
        one_row["image"] = row[5]
        result.append(dict(one_row))

    conn.close()
    return result

def check_add(DBname,id):

     resp_str = "SELECT DISTINCT ID_EVENT FROM EVENTS WHERE ID_EVENT = " + str(id)
     conn = _sqlite3.connect(DBname)
     cursor = conn.cursor()
     cursor.execute(resp_str)

     result = True
     for row in cursor:
         id = row[0]
         if id != 0:
             result = False

     conn.commit()
     conn.close()

     return result

def get_mills():
    delta = datetime.datetime.now() - start_time
    return int (delta.total_seconds())