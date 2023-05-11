import pandas as pd
import mysql.connector

# Read the Excel file into a DataFrame
df_Map_T = pd.read_excel("df_Map_Transaction.xlsx")
df_Map_U = pd.read_excel("df_map_user.xlsx")
df_Agg_T = pd.read_excel("df_Agg_Transaction.xlsx")
df_Agg_U = pd.read_excel("df_Agg_User.xlsx")
df_Top_T = pd.read_excel("df_Top_Transaction.xlsx")
df_Top_U = pd.read_excel("df_Top_user.xlsx")

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the database for all the 6 tables
cursor.execute("CREATE DATABASE IF NOT EXISTS map_transaction")
cursor.execute("CREATE DATABASE IF NOT EXISTS mapp_user")
cursor.execute("CREATE DATABASE IF NOT EXISTS Agg_Transaction")
cursor.execute("CREATE DATABASE IF NOT EXISTS Agg_User")
cursor.execute("CREATE DATABASE IF NOT EXISTS Top_Transaction")
cursor.execute("CREATE DATABASE IF NOT EXISTS Top_user")

# Close the cursor and the connection
cursor.close()
cnx.close()

# Connect to the newly created database for map Transaction
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="map_transaction",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS df_Map_T (
  sno INT AUTO_INCREMENT PRIMARY KEY,
  count INT,
  amount FLOAT,
  name VARCHAR(255),
  year INT,
  quarter VARCHAR(255)
)
""")

cnx.commit()
# Insert data into the table
for i, row in df_Map_T.iterrows():
    cursor.execute("""
    SELECT sno FROM df_Map_T WHERE sno = %s
    """, (row["sno"],))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("""
        INSERT INTO df_Map_T (sno, count, amount, name, year, quarter)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (row["sno"], row["count"], row["amount"], row["name"], row["year"], row["quarter"]))


# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()
###########################################################################################################

# Connect to the newly created database for map user
# appopens divided by 10000
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="mapp_user",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS df_Map_U (
  sno INT AUTO_INCREMENT PRIMARY KEY,
  state VARCHAR(255),
  registeredUsers INT,
  appOpens BIGINT,
  year INT,
  quarter VARCHAR(255)
)
""")

cnx.commit()
# Insert data into the table
for i, row in df_Map_U.iterrows():
    cursor.execute("""
    SELECT sno FROM df_Map_U WHERE sno = %s
    """, (row["sno"],))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("""
        INSERT INTO df_Map_U (sno, state, registeredUsers, appOpens, year, quarter)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (row["sno"], row["state"], row["registeredUsers"], row["appOpens"], row["year"], row["quarter"]))


# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

######################################################################################################################

# Connect to the newly created database for Agg Transaction
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Agg_Transaction",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS df_Agg_T (
  sno INT AUTO_INCREMENT PRIMARY KEY,
  count BIGINT,
  amount FLOAT,
  name VARCHAR(255),
  year INT,
  quarter VARCHAR(255)
)
""")

cnx.commit()
# Insert data into the table
for i, row in df_Agg_T.iterrows():
    cursor.execute("""
    SELECT sno FROM df_Agg_T WHERE sno = %s
    """, (row["sno"],))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("""
        INSERT INTO df_Agg_T (sno, count, amount, name, year, quarter)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (row["sno"], row["count"], row["amount"], row["name"], row["year"], row["quarter"]))


# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

###################################################################################################################

# Connect to the newly created database for Agg user
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Agg_User",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS df_Agg_U (
  sno INT AUTO_INCREMENT PRIMARY KEY,
  brand VARCHAR(255),
  count INT,
  percentage FLOAT,
  year INT,
  quarter VARCHAR(255)
)
""")

cnx.commit()
# Insert data into the table
for i, row in df_Agg_U.iterrows():
    cursor.execute("""
    SELECT sno FROM df_Agg_U WHERE sno = %s
    """, (row["sno"],))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("""
        INSERT INTO df_Agg_U (sno, brand, count, percentage, year, quarter)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (row["sno"], row["brand"], row["count"], row["percentage"], row["year"], row["quarter"]))


# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

####################################################################################################################

# Connect to the newly created database for Top Transaction
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Top_Transaction",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS df_Top_T (
  sno INT AUTO_INCREMENT PRIMARY KEY,
  entityName VARCHAR(255),
  count INT,
  amount BIGINT,
  year INT,
  quarter VARCHAR(255)
)
""")

cnx.commit()
# Insert data into the table
for i, row in df_Top_T.iterrows():
    cursor.execute("""
    SELECT sno FROM df_Top_T WHERE sno = %s
    """, (row["sno"],))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("""
        INSERT INTO df_Top_T (sno, entityName, count, amount, year, quarter)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (row["sno"], row["entityName"], row["count"], row["amount"], row["year"], row["quarter"]))


# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

####################################################################################################################

# Connect to the newly created database for Top user
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowsika1998*",
    database="Top_User",
    auth_plugin='mysql_native_password'
)

# Create a cursor object to execute SQL commands
cursor = cnx.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS df_Top_U (
  sno INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  registeredUsers INT,
  year INT,
  quarter VARCHAR(255)
)
""")

cnx.commit()
# Insert data into the table
for i, row in df_Top_U.iterrows():
    cursor.execute("""
    SELECT sno FROM df_Top_U WHERE sno = %s
    """, (row["sno"],))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("""
        INSERT INTO df_Top_U (sno, name, registeredUsers, year, quarter)
        VALUES (%s, %s, %s, %s, %s)
        """, (row["sno"], row["name"], row["registeredUsers"],row["year"], row["quarter"]))


# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

############################################ End ###################################################################
