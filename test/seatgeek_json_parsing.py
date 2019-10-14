import numpy as np
import pandas as pd
from IPython.core.display import clear_output
import json
import glob
import os


def format_ticket_json(file):
    # read in json file
    with open(file) as json_file:
        json_data = json.load(json_file)
    
    # json dict to pandas pd
    df = pd.DataFrame.from_dict(json_data['events'])
    
    if set(['stats', 'venue', 'performers', 'taxonomies']).issubset(df.columns):
        # split the stats, venur, and performers columns
        df = df.assign(**pd.DataFrame(df.stats.values.tolist()).add_prefix('stats_'))
        df = df.assign(**pd.DataFrame(df.venue.values.tolist()).add_prefix('venue_'))
        df = df.assign(**pd.DataFrame(df.performers.str[0].tolist()).add_prefix('performers_'))
        df = df.assign(**pd.DataFrame(df.taxonomies.str[0].tolist()).add_prefix('taxonomies_'))
        return df
    else: 
        print("{} doesn't have appropriate columns".format(file))

files = glob.glob('*.json')
nonblank = list()

for file in files:
    if os.path.getsize(file) > 106:
        nonblank.append(file)

nonblank_sorted = sorted(nonblank,key=lambda x: int(os.path.splitext(x)[0]))

result = pd.DataFrame()

for i in nonblank_sorted:
    print("Reading in file {}/{}".format(i, len(nonblank_sorted)))
    
    result= result.append(format_ticket_json(i))

result.to_csv('seatgeek_ticket_info.csv')