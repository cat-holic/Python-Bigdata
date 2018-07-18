import glob, os
import pandas

input_folder = "input_files/"
output_file = "output_files/13.p_output.xls"

all_workbooks = glob.glob(os.path.join(input_folder,'*.xls*'))
data_frames = []
for workbook in all_workbooks:
    all_worksheets = pandas.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheets.items():
        data_frames.append(data)
all_data_concatenated = pandas.concat(data_frames, axis=0, ignore_index=True)

writer = pandas.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name="all_data_all_workbooks", index=False)
writer.save()