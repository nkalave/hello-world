import json
import urllib3
import requests
from requests.auth import HTTPBasicAuth

def get_headcount_data(query):
    date = str(query)
    url = 'https://wd5-services1.myworkday.com/ccx/service/customreport2/paloaltonetworks/ISU_Report_Master/NK_-_Workday_Snapshot_Master_RAAS?effective_date='+date+'-08%3A00&format=json'
    r = requests.get(url, auth=HTTPBasicAuth('ISU_Report_Master', 'PanW$$_4328@'))
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
headcount_details(hc_data)