# meraki_client_location
Show Meraki wifi clients in Google maps

# Environment
- Python3
- MongoDB
- ngrok
- Meraki
- Debian 11

# Installation Instruction
1) Download from github
2) Run receiving server of Meraki location scan data
    $**python3 cmxreceiver-mongodb.py -v 'key' -s mysecret**
4) Run ngrok relay daemon
    $**ngrok http 5000**
6) Run web server of location reporting
   $**python3 run-location-backend-server.py**
7) Open Web Browser and enter http://<web server IP>:8000

! Architecture diagram (https://github.com/parkyangbs/meraki_client_location/blob/main/meraki_client_location.jpg)
