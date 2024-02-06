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
def append_df(json_data, dataframe, key_column="id"):
    if dataframe is None:
        dataframe = pd.DataFrame()

    # Create a set of values in key_column for faster membership testing
    unique_values_set = set()

    entries_to_add = []

    for entry in json_data:
        if entry.get(key_column) is not None and entry[key_column] not in unique_values_set:
        #if colloection.find_one({"name": new_document["name"]}) == None:
            entries_to_add.append(entry)
            unique_values_set.add(entry[key_column])
             #no need for unique values since after the first iteration it will do the filtering properly
        
    #upload documents here 
    if entries_to_add:
        dataframe = pd.concat([dataframe] + entries_to_add, ignore_index=True)

    return dataframe
def get_columns(entry):
    response = requests.get(entry)  # Corrected this line
    data = json.loads(json.dumps(response))  # Ensure the data is serialized to a valid JSON string
    normalized_data = pd.json_normalize(data)
    df = pd.DataFrame.from_records(normalized_data)  # Use from_records to create DataFrame
    # Get the column names (parameters) of the DataFrame
    return df.columns.tolist()


