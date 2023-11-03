import pandas as pd
from datetime import datetime

def get_date_columns(dataframe):
    date_columns = []

    # Iterate through the DataFrame columns and check if they are datetime objects
    for column in dataframe.columns:
        if pd.api.types.is_datetime64_any_dtype(dataframe[column]):
            date_columns.append(column)

    return date_columns

def date_column_info(col):
    current_date = datetime.now()
    col_info = {}

    col_info["Number of Unique Values"] = len(col.unique())
    col_info["Number of Rows with Missing Values"] = col.isnull().sum()
    col_info["Number of Weekend Dates"] = sum(col.dt.weekday.isin([5,6]))
    col_info["Number of Weekday Dates"] = sum(col.dt.weekday.isin([0,1,2,3,4]))
    col_info["Number of Dates in Future"] = sum(col > current_date)
    col_info["Number of Rows with 1900-01-01"] = sum(col == '1900-01-01')
    col_info["Number of Rows with 1970-01-01"] = sum(col == '1970-01-01')
    col_info["Minimum Value"] = col.min()
    col_info["Maximum Value"] = col.max()

    return col_info

def date_value_frequency(dataframe, column):
    # find top 20 most frequent values
    value_counts = dataframe[column].value_counts()
    df_freq = pd.DataFrame({'value': value_counts.index, 'occurence': value_counts.values})[:20]
    df_freq['percentage'] = (df_freq['occurence'] / len(dataframe))*100

    return df_freq