#21.11.2025
# import streamlit as st
# import time


# # Title
# st.title("Business Dashboard with Streamlit Layouts")

# # Objective
# msg="## Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard."
# st.write(msg)

# col1, col2= st.columns(2)

# with col1:
#   st.header("Q1 2024")
#   st.write("Revenue: $1.2M")
# with col2:
#     st.header("Q2 2024")
#     st.write("Revenue: $1.5M")


# tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
# with tab1:
#     st.write("Content for Sales Data")
#     sales_data = {
#         "Q1 2024": "$1.2M",
#         "Q2 2024": "$1.5M",
#         "Q3 2024": "$1.3M",
#         "Q4 2024": "$1.6M"
#     }
#     for quarter, revenue in sales_data.items():
#         st.write(f"{quarter}: {revenue}")
# with tab2:
#     st.write("Content for Customer Insights")
#     customer_feedback = [
#         "Great service!",
#         "Very satisfied with the product quality.",
#         "Quick delivery and excellent support."
#     ]
#     for idx, feedback in enumerate(customer_feedback):
#         st.write(f"{idx+1}. {feedback}")
# with tab3:
#   col1, col2= st.columns(2)
#   with col1:
#     st.header("Q1 2024")
#     st.write("Revenue: $1.2M")
#   with col2:
#     col1, col2= st.columns(2)
#     st.header("Q2 2024")
#     st.write("Revenue: $1.5M")
#     # st.write("Content for Market Trends")
#     # market_trends = {
#     #     "Eco-friendly products": "Increasing demand",
#     #     "Online shopping": "Continued growth",
#     #     "Subscription services": "Rising popularity"
#     # }
#     # for trend, status in market_trends.items():
#     #     st.write(f"{trend}: {status}")

#   with st.expander("More Information"):
#       st.write("Additional details on data collection methods.")
#       st.write("## Data was collected through surveys and sales reports.")
#       st.write("- Additional details on data collection methods.")
#       st.write("# Data was collected through surveys and sales reports.")


# # Dynamic Containers
# placeholder = st.empty()

# # Simulate loading data and updating the placeholder
# for i in range(5):
#     placeholder.write(f"Loading data... {i*20}% complete")
#     time.sleep(1)

# # Once loading is complete, display the final message
# placeholder.write("Data loading complete. Displaying business insights.")


#24.11.2025(Option menu)
# import streamlit as st
# from streamlit_option_menu import option_menu

# st.title('Hello, Students!')
# st.write('This is your Python Programming course.')

# with st.sidebar:
#     selected=option_menu(
#         menu_title = "Menu",
#         options = ["ISOM3400", "About", "Contact"],
#         icons = ['house', 'cloud-upload','list-task'],
#         menu_icon= "cast",
#         default_index=0,
#     )

# if selected == "ISOM3400":
#     st.title(f"Welcome to the {selected} page.")

# if selected == "About":
#     st.title(f"Welcome to the {selected} page.")

# if selected == "Contact":
#     st.title(f"Welcome to the {selected} page.")

#Displaying Data elements
# import streamlit as st
# import pandas as pd
# import os

# # Get the current working directory
# current_directory = os.getcwd()
# # Define the file path
# file_path = os.path.join(current_directory, 'winequality-red.csv')

# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path, delimiter=';')

# # Display the DataFrame in an interactive table
# st.write("Wine Quality Data")
# st.dataframe(df)

import pandas as pd
import streamlit as st

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}
df = pd.DataFrame(data)

# Show data with Streamlit elements
st.dataframe(df)                # Interactive table
st.data_editor(df)              # Editable table
st.table(df)                    # Static table

# Customize columns directly in the dataframe display
st.dataframe(df.style.format({'Sales': '${:,.0f}', 
                              'Customers': '{:,.0f}'}))




