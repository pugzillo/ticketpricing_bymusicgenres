import numpy as np
import pandas as pd
import requests
import requests_cache
import time
from IPython.core.display import clear_output
import json
import glob
import os
import multiprocessing
import json
import os.path
import logging

requests_cache.install_cache()

## Make first request
client_id = 'MTg4MDc2NjV8MTU3MDQ4OTQ1MC45MQ',
client_secret= '956e777ac06bd66c8d6157d380b4be02d9c07a215c6f4694304b28f7ac2a4d6d'

headers = {
    'Content-Type':'application/x-www-form-urlencoded',
}

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'format': 'json',
    'sort': 'datetime_utc.asc'
}

results = list(range(1,30096))
logging.basicConfig(format='%(asctime)s %(message)s')

def runTask(arg):
    try:
        page = arg
        print(page)
        headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        }

        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'format': 'json',
            'page': page,
            'sort': 'datetime_utc.asc'
        }

        r = requests.get('https://api.seatgeek.com/2/events?taxonomies.name=concert', headers=headers, params=payload)
        print(r)
        
        # if we get an error, print the response and halt the loop
        if r.status_code != 200:
            print("Error on page {}".format(page))
            sys.exit()

        with open(f'{page}.json', 'w') as outfile:
            json.dump(r.json(), outfile)

        # if it's not a cached result, sleep
        if not getattr(r, 'from_cache', False):
            time.sleep(0.25)

    except Exception:
        pass

with multiprocessing.Pool(5) as workers:
        workers.map(runTask, results)