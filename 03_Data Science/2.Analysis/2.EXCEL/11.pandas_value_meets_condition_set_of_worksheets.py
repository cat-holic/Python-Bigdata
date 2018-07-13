import pandas

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/11p.output.xls"

my_sheets = [0, 1]
threshold = 1900.0

data_frame = pandas.read_excel(input_file, sheet_name=my_sheets, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 2000.0])
filtered_row = pandas.concat(row_output, axis=0, ignore_index=True)

writer = pandas.ExcelWriter(output_file)
filtered_row.to_excel(writer, sheet_name="set_of_worksheets", index=False)
writer.save()
