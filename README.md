# PHONEPE PULSE DATA VISUALIZATION AND EXPLORATION
Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly.
# Phonepe
Phonepe pulse is launched for getting accurate and comprehensive data on digital payment transaction trends in India. This webiste mostly shows more than 2000+ transactions done by the consumers on interactive map of India. Phonepe Pulse is India's first interactive geospatial platform on digital payments.
reference for phonepe pulse.

# Data
The data used in PhonePe Pulse is available in this link. The data is divided into different categories, such as transaction data, user data, and top data. The data is stored in JSON format. A complete description of the data is provided in the link below, before proceeding to data visualisation or data processing kindly understand the data completly.
data: https://github.com/PhonePe/pulse

# Required Skills:
1) Python scripting 
2) Github Cloning 
3) Pandas 
4) Streamlit 
5) Plotly

# Cloning

To clone the Phonepe Pulse Github repository and store its data in a CSV or JSON format:
Clone the Phonepe Pulse Github repository using the following command:

```
!git clone https://github.com/phonepe/pulse.git
```
# PhonePe Pulse Dashboard
In this dashboard we are using the data that we extracted from the state-wise json files in the repository which are uploaded into MySQL database. Then using the data downloded from SQL database the geo visualization is created.

# Importing Libraries
Before proceeding further importing the necessary libraries in important. In this dash board we use streamlit, plotly to visualize our data.

```
import pandas as pd
import json
import os
import numpy as np
import streamlit as st
import mysql.connector
import plotly.express as px
```
# Connecting to Database
Next we coonect to the database were we stored our six dataframes which are transformed in a way to best suit for the visualization.

```
# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    auth_plugin='mysql_native_password'
)
```
Create a cursor object to execute SQL commands
cursor = cnx.cursor()


# Streamlit Programe
In here use your own imagination and create your dashboard using stremlit, If you look at my dashbord function block it has various charts and dataframe displayed using plotly graph. likewise you could also try to visualize in more beeter and efficient way.

# You can now view your Streamlit app in your browser.
'''Local URL: http://localhost:8501 Network URL: http://192.168.0.102:8501'''

# Conclusion
The final product of this project is the live geo visualization dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner.

