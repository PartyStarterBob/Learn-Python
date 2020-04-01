import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0]+ " "+ "<url>")
    sys.exit(1)

req = requests.get("http://"+ sys.argv[1])
print("\n"+str(req.headers))

gethost = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethost + "\n")

#ipinfo.io

req2 = requests.get("https://ipinfo.io/"+gethost+"/json")
resp = json.loads(req2.text)

print("Location: "+resp["loc"])
print("Region: "+resp["region"])
print("City:" +resp["city"])
print("Country:" +resp["country"])
