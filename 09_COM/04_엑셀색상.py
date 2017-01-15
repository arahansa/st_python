import win32com.client
import os
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

print(os.getcwd())
wb = excel.Workbooks.Open(os.getcwd()+'\\input.xlsx')
ws = wb.ActiveSheet
ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10
