import pymongo
import requests
from enum import Enum
from GeoLocation import GeoLocation
from DataFormat import get_data, append_df
import string
import pandas as pd
import json



url_list = []

#be_min = GeoLocation(49.30, 2.33)
#be_max = GeoLocation(51.30,6.24)

#CREATE FUNCTION FOR THE AMOUNT OF POINTS BETWEEN TWO GEOLOCATIONS (WILL MAKE THINGS EASIER)

#test values
be_min = GeoLocation(49.30,2.33)
be_max = GeoLocation(49.31,2.34)

curr_loc = GeoLocation(49.30, 2.33)
be_max.updt_lat(be_max.lat()+0.01)
be_max.updt_lng(be_max.lng()+0.01)
url_list = GeoLocation.get_loc_links(curr_loc,be_min,be_max)
    
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
#for entry in url_list:
#change for loop structure
    
api_data = get_data(url_list)
#change from entry to url_list
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
