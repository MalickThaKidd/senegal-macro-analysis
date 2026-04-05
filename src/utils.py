### This will we the doc, where all the function that we will use for the analysis will be

# 1. We import the librairies that we need
import requests
import pandas as pd
import json

# 2. Now, we create the the function that will take the data from the world bank website and transform it into a dataframe for futher analysis

def get_data(indicator_code, country_code, start_year, end_year, scale, new_name = 'value'):
    
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

# 3. Now we create the function to drop all the missing values  and by the same way, calculate outliers to see if in the dataframe, there is any outlier

def clean_data(df, column):
    # Check for missing values
    missing_values = df.isna().sum()
    df = df.dropna()
    
    # Store original size
    original_size = df.shape[0]

   # a. We will delimite the outliers by creating a Q1 and Q3 for the GDP data
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    
    # b. We will calculate the interquartile range (IQR) and use it to filter out the outliers
    IQR = Q3 - Q1

    # c. we will calculate the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # d. We will now detect the outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

    # e. Now we create a cleaned dataframe
    cleaned_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    # The numbers of removed outlier is 
    remove_outlier = original_size - cleaned_df.shape[0]
  
    return cleaned_df, outliers, remove_outlier, missing_values



