import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename


i = 2
inputYN='N'
message2 = "기준 마스터 파일을 선택하세요 "
Tk().withdraw()
json_file_path2 = askopenfilename(filetypes=[("JSON Files", "*.json")],title=message2)
while inputYN=='N':
    message = "변경하려고 하는 Json 파일을 선택하세요"
    Tk().withdraw()
    json_file_path = askopenfilename(filetypes=[("JSON Files", "*.json")],title=message)
    
    # 선택한 JSON 파일 읽기
    with open(json_file_path, 'r') as f:
        modifyData = json.load(f)
    with open(json_file_path2, 'r') as f:
        data = json.load(f)

    for t in modifyData:
        for item in data[0]['objects']:
            if 'name' in item and item['name'] == t['key']:
                item.update(t['elements'])

    # 수정된 JSON을 다른 이름으로 저장합니다.
    new_file_name = 'ExcelName'+ '_0'+ str(i) +'.json'
    with open(new_file_name, 'w') as file:
        json.dump(data, file)
    inputYN = input("그만 진행하시려면 Y , 계속 진행하려면 N 을 입력하세요 : ")
    i+=1    