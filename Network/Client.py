import urllib
import JsonCreator
import requests

def get_html(url):

    response = urllib.urlopen(url)
    return response.read()


def post(url):


    json = JsonCreator.req_all_events_json()

    print (json)

    r = requests.post(url,None,json, auth=('user', 'pass'))

    return r.text

def main():

    print (post('http://192.168.5.55'))

if __name__ == '__main__':
    main()