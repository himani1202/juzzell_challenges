#!/usr/bin/env python

import requests
import json
import sys

def getkeyvalue(url,djson):
#    djson = {}
    r = requests.get(url)
    if r.status_code == 404:
        return

    for line in r.text.split('\n'):

        url2 = '{0}/{1}'.format(url, line)

        if line.endswith('/'):
            newkey = line.split('/')[-2]
            djson[newkey] = {}
            getkeyvalue(url2,djson[newkey])

        else:
            r = requests.get(url2)
            if r.status_code != 404:
                try:
                    djson[line] = json.loads(r.text)
                except ValueError:
                    djson[line] = r.text
            else:
                djson[line] = None

    print(json.dumps(djson))



if __name__ == '__main__':

    djson = {}
	url = 'http://169.254.169.254/latest/meta-data'
	if len(sys.argv) > 1 :
	   url = '{0}/{1}'.format(url,sys.argv[2])
	getkeyvalue(url,djson)