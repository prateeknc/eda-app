import pandas as pd
import streamlit as st
import altair as alt

def display_text_column(col_info):
    info_df = pd.DataFrame(list(col_info.items()), columns=['Description', 'Value'])
    st.dataframe(info_df)

def barchart(dataframe, col_name):
    plot = alt.Chart(dataframe).mark_bar().encode(x = col_name, y = 'count()') 
    st.altair_chart(plot)

def frequent_text_values(dataframe):
    st.dataframe(dataframe)