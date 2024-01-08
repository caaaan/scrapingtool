import requests
import pandas as pd
import json

def get_data(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def append_df(json_data, dataframe, key_column="id"):
    if dataframe is None:
        dataframe = pd.DataFrame()

    # Create a set of values in key_column for faster membership testing
    unique_values_set = set(dataframe[key_column].tolist())

    entries_to_add = [
        pd.json_normalize(entry)
        for entry in json_data
        if entry.get(key_column) is not None and entry[key_column] not in unique_values_set
    ]

    if entries_to_add:
        dataframe = pd.concat([dataframe] + entries_to_add, ignore_index=True)

    return dataframe
    #dataframe = pd.concat([dataframe, pd.json_normalize(json_data)], ignore_index=True)
    return dataframe

def get_columns(entry):
    response = requests.get(entry)  # Corrected this line
    data = json.loads(json.dumps(response))  # Ensure the data is serialized to a valid JSON string
    normalized_data = pd.json_normalize(data)
    df = pd.DataFrame.from_records(normalized_data)  # Use from_records to create DataFrame
    # Get the column names (parameters) of the DataFrame
    return df.columns.tolist()


