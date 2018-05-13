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
data = """[{'payloadtimestamp': '1526001268', 'temperature': '101', 'clientid': 'C1', 'bp': '88', 'heartrate': '74'}, {'payloadtimestamp': '1526001273', 'temperature': '102', 'clientid': 'C1', 'bp': '145', 'heartrate': '74'}, {'payloadtimestamp': '1526001278', 'temperature': '100', 'clientid': 'C1', 'bp': '82', 'heartrate': '76'}, {'payloadtimestamp': '1526001283', 'temperature': '101', 'clientid': 'C1', 'bp': '92', 'heartrate': '74'}, {'payloadtimestamp': '1526001288', 'temperature': '102', 'clientid': 'C1', 'bp': '89', 'heartrate': '73'}, {'payloadtimestamp': '1526001293', 'temperature': '96', 'clientid': 'C1', 'bp': '97', 'heartrate': '72'}, {'payloadtimestamp': '1526001298', 'temperature': '98', 'clientid': 'C1', 'bp': '88', 'heartrate': '76'}, {'payloadtimestamp': '1526001303', 'temperature': '100', 'clientid': 'C1', 'bp': '99', 'heartrate': '73'}, {'payloadtimestamp': '1526001308', 'temperature': '99', 'clientid': 'C1', 'bp': '139', 'heartrate': '72'}, {'payloadtimestamp': '1526001313', 'temperature': '98', 'clientid': 'C1', 'bp': '99', 'heartrate': '73'}]"""
f = csv.writer(open("mlData.csv", "w"))
f.writerow(["payloadtimestamp", "temperature", "clientid", "bp", "heartrate"])

for x in data:
    f.writerow([x['payloadtimestamp'],
                x["temperature"],
                x["clientid"],
                x["bp"],
                x["heartrate"]])


