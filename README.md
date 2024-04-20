# meraki_client_location
Show Meraki wifi clients in Google maps

# Environment
Python3
MongoDB
ngrok
Meraki
Debian 11

**#Installation instruction#**
1) Download 
2) Run receiving server of Meraki location scan data
    $python3 cmxreceiver-mongodb.py -v 'key' -s mysecret
3) Run web server of location reporting
   $python3 run-location-backend-server.py
4) Open Web Browser and enter http://<web server IP>:8000

