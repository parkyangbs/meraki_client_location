# meraki_client_location
Show Meraki wifi clients in Google maps

# Environment
- Python3
- MongoDB
- ngrok
- Meraki
- Debian 11
- Google Maps API

# Installation Instruction
1) Download from github
2) Configuration

      2.1) Update Google Map API Key
   
      2.2) Update Meraki localtion API key
4) Deployment
      3.1) Run receiving server of Meraki location scan data
   
            python3 cmxreceiver-mongodb.py -v 'key' -s 'secret'
      3.2) Run ngrok relay daemon

           ngrok http 5000
      3.3) Run web server of location reporting

           python3 run-location-backend-server.py
   
5) Open Web Browser and enter http://35.226.133.19:8000
   
# Diagram
https://github.com/parkyangbs/meraki_client_location/blob/main/Meraki_Client_Location.jpg
