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
# # Display dynamic business insights
# business_insights = [
#     "Revenue increased by 15% in Q1 2024.",
#     "Customer satisfaction improved by 10%.",
#     "Market trends show a growing demand for eco-friendly products."
# ]
# for insight in business_insights:
#     placeholder.write(insight)
#     time.sleep(2)


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

# import pandas as pd
# import streamlit as st

# # Sample data
# data = {'Product': ['A', 'B', 'C'], 
#         'Sales': [1200, 850, 950], 
#         'Customers': [300, 400, 350]}
# df = pd.DataFrame(data)

# # Show data with Streamlit elements
# st.dataframe(df)                # Interactive table
# st.data_editor(df)              # Editable table
# st.table(df)                    # Static table

# # Customize columns directly in the dataframe display
# st.dataframe(df.style.format({'Sales': '${:,.0f}', 
#                               'Customers': '{:,.0f}'}))

#Data visualization

# import streamlit as st
# import numpy as np
# import pandas as pd

# # Step 3: Generate Random Sales Data
# sales_data = np.random.rand(100) * 1000

# # Step 4: Create a DataFrame
# products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
# sales = np.random.rand(5) * 1000
# customers = np.random.randint(1, 100, size=5)

# df = pd.DataFrame({
#     'Product': products,
#     'Sales': sales,
#     'Customers': customers
# })

# # Step 5: Visualize Sales Data

# # Display DataFrame using st.dataframe
# st.markdown("### Product Sales and Customer Data")
# st.dataframe(df)  # Interactive table with sorting and resizing

# # Line Chart - Sales Over Time
# st.markdown("### Sales Over Time")
# st.line_chart(sales_data)

# # Area Chart - Cumulative Sales
# st.markdown("### Cumulative Sales")
# st.area_chart(sales_data)

# # Bar Chart - Sales by Product
# st.markdown("### Sales by Product")
# st.bar_chart(df[['Product', 'Sales']].set_index('Product'))

# # Scatter Chart - Customer Engagement by Product
# st.markdown("### Customer Engagement by Product")
# st.scatter_chart(df[['Product', 'Customers']].set_index('Product'))

#Business Form

# import streamlit as st
# import pandas as pd

# # Sample Data
# data = {
#     'Product': ['A', 'B', 'C', 'D', 'E'],
#     'Sales': [1200, 850, 950, 1100, 1300],
#     'Customers': [300, 400, 350, 450, 500]
# }
# df = pd.DataFrame(data)

# # Display Sample Data
# st.write("### Sales Data")
# st.write(df)

# # Slider for Sales Range
# sales_range = st.slider("Select Sales Range", 
#                         min_value=0, 
#                         max_value=1500, 
#                         value=(500, 1000))

# # Filter Data Based on Sales Range
# filtered_df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]
# st.write("### Filtered Data")
# st.write(filtered_df)

# # Selectbox for Product Choice
# product_choice = st.selectbox("Select Product", filtered_df['Product'].unique())

# # Text Input for User Name
# user_name = st.text_input("Enter your name")

# # Text Area for Feedback
# feedback = st.text_area("Enter your feedback")

# # Checkbox for Agreement
# agree = st.checkbox("I agree to the terms and conditions")

# # File Uploader for Uploading Files
# uploaded_file = st.file_uploader("Upload a relevant file")

# # Button to Submit Feedback
# if st.button("Submit Feedback"):
#     if agree:
#         st.write("### Submitted Feedback")
#         st.write(f"**Name:** {user_name}")
#         st.write(f"**Product:** {product_choice}")
#         st.write(f"**Sales Range:** {sales_range}")
#         st.write(f"**Feedback:** {feedback}")
#         if uploaded_file is not None:
#             st.write("File uploaded successfully!")
#     else:
#         st.write("You must agree to the terms and conditions to submit feedback.")

#Streamlit Form

# import streamlit as st
# import pandas as pd

# # Step 1: Generate Sample Data with 5 Items
# data = {'Product': ['A', 'B', 'C', 'D', 'E'],
#         'Sales': [1200, 850, 950, 1100, 1300],
#         'Customers': [300, 400, 350, 450, 500]}
# df = pd.DataFrame(data)

# # Step 2: Display the Sample Data at the Top
# st.write("### Sample Data")
# st.write(df)

