### This will we the doc, where all the function that we will use for the analysis will be

# 1. We import the librairies that we need
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 2. Now, we create the the function that will take the data from the world bank website and transform it into a dataframe for futher analysis

def get_data(indicator_code, country_code, start_year, end_year, scale, new_name = 'value'):
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

# 3. Now we create the function to drop all the missing values  and by the same way, calculate outliers to see if in the dataframe, there is any outlier

def clean_data(df, column):
    """
    Clean dataset by removing missing values and detecting/removing outliers using IQR.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        column (str): Column name to clean and analyze

    Returns:
        tuple:
            cleaned_df (pd.DataFrame): Data without outliers
            outliers (pd.DataFrame): Detected outliers
            remove_outlier (int): Number of removed outliers
            missing_values (pd.Series): Count of missing values per column
    """
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

# 4. Here, we will create the visualisation functions, a line chart for the time series, a histogram for the distibution, a box plot for the detection of outliers and a scatter plot for the relation between different component 
# A. Line Chart Function

def line_plt(df, column, xlab, ylab, title = 'Time-series'):
    """
    Plot a time series line chart.

    Parameters:
        df (pd.DataFrame): Input data
        column (str): Column to plot
        xlab (str): Label for x-axis
        ylab (str): Label for y-axis
        title (str): Title of the plot

    Returns:
        None
    """
    
    # We determine the plot size 
    plt.figure(figsize=(15,8))

    # Here, we create the plot and labelise it properly
    sns.lineplot(data=df, x= df.index, y=column)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    #Now we show the plot 
    plt.show()

# B. Histogram Function
def hist_plt(df, column, xlab, kde = False, title = 'Histogram'):
    """
    Plot a histogram to visualize the distribution of a variable.

    Parameters:
        df (pd.DataFrame): Input data
        column (str): Column to analyze
        xlab (str): Label for x-axis
        kde (bool): Whether to overlay a density curve
        title (str): Title of the plot

    Returns:
        None
    """

    # We determine the plot size
    plt.figure(figsize=(15,8))

    # Here, we create the plot and labelise it properly
    sns.histplot(data= df, x= column, kde= kde)
    plt.title(title)
    plt.xlabel(xlab)
    if kde == True : 
        plt.ylabel('Density')
    else : 
        plt.ylabel('Count')
    #Now we show the plot 
    plt.show()

# C. Scatter Plot function
def scat_plt(df, x_col, y_col, xlab, ylab ,title = 'Scatter Plot'):
    """
    Plot a scatter plot to analyze the relationship between two variables.

    Parameters:
        df (pd.DataFrame): Input data
        x_col (str): Column for x-axis
        y_col (str): Column for y-axis
        xlab (str): Label for x-axis
        ylab (str): Label for y-axis
        title (str): Title of the plot

    Returns:
        None
    """
   
    # We determine the plot size
    plt.figure(figsize=(15,8))

    # Here, we create the plot and labelise it properly
    sns.scatterplot(data= df, x = x_col, y = y_col)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

   #Now we show the plot 
    plt.show()

# D. Box Plot function
def box_plt(df, column, xlab, title = 'Box Plot'):
    """
    Plot a boxplot to detect outliers and visualize distribution.

    Parameters:
        df (pd.DataFrame): Input data
        column (str): Column to analyze
        xlab (str): Label for x-axis
        title (str): Title of the plot

    Returns:
        None
    """
    
    # We determine the plot size
    plt.figure(figsize=(15,8))

    # Here, we create the plot and labelise it properly
    sns.boxplot(data= df, x = column)
    plt.title(title)
    plt.xlabel(xlab)
    
    #Now we show the plot 
    plt.show()
