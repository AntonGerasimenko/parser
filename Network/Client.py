import urllib
import JsonCreator as creator
import requests

def get_html(url):

    response = urllib.urlopen(url)
    return response.read()

def post(url):

    json = creator.req_all_events_json()
    print (json)

    r = requests.post(url,None,json, auth=('user', 'pass'))

    return r

def main():

   post('http://192.168.5.55')

if __name__ == '__main__':
    main()