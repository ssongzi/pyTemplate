import pandas as pd
# from openpyxl import load_workbook
import json

# 1-0. 엑셀파일 읽기
filename = "ExcelName.xlsx"

# Dataframe형식으로 엑셀 파일 읽기
df = pd.read_excel(filename, sheet_name="jsonType")

# 데이터 프레임 출력
# print(df)
# jsonDt = df.to_json(orient='records')

# jsonDt = jsonDt.replace("\n", "\\n")
# jsonDt = jsonDt.replace('\', "")
json_obj = json.loads(df.to_json(orient='records'))
print(json_obj)