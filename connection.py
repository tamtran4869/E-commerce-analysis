import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cmap
plt.style.use('ggplot')
import seaborn as sns
from plotly import graph_objects as go
import argparse
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd)
from get_df_visual import get_df_visual 

#Get arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--question', dest='question', type=str, help='Add question number from 0-19')
    parser.add_argument('--db', dest='db', type=str, help='Add database "name user password" to connect data from database', default= None)
    args = parser.parse_args()
    return args

# Get list of SQL output
def extract_data_from_db (db, query_path):
    # Parse database arguments
    lst = db.split(" ")
    db = lst[0]
    user = lst[1]
    password = lst[2]

    #Connect and run SQL query to get data
    with open(query_path) as f: # Get query from txt files
        lines = f.read().splitlines()
    Q =" ".join([i.strip('\t') for i in lines])
    try:
        connection = mysql.connector.connect(host='localhost',  #Connect to the db
                                            database=db,
                                            user= user,
                                            password= password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            sql_select_Query = Q   #Run SQL qeury
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, multi=True)
            records = cursor.fetchall()
            return records

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def main():
    args= parse_args()

    question = "Q"+args.question
    run_query_path = cwd + "/question/"+question+".txt"

    records = extract_data_from_db(args.db,run_query_path) # Get a list of sql output
    o = get_df_visual(records) # Create a getting df and visual class object

    # Print df and visual chart (if any)
    func = getattr(o,question) 
    func()

if __name__ == "__main__":
    main()
    


