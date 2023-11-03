import pandas as pd

def get_text_columns(dataframe):
    cat_columns = dataframe.select_dtypes(include='object')
    cat_col_names = cat_columns.columns.tolist()
    return cat_col_names

def text_column_info(col):
    col_info = {}

    col_info["Number of Unique Values"] = len(col.unique())
    col_info["Number of Rows with Missing Values"] = col.isnull().sum()
    col_info["Number of Empty Rows"] = col.eq("").sum()
    col_info["Number of Rows with Only Whitespace"] = len(col[col.str.isspace()])
    col_info["Number of Rows with Only Lowercases"] = len(col[col.str.islower()])
    col_info["Number of Rows with Only Uppercases"] = len(col[col.str.isupper()])
    col_info["Number of Rows with Only Alphabet"] = len(col[col.str.isalpha()])
    col_info["Number of Rows with Only Digits"] = len(col[col.str.isdigit()])
    col_info["Mode Value"] = col.mode()[0]

    return col_info

def text_value_frequency(dataframe, column):
    # find top 20 most frequent values
    value_counts = dataframe[column].value_counts()
    df_freq = pd.DataFrame({'value': value_counts.index, 'occurence': value_counts.values})[:20]
    df_freq['percentage'] = (df_freq['occurence'] / len(dataframe))*100

    return df_freq