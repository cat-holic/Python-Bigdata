# 목적 : 테이블에 새 레코드셋 삽입하기

import csv
import sqlite3

# Path to and name of a CSV input file

input_file = "csv_files/supplier_data.csv"

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers(
                    Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date);"""
c.execute(create_table)

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)  # Header 건너뛰고 data만 접근 하기 위함
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?,?,?,?,?);", data)
con.commit()
print("데이터 베이스 삽입 완료 \n\n")
# Query the Suppliers table
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)