import pandas

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/4p.output.xls"

dataframe = pandas.read_excel(input_file, 'january_2013')
print(dataframe)
print(dataframe['Sale Amount'] > 10)
dataframe_value_meets_condition = dataframe[dataframe['Sale Amount'].astype(float) > 1400.0]

writer = pandas.ExcelWriter(output_file)
dataframe_value_meets_condition.to_excel(writer, sheet_name="january_2013_output")
writer.save()
writer.close()

