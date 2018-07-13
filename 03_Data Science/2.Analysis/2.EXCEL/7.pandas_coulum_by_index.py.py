import pandas
import re
import string

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/7p.output.xls"

data_frame = pandas.read_excel(input_file, 'january_2013')

data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

print(data_frame_column_by_index)
writer = pandas.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer, sheet_name="jan_13_output", index=False)
writer.save()