# This module contains functions for retrieving and structuring macroeconomic data from external APIs.

import requests
import pandas as pd

# Retrieve World Bank indicator data and format it as a time-indexed DataFrame

def get_data(indicator_code, country_code, start_year, end_year, scale, new_name="value"):
    """
    Took data from the World Bank API and return a cleaned DataFrame.

    Parameters:
        indicator_code (str): World Bank indicator code (e.g., GDP, inflation)
        country_code (str): Country ISO code (e.g., 'SN' for Senegal)
        start_year (int): Start year of data
        end_year (int): End year of data
        scale (float): Scaling factor (e.g., 1e9 for billions)
        new_name (str): Name of the resulting column

    Returns:
        pd.DataFrame: Time-indexed DataFrame with one column of processed data
    """
    
    # This will use the API of the woldbank to retrieve all the information, we need about X country 
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"
    params = {
        "format":   "json",
        "date":     f"{start_year}:{end_year}",
        "per_page": 1000}
    response = requests.get(url, params=params)
    data = response.json()
    
    # Once we retrieve the data from the World Bank API, we will now convert it into a data frame 
    df = pd.DataFrame(data[1])
    df = df[["date", "value"]]

    # Then we convert the value in the scale that you want, if it is GDP for exemple, it will be converted in billion, etc. 
    df["value"] = df["value"] / scale
    
    # After that, we transform the dataframe into time series by setting date as index and standardizing the date using the 'to_datetime'fucntion
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    
    # At the end, I just rename the value column as 'GDP (in billions of USD)' 
    df.rename(columns={"value": new_name}, inplace=True)
    
    return df