import pymongo
from pymongo import MongoClient
import requests
import pandas as pd
import json

def get_data(urls):
    concatenated_data = {}  # Initialize an empty dictionary for concatenated data
    
    for url in urls:
        #multi-threading işi kolaylaştırır
        response = requests.get(url)
        
        if response.status_code == 200:
            json_data = response.json()
            concatenated_data[url] = json_data  # Store the JSON data in the dictionary
        else:
            print(f"Error {response.status_code}: {response.text}")

    return concatenated_data


    #
def append_db(json_data, dataframe, key_column="id"):
    uri = "" #ENTER URI
    
    client = MongoClient(uri)
    db = client.url_data
    coll = db.url_list
   
    entries_to_add = []

    for entry in json_data:
        #if entry.get(key_column) is not None and entry[key_column] not in unique_values_set:
        if coll.find_one({key_column: entry[key_column]}) == None:
            entries_to_add.append(entry)
            coll.insert_one(entry)



def get_columns(entry):
    response = requests.get(entry)  # Corrected this line
    data = json.loads(json.dumps(response))  # Ensure the data is serialized to a valid JSON string
    normalized_data = pd.json_normalize(data)
    df = pd.DataFrame.from_records(normalized_data)  # Use from_records to create DataFrame
    # Get the column names (parameters) of the DataFrame
    return df.columns.tolist()


