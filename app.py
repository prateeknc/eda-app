import streamlit as st
import pandas as pd
from tab_df.logics import data_info, column_info, data_sample
from tab_df.display import display_data_info, display_column_info, display_data_sample

st.title("Exploratory Data Analysis")

@st.cache_data
def load_data(file_name):
  return pd.read_csv(file_name)

st.sidebar.title("Upload Data")
uploaded_data = st.sidebar.file_uploader("Choose a CSV file")

if uploaded_data is not None:
  #read csv
  df = load_data(uploaded_data)

tab1, tab2, tab3, tab4 = st.tabs(["DataFrame", "Numeric Series", "Text Series", "Datetime Series"])

with tab1:
  if uploaded_data is not None:
    # section 1
    st.header("Dataframe")
    row_count, column_count, duplicate_rows_count, missing_value_row_count = data_info(df)
    display_data_info(row_count, column_count, duplicate_rows_count, missing_value_row_count)

    # section 2
    st.header("Columns")
    column_memory_usage = column_info(df)
    display_column_info(list(df.columns), df.dtypes.tolist(), column_memory_usage)

    # section 3
    st.header("Explore Dataframe")

    # define user input widgets
    rows_to_display = st.slider("Select the number of rows to be displayed", 5, 50, 5)
    method = st.radio("Exploration Method", ["Head", "Tail", "Sample"])

    data_subset = data_sample(df, rows_to_display, method)
    display_data_sample(data_subset)