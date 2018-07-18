import csv, MySQLdb
output_file = "output_files/output_file.cvs"

con = MySQLdb.connect(port=3307, db='my_suppliers', user='pytest', passwd="1234")
c = con.cursor()

filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

c.execute("""SELECT *
            FROM Suppliers
            WHERE Cost > 700.0""")

rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
