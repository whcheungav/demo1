import streamlit as st


st.title("Business Sales Dashboard")

st.header("Header")
st.write("Message")


age=st.number_input("Enter monthly Sales Target (in USD): ",
                    min_value=0,
                    max_value=100000,
                    value=50000)
