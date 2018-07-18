import sqlite3
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
delete_table = """DELETE FROM Suppliers
                WHERE Supplier_Name = 'Supplier Z'"""
c.execute(delete_table)
con.commit()

cursor = con.cursor()
cursor = con.execute("SELECT * FROM Suppliers")
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)