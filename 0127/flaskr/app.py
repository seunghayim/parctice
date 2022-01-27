from flask import Flask
from pakage.vaccadd import VaccPublicData

# 인스턴스 선언 및 app의 위치를 알리기 위해 __name__
app = Falsk(__name__)
# UTF-8 을 적용하기 위해
app.config['JSON_AS_ASCII'] = False

# 데코레이션
@app.route('/')
def flaskData():
    # 인스턴스 
    data1 = VaccPublicData(1,5,"중랑구")
    return data1.vaccUrl
