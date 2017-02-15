import json
import urllib3
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
from requests.auth import HTTPBasicAuth

def get_headcount_data(query):
    date = str(query)
    url = "URL GOES HERE - SAMPLE FILE EXPECTS JSON FORMAT"
    r = requests.get(url, auth=HTTPBasicAuth('USERNAME', 'PW'))
    data = json.loads(r.text)
    return data

def headcount_details(data):
    headcount = 0
    male = 0
    female = 0
    
    for item in data['Report_Entry']:
        headcount = headcount + 1
        if item.has_key('gender'):
            if item['gender'] == "Male":
                male = male + 1
            if item['gender'] == "Female":
                female = female + 1
    print 'Headcount:', headcount
    print 'Male:', male
    print 'Female:', female

new_date = input('What is the date:')

hc_data = get_headcount_data(new_date)

df = pd.DataFrame(hc_data["Report_Entry"])
df = df.set_index("employee_id")

print df