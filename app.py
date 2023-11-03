import streamlit as st
import pandas as pd
from tab_df.logics import data_info, column_info, data_sample
from tab_df.display import display_data_info, display_column_info, display_data_sample
from tab_numeric.logics import get_numeric_columns, numeric_column_info, num_value_frequency
from tab_numeric.display import display_num_column, plot_histogram, display_frequent_values
from tab_text.logics import get_text_columns, text_column_info, text_value_frequency
from tab_text.display import display_text_column, barchart, frequent_text_values

st.title("Exploratory Data Analysis")

@st.cache_data
def load_data(file_name):
  data = pd.read_csv(file_name)
  data['Date'] = pd.to_datetime(data['Date'])
  return data

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

with tab2:
  if uploaded_data is not None:
    # find numeric columns in the dataframe
    num_cols = get_numeric_columns(df)
    selected_num_col = st.selectbox("Which numeric column do you want to explore?", num_cols)

    # section 1
    st.header(f"{selected_num_col}")
    num_col_info = numeric_column_info(df[selected_num_col])
    display_num_column(num_col_info)

    # section 2
    st.header("Histogram")
    plot_histogram(df, selected_num_col)

    # section 3
    st.header("Most Frequent Values")
    freq_df = num_value_frequency(df, selected_num_col)
    display_frequent_values(freq_df)

with tab3:
  if uploaded_data is not None:
    # find numeric columns in the dataframe
    text_cols = get_text_columns(df)
    selected_text_col = st.selectbox("Which text column do you want to explore?", text_cols)

    # section 1
    st.header(f"{selected_text_col}")
    text_col_info = text_column_info(df[selected_text_col])
    display_text_column(text_col_info)

    # section 2
    st.header("Bar Chart")
    barchart(df, selected_text_col)

    # section 3
    st.header("Most Frequent Values")
    freq_df = text_value_frequency(df, selected_text_col)
    frequent_text_values(freq_df)