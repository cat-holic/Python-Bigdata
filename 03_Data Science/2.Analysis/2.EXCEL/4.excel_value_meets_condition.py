#목적 : 특정조건을 충족하는 행의 필터링


from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/4e.output.xls"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("jan_2013_output")

sale_amout_coulumn_index = 3
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name("january_2013")
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        sale_amout = worksheet.cell_value(row_index, sale_amout_coulumn_index)
        if sale_amout > 1400.0:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, elemnt in enumerate(output_list):
            output_worksheet.write(list_index, element_index, elemnt)

output_workbook.save(output_file)