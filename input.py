import urllib2
import json


url = ""

response = urllib2.urlopen(url)
data = json.loads(response.read())


# Writing JSON data
with open('monero.json', 'w') as f:
    json.dump(data, f)

# Reading data back
# with open('data.json', 'r') as f:
#     new_data = json.load(f)
#     print(new_data[0])

