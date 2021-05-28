import sqlite3
import json
from sqlite3 import Error

json_query = lambda rows: json.dumps([list(row) for row in rows])

def create_connection(db_file="stations.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def query_stations(conn, line_id=None):
    cur = conn.cursor()
    if not line_id:
        cur.execute("SELECT * FROM t")
    else:
        cur.execute("SELECT * FROM t WHERE LINES=?",(line_id,))

    rows = cur.fetchall()
    return json_query(rows)

def query_lines(conn):
    pass