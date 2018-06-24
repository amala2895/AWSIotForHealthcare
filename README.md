# AWS Iot For Healthcare

![alt text](https://github.com/amala2895/AWSIotForHealthcare/blob/master/architecture.png)

simulation.py - Script to simulate the heartbeat, BP and temperature and send to AWS IOT via mqtt broker.

alert.py - This is lambda script to alert the user if blood pressure is not in the optimal threshold. This function is triggered by AWS IOT rule and its action is to call AWS SNS service to send SMS to the user.

checkstatus.py- This is a lamnda script to check health of device and sends alert message to the user if device is not working. This script is scheduled to run every 10 hours.

index.js - Script to make data available at API Gateway 

query.py - Script to query the API and save the data into a CSV format 



