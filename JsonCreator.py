import json
from DB import data_base as DB
import os

def get_all_rows(ids=None,time=None):
    path = os.path.dirname(os.path.abspath(__file__)) + '\\events.db'

    return DB.read(path, ids, time)


def empty_json():

    return json.dumps('')

def req_all_events_json(olds=None,time=None):
    data = {}
    out = list()
    if time != None:
        data['time'] = time
        out.append(data)
    if olds == None:
        data['all'] = True
    else:
        for old in olds:
            data = {}
            data['id'] = old
            out.append(data)
    return out


def resp_all_events_json(except_ids=None,time=None):

    rows = get_all_rows(except_ids,time)
    jsn = json.dumps(rows)
    print "JSN"
    print jsn

    return jsn

def parse(data):

    dict = json.loads(data)
    return dict


