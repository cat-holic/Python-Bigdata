import csv
import MySQLdb
con = MySQLdb.connect(port=3307, db='my_suppliers', user='pytest', passwd="1234")
c = con.cursor()

# input_file = "supplier_data.csv"
# file_reader = csv.reader(open(input_file, 'r'), delimiter=",")
#
# header = next(file_reader)

c.execute("""DELETE FROM suppliers
            WHERE Cost < 500;""")
# c.fetchall()
# c.execute("SELECT * FROM suppliers;")
result = c.fetchall()
for row in result:
    print(row)
