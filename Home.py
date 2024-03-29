import streamlit as st
import pandas

st.set_page_config(layout="wide")

# Setting up the top two columns
col1, col2 = st.columns(2)

with col1:
    st.title("Brandon Chow")
    content = """
    Hi, my name is Brandon and I am a python programmer.
    """
    st.info(content)

with col2:
    st.image("images/photo.png")

content2 = """
Below you can find some of the apps I have built in Python.
Feel free to contact me!
"""

st.write(content2)

# Setting up the rest of the page to display my apps
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(row['url'])
        st.write(f"[Source Code]({row['url']})")