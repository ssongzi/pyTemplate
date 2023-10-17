# import pandas as pd
from openpyxl import load_workbook
import json

# 1-0. 엑셀파일 읽기
filename = "ExcelName.xlsx"
book = load_workbook(filename, data_only=True)

# 1-1. 첫번째 시트를 가져온다
sheet = book.worksheets[0]

# Json 형식에 맞게 문자 변경함수


def replaceToJson(text):
    if text == None:
        return ""
    else:
        text = text.replace("\n", "\\n")
        text = text.replace('"', '\\"')
        return text


cols = ''

# print(sheet.rows.columns)

idx = 0
for row in sheet.rows:
    if idx == 0:
        cols = row[idx].column
    replaceToJson(row[idx].value)


print(cols)
