# 목적 : 데이터 베이스를 메모리에 생성시 휘발성데이터임을 확인
import csv
import sqlite3

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)
