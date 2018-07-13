import pandas

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/10p.output.xls"

data_frame = pandas.read_excel(input_file, sheet_name=None)
column_output = []
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
filtered_row = pandas.concat(column_output, axis=0, ignore_index=True)

writer = pandas.ExcelWriter(output_file)
filtered_row.to_excel(writer, sheet_name="elected_columns_all_worksheets", index=False)
writer.save()
