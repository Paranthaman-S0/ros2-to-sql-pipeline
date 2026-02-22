import pandas as pd
import sqlite3

# read csv
df = pd.read_csv("turtle_pose.csv")

# connect database
conn = sqlite3.connect("turtle_data.db")

# load to sql table
df.to_sql("turtle_pose", conn, if_exists="replace", index=False)

conn.close()

print("Loaded turtle_pose.csv into turtle_data.db")
