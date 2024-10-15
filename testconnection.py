import psycopg2

try:
    connection = psycopg2.connect("postgresql://shamilsd:database2024@localhost:5437/cloneitdb")
    print("Connection successful")
except Exception as e:
    print("Connection failed:", e)

