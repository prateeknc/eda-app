import pandas as pd

def get_numeric_columns(dataframe):
    # Get a list of all numeric columns
    numeric_cols = dataframe.select_dtypes(include='number').columns.tolist()
    return numeric_cols

def numeric_column_info(col):
    col_info = {}

    col_info["Number of Unique Values"] = len(col.unique())
    col_info["Number of Rows with Missing Values"] = col.isnull().sum()
    col_info["Number of Rows with 0"] = col.eq(0).sum()
    col_info["Number of Rows with Negative Values"] = col.lt(0).sum()
    col_info["Average Value"] = col.mean()
    col_info["Standard Deviation Value"] = col.std()
    col_info["Minimum Value"] = col.min()
    col_info["Maximum Value"] = col.max()
    col_info["Median Value"] = col.median()

    return col_info

def num_value_frequency(dataframe, column):
    # find top 20 most frequent values
    value_counts = dataframe[column].value_counts()
    df_freq = pd.DataFrame({'value': value_counts.index, 'occurence': value_counts.values})[:20]
    df_freq['percentage'] = (df_freq['occurence'] / len(dataframe))*100

    return df_freq
