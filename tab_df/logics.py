def data_info(dataframe):
    row_count = dataframe.shape[0]
    column_count = dataframe.shape[1]
    
    # Use the duplicated() function to identify duplicate rows
    duplicates = dataframe[dataframe.duplicated()]
    duplicate_rows_count =  duplicates.shape[0]

    missing_value_row_count = dataframe[dataframe.isna().any(axis=1)].shape[0]

    return row_count, column_count, duplicate_rows_count, missing_value_row_count

def column_info(dataframe):
    columns = list(dataframe.columns)

    memory_usage = []

    for c in columns:
        memory_usage.append(dataframe[c].memory_usage())

    return memory_usage

def data_sample(dataframe, row_count, method):
    if method == "Head":
        return dataframe.head(row_count)
    elif method == "Tail":
        return dataframe.tail(row_count)
    else:
        return dataframe.sample(row_count)