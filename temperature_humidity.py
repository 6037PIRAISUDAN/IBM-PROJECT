#Build a python code,Assume u get Temperature and Humidity values
#(Generated with random function) and write a condition to countinuosly
#detect alarm in case of high temperature


from random import*     #import random value generator package
temp=randint(1,100);    #Random Value generator
hum=randint(1,100);     
print("Temperature is",temp,"\nHumidity is",hum);
if temp>=70 and hum>60:
        print("Hazadous area..Leave the place");
elif temp>=70:
    print("Temperature high");
else:
    print("Everything is Fine");
