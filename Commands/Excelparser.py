import pandas as pd
import glob

folder = r'C:\example'
files = glob.glob('C:\example\**\*.xlsx', recursive=True)

df = pd.DataFrame()

for num, fname in enumerate(files, start = 1):
    print("File # {} | {}".format(num, fname))
    if len(fname) > 0:
        data = pd.read_excel(fname, sheet_name=0, header=0, index_col=0, usecols="B:I", skiprows=10)
        df = data.append(data)

df.head()
df.to_excel('C:\example\example.xlsx')


# for f in files_list:
#     df = pd.read_excel(folder, sheet_name=0, header=0, index_col=0, usecols="B:I", skiprows=10)
# print(df)

# files = [os.path.join(folder, "*.xlsx") for f in folder]
# all_file_frame = []
# for f in files:
#     # print('Reading %s'%f)
#     # data = pd.read_excel(r'C:\example\Рога и копыта_январь 2018.xlsx', sheet_name=0, header=0, index_col=0, usecols="B:I",
#     #                      skiprows=10)
#     data = pd.read_excel(f, sheet_name=0, header=0, index_col=0, usecols="B:I", skiprows=10)
#     all_file_frame.append(data)
# all_frame = pd.concat(all_file_frame, axis=0)
# all_frame.to_excel("C:\example\example1.xlsx")


# path = r' C:\example\ '
# filenames = glob.glob(path + '/*.xlsx')

# data = pd.read_excel(r'C:\example\Рога и копыта_январь 2018.xlsx', sheet_name=0, header=0, index_col=0, usecols="B:I",
#                      skiprows=10)
# df = pd.DataFrame(data=data)
# df.to_excel("C:\example\example.xlsx")
# print(df)

# import pandas as pd
#
# xl_file = pd.ExcelFile('C:\Рога и копыта_январь 2018.xlsx')
# dfs = {sheet_name: xl_file.parse(sheet_name)
#           for sheet_name in xl_file.sheet_names}
# print(dfs)

# xls = pd.ExcelFile('C:\Рога и копыта_январь 2018.xlsx')
#
# sheetX = xls.parse('лист')
#
# var1 = sheetX
# print(var1)
#
#
# from openpyxl import load_workbook
# wb=load_workbook(filename='C:\Рога и копыта_январь 2018.xlsx')
# sheet_ranges=wb['лист']
# print(sheet_ranges['D20']. value)
#
#
# from openpyxl import load_workbook
# wb=load_workbook(filename='C:\Рога и копыта_январь 2018.xlsx')
# sheet_ranges=wb['лист']
# print(sheet_ranges['D20']. value)


#
# import xlrd
# file_location = 'C:\Рога и копыта_январь 2018.xlsx'
# workbook=xlrd.open_workbook(file_location)
# sheet=workbook.sheet_by_index(0)
# values = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#
# print(values)

# from openpyxl import load_workbook
# wb=load_workbook(filename='C:\Рога и копыта_январь 2018.xlsx')
# sheet_ranges=wb['лист']
# print(sheet_ranges['D20']. value)
#
# excel_data_file = xlrd.open_workbook("C:\Рога и копыта_январь 2018.xlsx")
# sheet = excel_data_file.sheet_by_index(0)
#
# cash_flow_information = []
# row_number = sheet.nrows
#
# if row_number > 0:
#     for row in range(0,row_number):
#         cash_flow_information.append(str(sheet.row(row)[1]))
#         print(len(cash_flow_information))
#
#     else:
#         print("косорукое заполнение файла")
#
# print('\n'.join(cash_flow_information))
#
# import pandas as pd
#
# df = pd.read_excel("C:\Рога и копыта_январь 2018.xlsx", sheet_name=0)
# print(df)
#
# xls = pd.ExcelFile('C:\Рога и копыта_январь 2018.xlsx')
#
# sheetX = xls.parse('лист')
#
# var1 = sheetX
# print(var1)
#
#
# from openpyxl import load_workbook
# wb=load_workbook(filename='C:\Рога и копыта_январь 2018.xlsx')
# sheet_ranges=wb['лист']
# print(sheet_ranges['D20']. value)
#
# import xlrd
#
# file_location='C:\Рога и копыта_январь 2018.xlsx'
# workbook=xlrd.open_workbook(file_location)
# sheet=workbook.sheet_by_index(0)
# print(sheet.cell_value(0,0))
#
# class CashFlow(object):
#     def __init__(self,):

# import xlrd
#
# rb = xlrd.open_workbook('C:\Рога и копыта_январь 2018.xlsx')
# sheet = rb.sheet_by_index(0)
# for rownum in range(sheet.nrows):
#     row = sheet.row_values(rownum)
#     c_row = []
#     for c_el in row:
#         c_row.append(c_el)
#
# print(sheet)
