import streamlit as st
import pandas as pd
from tab_df.logics import data_info

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
  st.header("Explore Dataframe")
  row_count, column_count, duplicate_rows_count, missing_value_row_count = data_info(df)
  st.write(f"{row_count}, {column_count}, {duplicate_rows_count}, {missing_value_row_count}")