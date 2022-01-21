#전체평균 /전체 총점 - 개인평균 / 개인총점 구하는 class
class MeanCalc:
    def __init__(self, data):
        self.data = data

    
    # 개인 평균 / 개인 총점 구하는 메서드
    def personalMean(self, name):
        score = sum(self.data[name][0].values())
        mean =  score / len(self.data[name][0])
        return f'이름:{name}, 총점:{score}, 평균:{mean:.1f}'
        

    # 전체 평균 / 전체 총점 구하는 메서드
    def totalMean(self):
        totalScore = 0
        totalNum = 0
        for k in grade.keys():
            totalScore += sum(self.data[k][0].values())
            totalNum += len(self.data[k][0])
        return f'반 총점:{totalScore}, 전체 평균:{totalScore / totalNum:.1f}'     
        

# test
if __name__ == '__main__':
    # 점수 자료
    grade = {
        'hong1': [{'국어': 95, '영어': 90, '수학': 80, '과학': 50,}],
        'hong2': [{'국어': 100, '영어': 50, '수학': 90, '과학': 90,}],
        'hong3': [{'국어': 99, '영어': 60, '수학': 100, '과학': 40,}],
        'hong4': [{'국어': 55, '영어': 80, '수학': 80, '과학': 60,}],
        'hong5': [{'국어': 30, '영어': 17, '수학': 98, '과학': 99,}],
        'hong6': [{'국어': 58, '영어': 100, '수학': 8, '과학': 23,}],
    }        

    # class를 인스턴스한 객체 result  (변수->자료)
    result = MeanCalc(grade)

    # personalMean 메서드를 이용해 개인 평균 / 개인 총점 구하기 (변수->이름)
    data1 = result.personalMean('hong1')
    data2 = result.personalMean('hong2')
    data3 = result.personalMean('hong3')
    data4 = result.personalMean('hong4')
    data5 = result.personalMean('hong5')
    data6 = result.personalMean('hong6')

    # totalMean 메서드를 이용하여 전체 평균 / 전체 총점 구하기
    data7 = result.totalMean()

    # 디버깅을 위한 임시변수
    temp = 0
