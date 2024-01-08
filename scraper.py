import pymongo
import requests
from enum import Enum
from GeoLocation import GeoLocation
from DataFormat import get_data, append_df
import string
import pandas as pd
import json

basic_url = "https://park4night.com/api/places/around?"
url_ext = "&z=22&radius=200&filter=%7B%7D"
#&lang=en

url_list = []

#be_min = GeoLocation(49.30, 2.33)
#be_max = GeoLocation(51.30,6.24)

#test values
be_min = GeoLocation(49.30,2.33)
be_max = GeoLocation(49.31,2.34)

curr_loc = GeoLocation(49.30, 2.33)
be_max.updt_lat(be_max.lat()+0.01)
be_max.updt_lng(be_max.lng()+0.01)
temp = ""
while(curr_loc.lat() <= be_max.lat()):
    #ßif(curr_loc.lat() != be_max.lat()):
    curr_loc.updt_lng(be_min.lng())

    while(curr_loc.lng() <= be_max.lng()):
        #lat=47.757846722255074&lng=-1.6754150390625
        temp = basic_url + "lat=" + str(curr_loc.lat()) + "&lng=" + str(curr_loc.lng()) + url_ext
        url_list.append(temp)
        curr_loc.inc_min("lng",1)
    curr_loc.inc_min("lat",1)
    
#access points
#print(requests.get(url_list[1]).json)


# Create an empty DataFrame with the desired columns
# ...

# Create an empty DataFrame with the desired columns
columns = ["id", "url", "name", "title", "title_short", "description"
           , "lat", "lng", "services", "activities", "review", "rating", "photo"
           , "images", "isPro", "isTop", "waiting_validation", "distance", "created_at"
           , "review__id", "nature_protect", "type.id", "type.code", "type.label"
           , "address.street", "address.zipcode", "address.city", "address.country"]
dataframe = pd.DataFrame(columns=columns)

i = 1
# Get data from the API
#print()
for entry in url_list:
    
    api_data = get_data(entry)
    # If data is successfully retrieved, append it to the DataFrame
    if api_data:
        dataframe = append_df(api_data, dataframe)
        #filtreleme işlemini append'de değilde gette yapmaya çalış
        print(f"added: {i} of {len(url_list)} ")
    else:
        print(f"not added: {i}")
    i = i+1

#dictionary ile multiple checkle

print(dataframe)
