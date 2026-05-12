
"""
Visualization module for macroeconomic analysis.

This module contains reusable plotting functions used to visualize
macroeconomic time series, distributions, outliers, and relationships
between variables.

The goal is to keep the notebook clean by separating visualization logic
from the analysis workflow.
"""

import matplotlib.pyplot as plt
import seaborn as sns

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
