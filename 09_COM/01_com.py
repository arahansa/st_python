import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.Visible = 1

print("word..?")
