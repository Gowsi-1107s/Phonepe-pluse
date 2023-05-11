import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import mysql.connector

# Define streamlit app and dashboard layout
st.set_page_config(layout='wide')
st.title("Phonepe Pulse Data Visualization and Exploration")
# Establish database connections
cnx_map_t = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="map_transaction",
    auth_plugin='mysql_native_password'
)
cnx_map_u = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="map_user",
    auth_plugin='mysql_native_password'
)
cnx_agg_t = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Agg_Transaction",
    auth_plugin='mysql_native_password'
)
cnx_agg_u = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Agg_User",
    auth_plugin='mysql_native_password'
)
cnx_top_t = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Top_Transaction",
    auth_plugin='mysql_native_password'
)
cnx_top_u = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Top_user",
    auth_plugin='mysql_native_password'
)

# Load data from databases into data frames
df_Map_T = pd.read_sql_query("SELECT * FROM df_Map_T", cnx_map_t)
df_Map_U = pd.read_sql_query("SELECT * FROM df_Map_U", cnx_map_u)
df_Agg_T = pd.read_sql_query("SELECT * FROM df_Agg_T", cnx_agg_t)
df_Agg_U = pd.read_sql_query("SELECT * FROM df_Agg_U", cnx_agg_u)
df_Top_T = pd.read_sql_query("SELECT * FROM df_Top_T", cnx_top_t)
df_Top_U = pd.read_sql_query("SELECT * FROM df_Top_U", cnx_top_u)

# Set up Streamlit app
st.title("My Dashboard")

# Define list of dropdown options for users to select
options = ['count', 'amount', 'state', 'registeredUsers', 'appOpens', 'brand', 'percentage', 'entityName', 'name']

# Define main dashboard area with plotly choropleth map and bar chart for each data frame
#st.header("Map Transaction")
#fig_map_t = px.choropleth(df_Map_T, locations='name', color='count', locationmode='India-states', scope="india")
#st.plotly_chart(fig_map_t)

#st.header("Map User")
#fig_map_u = px.choropleth(df_Map_U, locations='state', color='registeredUsers', locationmode='USA-states', scope="usa")
#st.plotly_chart(fig_map_u)

st.header("Agg Transaction")
fig_agg_t = px.bar(df_Agg_T, x='name', y='amount', color='year')
st.plotly_chart(fig_agg_t)

fig_agg_t = px.bar(df_Agg_T, x='name', y='count', color='year')
st.plotly_chart(fig_agg_t)

# Define the dropdown options
dropdown_options = ['count', 'amount']
#dropdown_options = ['year', 'quarter']

# Add a title to the page
st.title('Line Chart with Dropdown Example')

# Add a dropdown to select the data to display
selected_option = st.selectbox('Select Data to Display', dropdown_options)

# Filter the data based on the selected option
filtered_data = df_Agg_T[['year', 'quarter',selected_option]]
#filtered_data = df_Agg_T[[ selected_option,'count', 'amount']]

# Group the data by year and quarter
grouped_data = filtered_data.groupby(['year', 'quarter'], as_index=False).sum()

# Create the line chart using Plotly Express
fig = px.bar(grouped_data, x='year', y=selected_option, color='year')

# Display the chart
st.plotly_chart(fig)

st.header("Agg User")
fig_agg_u = px.bar(df_Agg_U, x='brand', y='count', color='quarter')
st.plotly_chart(fig_agg_u)

fig_agg_u = px.bar(df_Agg_U, x='brand', y='percentage', color='quarter')
st.plotly_chart(fig_agg_u)

st.header("Top Transaction")
fig_top_t = px.bar(df_Top_T, x='entityName', y='amount')
st.plotly_chart(fig_top_t)

fig_top_t = px.bar(df_Top_T, x='entityName', y='count')
st.plotly_chart(fig_top_t)

st.header("Top User")
fig_top_u = px.bar(df_Top_U, x='name', y='registeredUsers')
st.plotly_chart(fig_top_u)

fig_top_u = px.bar(df_Top_U, x='name', y='registeredUsers')
st.plotly_chart(fig_top_u)

st.header("Map Transaction")
fig_top_t = px.bar(df_Map_T, x='year', y='amount', color='quarter')
st.plotly_chart(fig_top_t)

fig_agg_t = px.bar(df_Agg_T, x='name', y='count', color='year')
st.plotly_chart(fig_agg_t)

st.header("Map User")
fig_map_u = px.bar(df_Map_U, x='state', y='registeredUsers')
st.plotly_chart(fig_map_u)

fig_map_u = px.bar(df_Map_U, x='state', y='appOpens')
st.plotly_chart(fig_map_u)
