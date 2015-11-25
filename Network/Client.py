import urllib
import JsonCreator as creator
import requests

def get_html(url):

    response = urllib.urlopen(url)
    return response.read()

def post(url):
    #{13648, 13654,13664,13651,13657,13667,13670}
    json = creator.req_all_events_json({13648, 13654,13664,13651,13657,13667,13670}, time=123123)
    print "Get all events with the exception of : "
    print  json

    r = requests.post(url,None,json, auth=('user', 'pass'))

    return r

def main():

    response = post('http://192.168.5.55')
    print "Server response:"
    print response.text

if __name__ == '__main__':
    main()