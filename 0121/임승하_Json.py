from base64 import encode
import json, os

# 현제 경로 / 및 launch.json 파일의 절대 경로 
path = os.getcwd()
print(os.path.abspath('launch.json'))
# 왜 절대경로인데를 잘못 표시하는거지? .vscode 인식을 하지 않는 이유는?


# 기본적으로 문자열을 읽을 때나 저장할 경우 dumps, loads /// 파일을 읽거나 저장할 경우 dump, load
# json 파일의 주석문이 python 으로 변환시 주석문으로 인식하지 않아서, 발생하는 문제를 해결
with open(".vscode/launch.json", "r", encoding="utf-8") as fileName:
    tempFile = json.loads('\n'.join(row for row in fileName if not row.lstrip().startswith("//")))
    print(tempFile)

    # 이렇게 무식하게 해야하나... 방법이 없을까
    resultData2 = tempFile["configurations"][0]["name"]
    resultData1 = tempFile["configurations"][1]["name"]
    resultData3 = tempFile["configurations"][2]["name"]
    resultData2 = tempFile["configurations"][0]["type"]
    resultData1 = tempFile["configurations"][1]["type"]
    resultData3 = tempFile["configurations"][2]["type"]

# json 파일에 주석문이 없을 때    
with open("myData.json", "r", encoding="utf-8") as fileName:
    tempFile = json.load(fileName)
    print(tempFile)



# 예외 처리로 할경우 .. 
try:
    fileName = open(".vscode/launch.json", "r", encoding="utf-8")
    tempFile = json.loads('\n'.join(row for row in fileName if not row.lstrip().startswith("//")))
    print(tempFile)
except Exception as ex:
    error = str(ex)
else:
    fileName.close()

# 파일
data1 = {
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development"
      },
      "args": [
        "run",
        "--no-debugger"
      ],
      "jinja": True
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}\\project\\project\\manage.py",
      "args": [
        "runserver"
      ],
      "django": True
    }
  ]
}

# json 파일을 폴더로 저장
with open("myData.json", "w", encoding="utf-8") as fileName:
    tempFile = json.dump(data1, fileName, ensure_ascii=False, indent=4)

# 디버깅을 위한 임시 변수
temp = 0 
