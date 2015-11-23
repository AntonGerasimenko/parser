import urllib
import requests
import JsonCreator as creator


def get_html(url):

    response = urllib.urlopen(url)
    return response.read()


def post(url):


    json = creator.req_all_events_json()

    json = creator.resp_all_events_json()

    print (json)

   # r = requests.post(url,None,json, auth=('user', 'pass'))


    #return r.text

def main():

    print (post('http://127.0.0.1'))

if __name__ == '__main__':
    main()