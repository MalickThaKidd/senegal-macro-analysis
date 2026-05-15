import pandas as pd

# A. GDP Growth Rate Function
def compute_growth_rate(df, column, new_column="growth_rate"):
    """
    Compute the percentage growth rate of a time series.

    Parameters:
        df (pd.DataFrame): Input time-series DataFrame
        column (str): Column used to compute growth
        new_column (str): Name of the growth rate column

    Returns:
        pd.DataFrame: DataFrame with the growth rate column added
    """
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    df.sort_index(ascending=True, inplace=True)
    df[new_column] = df[column].pct_change() * 100
    
    return df

# B. CAGR Function
def compute_cagr(df, column, start_year, end_year):
    """
    Compute the Compound Annual Growth Rate (CAGR) for a given time series.

    Parameters:
        df (pd.DataFrame): Input time-series DataFrame
        column (str): Column used to compute CAGR
        start_year (int): Starting year for CAGR calculation
        end_year (int): Ending year for CAGR calculation
    Returns:
        float: CAGR value in percentage
    """
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    df.sort_index(ascending=True, inplace=True)
    start_value = df.loc[df.index.year == start_year, column].iloc[0]
    end_value = df.loc[df.index.year == end_year, column].iloc[0]
    years = end_year - start_year
    cagr = ((end_value / start_value) ** (1 / years) - 1) * 100
    
    return cagr

# C. Moving Average Function
def compute_moving_average(df, column, window, new_column=None):
    """
    Compute the moving average of a time series.

    Parameters:
        df (pd.DataFrame): Input time-series DataFrame
        column (str): Column used to compute moving average
        window (int): Number of periods for moving average
        new_column (str): Name of the moving average column

    Returns:
        pd.DataFrame: DataFrame with the moving average column added
    """
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    df.sort_index(ascending=True, inplace=True)
    
    if new_column is None:
        new_column = f"{column} {window}Y MA"
        
    df[new_column] = df[column].rolling(window=window).mean()
    
    return df

# D. Volatility Function
def compute_volatility(df, column):
    """
    Compute the volatility (standard deviation) of a time series.

    Parameters:
        df (pd.DataFrame): Input time-series DataFrame
        column (str): Column used to compute volatility

    Returns:
        float: Volatility value
    """
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    df.sort_index(ascending=True, inplace=True)
    
    volatility = df[column].dropna().std()
    
    return volatility
