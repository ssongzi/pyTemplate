import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askopenfile
import pandas as pd

# Function Area [START] ==========================================================================
# Validation Check 할 변수
# "" : FALSE / "ABC~~" : TRUE
def fnIsSuccess(str):
    if str: return "Y"
    else: return "N"
    
# Json 파일을 읽기 [1 : json 파일 (단건) / 2 : Excel 파일 (여러건)]
def fnOpenJsonFile(filePath):
    with open(filePath, 'r') as f:
        modifyData = json.load(f)
    return modifyData

# Excel 파일을 읽기
def fnOpenExcelFile(filePath):
    sheetNm = input("시트명을 입력해주세요. (기본 : Sheet + 숫자 일 경우 숫자, 모든 시트일 경우 A 입력)")
    
    if sheetNm == '1': sheetNm = 'Sheet1'
    if sheetNm.upper() == 'A': sheetNm = 'A'

    excelData = pd.read_excel(filePath, sheet_name=sheetNm)
    modifyData = json.loads(excelData.to_json(orient='records'))
    return modifyData

# 읽어온 Json 파일에 맞게 마스터 json 파일 수정
def fnModifyDataByJson(modifyData):
    for t in modifyData:
        for item in modifyData[0]['objects']:
            if 'name' in item and item['name'] == t['key']:
                item.update(t['elements'])

    # 수정된 JSON을 다른 이름으로 저장합니다.
    fileSaveMsg = "파일명을 입력해주세요."
    fileName = asksaveasfilename(filetypes=[("JSON Files", "*.json")],title=fileSaveMsg)
    # new_file_name = 'L123'+ '_0'+ str(i) +'.json'
    with open(fileName, 'w') as file:
        json.dump(modifyData, file)
# Function Area   [END] ==========================================================================

# 기준파일을 가져온다
masterFileMsg = "기준 마스터 파일을 선택하세요 "
masterFilePath = askopenfilename(filetypes=[("JSON Files", "*.json")],title=masterFileMsg)

# 단일 정보인지 여러건인지 Validate
if fnIsSuccess(masterFilePath):
    modifyType = input("수정하실 타입을 선택하세요. [단일건 : 1 / 여러건 : 2]")
    isSuccess = fnIsSuccess(modifyType)

# 변경할 내용이 담긴 파일을 가져온다.
# 1 : json 파일 (단건)
# 2 : Excel 파일 (여러건)
chooseFileMsg = "파일을 선택하세요 "
if modifyType == '1': 
    chooseFilePath = askopenfilename(filetypes=[("JSON Files", "*.json")],title=chooseFileMsg)
    if fnIsSuccess(chooseFilePath) : 
        modifyData = fnOpenJsonFile(chooseFilePath)
elif modifyType == '2': # Excel 대량등록
    chooseFilePath = askopenfilename(filetypes=[("JSON Files", "*.xlsx;*.xls")],title=chooseFileMsg)
    if fnIsSuccess(chooseFilePath) : 
        modifyData = fnOpenExcelFile(chooseFilePath)

# 최종 JSON 파일을 반환
fnModifyDataByJson(modifyData)

