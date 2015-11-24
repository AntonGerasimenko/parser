import json
from DB import data_base as DB
import os

def get_all_rows():
    path = os.path.dirname(os.path.abspath(__file__)) + '\\events.db'
    return DB.read(path)

def empty_json():

    return json.dumps('')




def req_all_events_json(olds=None):
    data = {}
    out = list()

    if olds == None:
        data['all'] = True
        out.append(data)
        return out
    else:
        for old in olds:
            data = {}
            data['id'] = old
            out.append(data)
        return out



def resp_all_events_json(olds=None):

    rows = get_all_rows()
    if olds==None:
        return json.dumps(rows)



def parse(data):

    dict = json.loads(data)
    return dict


