
import pandas as pd

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/3p.output.xls"

# data_frame = pd.read_excel(input_file, sheetname='januar_2013')
# sheetname은 defrecate 되었음
data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer,sheet_name="jan_13_output", index=False)
writer.save()