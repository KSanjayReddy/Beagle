import paho.mqtt.client as mqtt
import time
import serial

c1=mqtt.Client()
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)


def on_message(client, userdata, message):
	x = str(message.payload.decode("utf-8"))
	x = x.strip()
	print(x)
	# if x=="green":
	# 	var = 'a'
	# 	ser.write(bytes(var.encode('ascii')))
	# 	print(bytes(var.encode('ascii')))
	# elif x=="yellow":
	# 	var = 'b'
	# 	ser.write(bytes(var.encode('ascii')))
	# 	print(bytes(var.encode('ascii')))
	# elif x=="red":
	# 	var = 'c'
	# 	ser.write(bytes(var.encode('ascii')))
	# 	print(bytes(var.encode('ascii')))
	# else:
	# 	var = 'd'
	# 	ser.write(bytes(var.encode('ascii')))
	# 	print(bytes(var.encode('ascii')))


c1.connect("broker.mqttdashboard.com") #connect to broker
c1.on_message=on_message

c1.loop_start()
c1.subscribe("winchat")
while True:
    msg=input("")
    if len(msg)>0:
        #print(msg)
        c1.publish("winchat"," "+msg)

   # sermsg=ser.readline()
    #print("serial:")
    #print(sermsg)


time.sleep(4)
print("finish")
