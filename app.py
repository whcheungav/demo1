import streamlit as st
import time


# Title
st.title("Business Dashboard with Streamlit Layouts")

# Objective
msg="## Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard."
st.write(msg)

col1, col2= st.columns(2)

with coli:
  st.header("Q1 2024")
  st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
