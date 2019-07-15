import csv
import json
import os
import sys
from datetime import datetime

#User or Ansible passes the CSV file name
csvfile = str(sys.argv[1])
jsonFilePath= "happy.json"

#set some of the dictionaries for json jsonFile
workspacesprop = {
"RunningMode": "AUTO_STOP",
"RunningModeAutoStopTimeoutInMinutes": 0,
"RootVolumeSizeGib": 50,
"UserVolumeSizeGib": 80,
"ComputeTypeName": "STANDARD"}

tags = { "Key": "test",
"Value": "test",
}

# Open the CSV, write to JSON for each line
data = {}
with open( str(csvfile), 'r' ) as f:
  reader = csv.DictReader(f)
  with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write("")
  counter = 0
  for row in reader:
    data = dict(row)
    #set vars for json file
    DirectoryID = str(data["DirectoryId"])
    UserName = str(data["UserName"])
    BundleID = str(data["BundleId"])
    VolumeEncryptionKey = str(data["VolumeEncryptionKey"])
    #set dict for JSON json file
    properties = {
      "DirectoryId": DirectoryID,
      "UserName": UserName,
      "BundleId": BundleID,
      "VolumeEncryptionKey": VolumeEncryptionKey,
      "UserVolumeEncryptionEnabled": "true",
      "RootVolumeEncryptionEnabled": "true",
      "WorkspaceProperties" : workspacesprop,
      'Tags': [ tags ]}

    entry = {'Workspaces': [properties]}

    with open(jsonFilePath, "a") as jsonFile:
      jsonFile.write(json.dumps(entry, indent=4))

    #counter portion to only have 8 users per file
    counter += 1
    #once 8 users is hit, accomodate and reset
    if counter >= 8:
      stamp = str(datetime.utcnow().strftime('%S.%f'))
      jsonFilePath = "happy" + stamp + ".json"
      with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write("")
      counter = 0

print("JSON saved!")
