import json, requests

class VaccPublicData():
    def __init__(self, startNum, endNum, address):
        self.startNum = startNum
        self.endNum = endNum
        self.address = address
    
    
    def VaccUrl(self):
        keyValue = r"V6lQYKtQODdLI8HPFUM%2FF1fi2FGeE%2FbXr142ghKq1Vfzozi42DXMWVzP9Hp9GI%2FI%2F1%2BbUud5Pa4JVwsu653Y8Q%3D%3D"
        dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
        dataURL += f"page={str(self.startNum)}&perPage={str(self.endNum)}"
        dataURL += f"&cond%5BorgZipaddr%3A%3ALIKE%5D={self.address}"
        dataURL += f"&serviceKey={keyValue}"
        temp = requests.get(dataURL).text
        return json.loads(temp)
