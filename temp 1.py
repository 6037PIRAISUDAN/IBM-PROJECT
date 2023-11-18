import random
flag = None

while True:
    temp = random.randint(10,120)
    humidity = random.randint(10,120)
    
    if(temp>35 and humidity>60):
        flag = 1
        print(f"High Temperature and Humidity of {temp} and {humidity}")
    elif(temp<35 and humidity<60):
        flag = 0
        print(f"Normal Temperature and Humidity of {temp} and {humidity}")
    
    if(flag):
        print("Alarm Turned on")
    else:
        print("Temp and humi",temp,humidity)
        print("Alarm Turned Off")
        break
