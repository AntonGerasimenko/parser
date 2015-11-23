import json
from DB import data_base as DB

def empty_json():

    return json.dumps('')


def req_all_events_json():

    data = {}
    data['all'] = True

    return json.dumps(data)

def resp_all_events_json():

    all = {}

    rows = DB.read()


    for num in range(0,5):

        data = {}
        data['id'] = 1
        data['title'] = "Gorky Park"
        data['text'] = "Dark Blue Red"
        data['image'] = "http://hdkjhfksdf.jpg"

        all['event'] = data


    return json.dumps(rows)


def parse(data):

    buff = json.loads(data)
    return json.loads(str(buff))


