import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_icon="🗺", page_title="my app")

st.title('my app')

#sidebar
st.sidebar.header('User Input Features')
slider = st.sidebar.slider('x')  # 👈 this is a widget

st.write("Here's our first attempt at using data to create a table:")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

with col3:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


with col1:
    dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)))
    st.table(dataframe)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)