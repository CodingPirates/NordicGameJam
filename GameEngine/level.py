import json
import pprint

def readLevel (path):

    jsonData = open (path).read ()

    data = json.loads (jsonData)
readLevel ("Ost.json")
