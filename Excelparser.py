import pandas as pd

df = pd.read_excel('C:\Рога и копыта_январь 2018.xlsx', sheet_name='лист', header=None, index_col=None)
print(df)

xls = pd.ExcelFile('C:\Рога и копыта_январь 2018.xlsx')

sheetX = xls.parse('лист')

var1 = sheetX
print(var1)


from openpyxl import load_workbook
wb=load_workbook(filename='C:\Рога и копыта_январь 2018.xlsx')
sheet_ranges=wb['лист']
print(sheet_ranges['D20']. value)

import xlrd

file_location='C:\Рога и копыта_январь 2018.xlsx'
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
print(sheet.cell_value(0,0))

class CashFlow(object):
    def __init__(self,):
