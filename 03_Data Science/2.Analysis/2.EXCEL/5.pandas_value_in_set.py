import pandas
import string

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/5p.output.xls"

data_frame = pandas.read_excel(input_file, 'january_2013')

important_dataes = ['01/24/2013', '01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dataes)]

writer = pandas.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer,sheet_name="jan_13_output",index=False)
writer.save()
