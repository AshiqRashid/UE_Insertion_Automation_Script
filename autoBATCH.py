###########################################################Load CSV#################################################################
import pandas as pd
df = pd.read_csv(r'./UE.csv')
length = len(df)
####################################################################################################################################

#########################################################Load MongoDB###############################################################
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient("mongodb://localhost:27017/")

# Access a specific database i.e. open5gs
db = client["open5gs"]

# Access a specific collection within the database i.e subscribers
collection = db["subscribers"]
###################################################################################################################################

#######################################################Add Subscribers#############################################################
i = 0
k = 0
for j in range(length):
    data =  {
  "schema_version": 1,
  "imsi": "",
  "msisdn": [],
  "imeisv": [],
  "mme_host": [],
  "mme_realm": [],
  "purge_flag": [],
  "security": {
    "k": "",
    "op": None,
    "opc": "",
    "amf": "8000"
  },
  "ambr": { "downlink": { "value": 1, "unit": 3 }, "uplink": { "value": 1, "unit": 3 } },
  "slice": [
    {
      "sst": 1,
      "default_indicator": True,
      "session": [
        {
          "name": "internet",
          "type": 1,
          "qos": { "index": 9, "arp": {"priority_level":8, "pre_emption_capability":1, "pre_emption_vulnerability":1} },
          "ambr": { "downlink": { "value": 1, "unit": 3 }, "uplink": { "value": 1, "unit": 3 }},
          "pcc_rule": []
        },
        {
          "name": "ims",
          "type": 1,
          "qos": { "index": 5, "arp": {"priority_level":1, "pre_emption_capability":1, "pre_emption_vulnerability":1} },
          "ambr": { "downlink": { "value": 3850, "unit": 1 }, "uplink": { "value": 1530, "unit": 1 }},         
	  "pcc_rule" : [{"qos":{"index":1,"arp":{"priority_level":2,"pre_emption_capability":2,"pre_emption_vulnerability":2},"mbr":{"downlink":{"value":128,"unit":1},"uplink":{"value":128,"unit":1}},"gbr":{"downlink":{"value":128,"unit":1},"uplink":{"value":128,"unit":1}}}}, {"qos":{"index":2,"arp":{"priority_level":4,"pre_emption_capability":2,"pre_emption_vulnerability":2},"mbr":{"downlink":{"value":128,"unit":1},"uplink":{"value":128,"unit":1}},"gbr":{"downlink":{"value":128,"unit":1},"uplink":{"value":128,"unit":1}}}}]

        }

                  ]
    }
  ],
  "access_restriction_data": 32,
  "subscriber_status": 0,
  "network_access_mode": 0,
  "subscribed_rau_tau_timer": 12,
  "__v": 0 
}

    data["imsi"] = str(df["IMSI"][i])
    data["msisdn"] = [str(df["MSISDN\n"][i])]
    data["security"]["k"] = str(df["KEY\n"][i])
    data["security"]["opc"] = str(df["OPC\n"][i])

    # Insert the document into the collection
    try:
        inserted_document = collection.insert_one(data)
        #print("Inserted document ID:", inserted_document.inserted_id)
        i = i + 1
    except DuplicateKeyError as e:
        print("Duplicate IMSI found!", df["IMSI"][i], "Skipping this IMSI.")
        k = k + 1
        i = i + 1

l = i - k
print("Total number of inserted subscriber", l, "out of", length)
