import csv, sqlite3

columns = ("FID","OBJECTID","NAME","EASTING","NORTHING","LINES","NETWORK","Zone","x","y")

column_string = "(" +  ", ".join(columns)  +")"

con = sqlite3.connect("stations.db")
cur = con.cursor()
cur.execute(f"CREATE TABLE IF NOT EXISTS t {column_string};") # use your column names here

with open('london_stations.csv','r') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [[i[col] for col in columns] for i in dr]

cur.executemany(f"INSERT INTO t {column_string} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()