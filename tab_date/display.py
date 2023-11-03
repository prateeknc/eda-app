import pandas as pd
import streamlit as st
import altair as alt

def display_date_column(col_info):
    info_df = pd.DataFrame(list(col_info.items()), columns=['Description', 'Value'])
    st.dataframe(info_df)

def date_barchart(dataframe, col_name):
    plot = alt.Chart(dataframe).mark_bar().encode(x = col_name, y = 'count()') 
    st.altair_chart(plot, use_container_width=True)

def frequent_date_values(dataframe):
    st.dataframe(dataframe)