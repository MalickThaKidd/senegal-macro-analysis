import pandas as pd

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
