import requests
# url to call the api
url = "https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api" \
     "/c55fea158925365eedc47d126001b6a64847262bb64530761d9d8136b136a518/entries/entries"

# set the response equal to the get url for the api
response = requests.get(url)

# change the response type to json
json = response.json()

# the items are in a list so we set a name for the list
items_list = json['entries']


