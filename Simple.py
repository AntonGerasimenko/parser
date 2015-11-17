import urllib

import

def get_html(url):

    response = urllib.urlopen(url)
    return response.read()

def parse(html):

    soap =



def main():

    print (get_html("http://www.graffiti.by/"))


if __name__ == '__main__':
        main()





