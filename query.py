import csv
import json
import requests

#Example on how to get data using custom API
headers={'content-type': 'application/json'}
payload={'clientid':'C1'}
url='https://clug3kaqw4.execute-api.us-east-1.amazonaws.com/dev/'
r = requests.get(url, data=json.dumps(payload), headers=headers)
data=r.json()


#Converting to CSV 
f = csv.writer(open("mlData.csv", "w"))
f.writerow(["payloadtimestamp", "temperature", "clientid", "bp", "heartrate"])

for x in data:
    f.writerow([x['payloadtimestamp'],
                x["temperature"],
                x["clientid"],
                x["bp"],
                x["heartrate"]])


