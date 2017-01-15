import win32com.client
import os
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

print(os.getcwd())
wb = excel.Workbooks.Open(os.getcwd()+'\\input.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()