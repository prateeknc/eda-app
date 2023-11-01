import pandas as pd
import streamlit as st

def display_data_info(row_count, column_count, duplicate_rows_count, missing_value_row_count):
    # create a markdown table 
    table_markdown = f"""
      | Description | Value | 
      |---|---|
      | Number of Rows | {row_count} |
      | Number of Columns | {column_count} |
      | Number of Duplicated Rows | {duplicate_rows_count} |
      | Number of Rows with Missing Values | {missing_value_row_count} |
      """
    st.markdown(table_markdown)

def display_column_info(columns, data_type, memory_usage):
    column_info_table = pd.DataFrame({
        "column": columns,
        "data_type":data_type,
        "memory": memory_usage
    })

    st.dataframe(column_info_table, hide_index=True)

def display_data_sample(data):
    st.dataframe(data)