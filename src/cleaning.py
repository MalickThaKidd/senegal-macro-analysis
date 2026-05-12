# This module contains functions for cleaning macroeconomic datasets.

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
