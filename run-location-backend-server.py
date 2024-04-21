from flask import Flask, render_template
from pymongo import MongoClient
import pytz
from datetime import datetime

app = Flask(__name__)

client_mac = "10:f9:20:18:d3:c6"

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Assuming MongoDB is running locally on the default port
db = client['test']  # Replace 'your_database_name' with the name of your MongoDB database
collection = db['cmxdata']  # Replace 'your_collection_name' with the name of your MongoDB collection

@app.route('/')

def index():
  
    # Retrieve data from MongoDB
    lastobject = collection.find().sort({'_id': -1}).limit(1)
 
    # Get the first (and only) document
    doc = lastobject[0]

    #data = doc.get("data")
    #print(data)

    # Extract the "data" field
    data = doc.get("data")
    
    # Extract the "observations" field from "data" if "data" exists
    observations = data.get("observations") if data else None

    # Check if "observations" exist
    if observations is not None:
        # Print the extracted data
        print({
            "data": data,
            "observations": observations
        })
    else:
        print("The 'observations' field is missing in the document.")
   
    # Extract the "data" and "observations" fields
    observations = doc['data']['observations']

    observations_sorted = sorted(observations, key=lambda x: x['clientMac'])

    # Extract clientMac and lat from observations
    eastern = pytz.timezone('America/New_York')

    data = []
    for obs in observations_sorted:
        utc_time = datetime.strptime(obs['seenTime'], '%Y-%m-%dT%H:%M:%SZ')
        eastern_time = utc_time.replace(tzinfo=pytz.utc).astimezone(eastern)

        if obs['clientMac'] == 'e0:33:8e:57:cc:93':
            comment = 'iPhonex'
        elif obs['clientMac'] == '10:f9:20:18:d3:c6':
            comment = 'CP-860'
        elif obs['clientMac'] == '8c:85:90:9d:a1:33':
            comment = 'MAC Pro'
        else:
            comment = ''

        data.append({
            'clientMac': obs['clientMac'], 
            'manufacturer': obs.get('manufacturer', ''),  # Add manufacturer field
            'comment': comment,
            'lat': obs['location']['lat'],
            'lng': obs['location']['lng'],
            'seenTime': eastern_time.strftime('%Y-%m-%d %H:%M:%S'),
            'map_url': f"https://www.google.com/maps/embed/v1/place?key='Google_maps _API_Key'&q={obs['location']['lat']},{obs['location']['lng']}" # Embedd -trd in iframe
        })

    # Render HTML template with the data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
