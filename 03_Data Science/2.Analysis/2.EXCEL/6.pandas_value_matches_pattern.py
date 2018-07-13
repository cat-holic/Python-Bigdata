import pandas
import re
import string

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/6p.output.xls"

data_frame = pandas.read_excel(input_file, 'january_2013')

data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pandas.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name="jan_13_output", index=False)
writer.save()