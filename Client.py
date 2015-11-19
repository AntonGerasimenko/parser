import urllib
import requests
import json

def get_html(url):

    response = urllib.urlopen(url)
    return response.read()

def get_Json():

    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)

    return json_data


def post(url):

    json = get_Json()

    r = requests.post(url,None,json, auth=('user', 'pass'))

    return r.links



def main():

    print (post('http://127.0.0.1'))


if __name__ == '__main__':
    main()