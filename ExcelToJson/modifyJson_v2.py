import json
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd

# @Desc : json 형태로 만든 데이터
def getModifyData():
    # 1-0. 엑셀파일 읽기
    filename = "ExcelName.xlsx"
    # 엑셀 Sheet명으로 찾아서 내용 가져오기
    df = pd.read_excel(filename, sheet_name="jsonType")
    # 받아온 내용을 json 형태로 변환
    jsonData = json.loads(df.to_json(orient='records'))
    return jsonData

# @Desc : LD 에서 만든 Master JSON Data
def getMasterJsonData():
    json_file_path2 = askopenfilename(filetypes=[("JSON Files", "*.json")],title=message2)
    with open(json_file_path2, 'r') as f:
        data = json.load(f)
    return data

# @Desc 파일을 가져온다
message2 = "기준 마스터 파일을 선택하세요 "
# Tk().withdraw()
root = Tk()
root.withdraw()

# file_path = fieldi


# Master Json Data
masterData = getMasterJsonData()

# 선택한 JSON 파일 읽기
modifyData = getModifyData()
idx = 0
for t in modifyData:
    for item in masterData[0]['objects']:
        print(t , ' ★ ' , item)
        
    if idx == 5: break;
        # if 'name' in item and item['text'] == t['name']:
        #     item.update(t['elements'])
idx += 1

# 수정된 JSON을 다른 이름으로 저장합니다.
# new_file_name = 'ExcelName'+ '_0'+ str(i) +'.json'
# with open(new_file_name, 'w') as file:
#     json.dump(masterData, file)
# inputYN = input("그만 진행하시려면 Y , 계속 진행하려면 N 을 입력하세요 : ")
# i+=1    