# # Step 3: Create a Slider for Selecting a Sales Range
# sales_range = st.slider("Select Sales Range", min_value=0, max_value=1500, value=(500, 1000))

# # Step 4: Filter Products Based on Selected Sales Range
# filtered_df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]

# # Step 5: Create a Dropdown for Selecting a Product from Filtered Data
# product_choice = st.selectbox("Select Product", filtered_df['Product'].unique())

# # Step 6: Create a Form for Feedback Submission
# with st.form(key="feedback_form"):
#     product_id = st.text_input("Enter Product ID")
#     feedback = st.text_area("Enter your feedback")
#     submit_button = st.form_submit_button("Submit Feedback")

# # Step 7: Define a Callback Function to Submit Feedback
# def submit_feedback():
#     st.write("### Submitted Feedback")
#     st.write(f"**Product:** {product_choice}")
#     st.write(f"**Sales Range:** {sales_range}")
#     st.write(f"**Product ID:** {product_id}")
#     st.write(f"**Feedback:** {feedback}")

# # Step 8: Check if the Submit Button is Clicked
# if submit_button:
#     submit_feedback()

# business_app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# # Title of the app
# st.title("Business Data Dashboard")

# # Introduction text
# st.write("This dashboard helps visualize sales data over time.")

# # Sample data
# date_rng = pd.date_range(start='1/1/2023', end='12/31/2023', freq='M')
# df = pd.DataFrame(date_rng, columns=['date'])
# df['sales'] = np.random.randint(100, 500, size=(len(date_rng)))

# # Data visualization with Streamlit
# st.subheader("Monthly Sales Data")
# st.line_chart(df.set_index('date'))

# # Adding a slider for user input
# sales_threshold = st.slider("Sales threshold", 100, 500, 300)

# # Filtering and displaying data based on user input
# filtered_data = df[df['sales'] >= sales_threshold]
# st.write(f"Months with sales above {sales_threshold}")
# st.write(filtered_data)

# st.title("Hello")
# st.write("Hello")
# st.header("Hello")
# st.subheader("Hello")
# st.number_input("Hello",max_value=1000,min_value=0,value=5)
# input=st.selectbox("Hello",["Hi","Bye","Yo"])
# st.write(f"You have input: {input}")

# if st.button("Hi"):
#   st.write("Bye")
#   st.success("Hello")

# st.title("Retail Business Dashboard")
# st.header("Manager Input Section")
# st.write("Please enter the monthly sales target and select the region")
# Target=st.number_input("Enter Monthly Sales Target (in USD):", min_value=0, value=50000)
# Region=st.selectbox("Select Region:",["N","E","S","W"])
# if st.button("submit"):
#     st.write(f'''Target: {Target} 
#     Region: {Region}''')
#     if Target>100000:
#         st.write("You have set ambitious target!")
#     st.success("Data input complete")

st.title("Business Performance Dashboard")
st.write("Objective: Provide insights into revenue, customer feedback, and market trends.")
Revenue={"Q1":"1.2M",
        "Q2":"1.5M",
        "Q3":"1.3M"}
customer_insights=["good","ho","very good"]
col1,col2,col3=st.columns(3)
with col1:
  st.header("Q1")
  st.write("Revenue=1.2M")
with col2:
  st.header("Q2")
  st.write("Revenue=1.5M")
with col3:
  st.header("Q3")
  st.write("Revenue=1.3M")

tab1,tab2,tab3=st.tabs(["SD","CI","MT"])
with tab1:
  for quarter, revenues in Revenue.items():
    st.write(f"{quarter}:{revenues}")
with tab2:
  for idx, insights in enumerate(customer_insights):
    st.write(f"{idx+1}. {insights}")
with tab3:
  trend={"Ys":"a","No":"b","Bye":"c"}
  for words, trends in trend:
    st.write(f"{words} : {trends}")

with st.expander("More info"):
  st.write("hi")

placeholder=st.empty()

for i in range(5):
  placeholder.wrtie(f"Loading progress: {i+20}%")
  time.sleep(1)
st.write("Loading complete")
message=["Hi","Bye","Yo"]
for msg in message:
  placeholder.wrtie(f"{msg}")
  time.sleep(3)



quarter_option=st.selectbox("Please select the quater you want", ["Q1","Q2","Q3","Q4"])


