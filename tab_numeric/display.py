import pandas as pd
import streamlit as st
import altair as alt

def display_num_column(col_info):
    info_df = pd.DataFrame(list(col_info.items()), columns=['Description', 'Value'])
    st.dataframe(info_df)

def plot_histogram(dataframe, col_name):
    hist = alt.Chart(dataframe).mark_bar().encode(x = col_name, y = 'count()') 
    st.altair_chart(hist)

def display_frequent_values(dataframe):
    st.dataframe(dataframe)
    
