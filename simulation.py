import paho.mqtt.client as mqtt
from datetime import datetime
import time
import json
from random import *
client1=mqtt.Client("C1")
client1.connect("localhost")
client1.loop_start()
client2=mqtt.Client("C2")
client2.connect("localhost")
client2.loop_start()

client3=mqtt.Client("C3")
client3.connect("localhost")
client3.loop_start()
clients=["C1","C2","C3"]
for i in range(10):
	for client_name in clients:
		timestamp=int(time.time())
		heartrate=randint(72,76)
		bp=randint(80,150)
		tem=randint(96,102)
		data={"timestamp":timestamp,"heartrate":heartrate,"bp":bp,"clientid":client_name,"temperature":tem}
		if client_name=="C1":
		jdata1=json.dumps(data)
		if client_name=="C2":
		jdata2=json.dumps(data)
		if client_name=="C3":
		jdata3=json.dumps(data)

		client1.publish("localgateway_to_awsiot",jdata1,1)
		client2.publish("localgateway_to_awsiot",jdata2,1)
		client3.publish("localgateway_to_awsiot",jdata3,1)
	print("done")
	time.sleep(300)
client1.disconnect()
client2.disconnect()
client3.disconnect()