import csv
import copy

class schoolLoc:
    def __init__(self):
        self.schoolDict = dict()
        f = open('res/data/seoul_elementary.csv', 'r', encoding='cp949')
        readCsv = csv.reader(f)
        for line in readCsv:
            self.schoolDict[line[3]]=line[7]
        f.close()

    ## 함수 선언부
    def find(self, schoolName):
        if self.schoolDict.get(schoolName):
            return self.schoolDict[schoolName]
        else:
            return ('없음')

dataPath = 'res/data/서울특별시_' #데이터 경로
gulist = ['강남구','강북구','관악구','동작마포서대문영등포','송파광진성동','양천구_구로구_금천구','1']
filetype = '.csv' #파일 형식
school_num=[2, 1, 0, 1, 1, 1, 1] #학교명이 들어가는 열
date=[4, 4, 2, 2, 2, 2, 2]
data= dict()
data_list = []
data_date = []
buf = []
result = []
for i , gu in enumerate(gulist):# enumrate로 몇번째 행인지와 구 각각 불러오기

    file_name = dataPath + gu + filetype # 위에서 지정한 경로와 구 명, 파일형식합쳐서 파일위치 만들기
    with open(file_name, "r",encoding="cp949") as f:#파일열어서

        data = csv.reader(f)# csv리더로 csv 객체 생성
        for line in data:#csv객체 각 줄 불러서
            if(line[school_num[i]].find("초등학교")!=-1):
                #print(line[school_num[i]]+','+line[date[i]])
                data_list.append(line[school_num[i]])
                data_date.append(line[date[i]])
data_list, data_date
juso = schoolLoc()

for i, j in enumerate(data_list):
    buf.append(j)
    buf.append(data_date[i])
    buf.append(juso.find(j))
    result.append(copy.deepcopy(buf))
    buf.clear()
print(result)
