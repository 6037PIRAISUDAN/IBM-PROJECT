import wiotp.sdk.device

import time

import random

myConfig = {
    "identity": {
        "orgId": "k2m20e",
        "typeId": "NodeMCU",
        "deviceId": "12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback (cmd):
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient (config=myConfig, logHandlers=None)
client.connect()

def pub (data):
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0)
                
    print("Published data Successfully: %s", myData)

while True:
    myData={'name': 'Train1', 'lat': 13.000988 , 'lon': 77.674746 }
    pub (myData)
    time.sleep(3)
    

    myData={'name': 'Train1', 'lat': 13.104706  , 'lon': 77.591532 }
    pub (myData)
    time.sleep(3)

    myData={'name': 'Train1', 'lat': 13.818805 , 'lon': 77.500015 }
    pub (myData)
    time.sleep (3)

    myData={'name': 'Train1', 'lat': 15.396830 , 'lon':  77.864205}
    pub (myData)
    time.sleep(3)

    myData={'name': 'Train1', 'lat': 16.757347 , 'lon': 77.999011 }
    pub (myData)
    time.sleep(3)

    myData={'name': 'Train1', 'lat': 17.389526 , 'lon': 78.499394 }
    pub (myData)
    time.sleep(3)
    client.commandCallback = myCommandCallback

client.disconnect()
 
