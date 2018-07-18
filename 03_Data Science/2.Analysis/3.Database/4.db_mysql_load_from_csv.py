import csv
import MySQLdb
from datetime import datetime, date

# Path where CSV input file
input_file = "csv_files/supplier_data.csv"

# Connect to a MySQL database
# con = MYSQLdb.connect(host='localhost', port=3306, db='my_suppliers',
# user='python_training', passwd="python_training')

# con = MYSQLdb.connect(host='localhost', port=3306, db='mysuppliers',
# user='root', password='1111')

con = MySQLdb.connect(port=3307, db='my_suppliers', user='pytest', passwd="1234")
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=",")
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(row)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]), "%m/%d/%y"))
            a_date = a_date.strftime('%y-%m-%d')
            data.append(a_date)
    print(data)
    c.execute("INSERT INTO Suppliers VALUES(%s,%s,%s,%s,%s);", data)
con.commit()
