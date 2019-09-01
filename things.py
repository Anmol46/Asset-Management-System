import urllib

data=urllib.urlopen("https://api.thingspeak.com/update?api_key=RIWDCNRNX69VRCCF&field1=0"+str(100));
print ("data");