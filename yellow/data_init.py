import csv


dataPath = 'res/data/서울특별시_' #데이터 경로
gulist = ['강남구','강북구','관악구','동작마포서대문영등포','송파광진성동','양천구_구로구_금천구','1']
filetype = '.csv' #파일 형식
school_num=[2, 1, 0, 1, 1, 1, 1] #학교명이 들어가는 열
date=[4, 4, 2, 2, 2, 2, 2]
data= dict()
data_list = []
data_date = []
for i , gu in enumerate(gulist):# enumrate로 몇번째 행인지와 구 각각 불러오기

    file_name = dataPath + gu + filetype # 위에서 지정한 경로와 구 명, 파일형식합쳐서 파일위치 만들기
    with open(file_name, "r",encoding="cp949") as f:#파일열어서

        data = csv.reader(f)# csv리더로 csv 객체 생성
        for line in data:#csv객체 각 줄 불러서
            if(line[school_num[i]].find("초등학교")!=-1):
                #print(line[school_num[i]]+','+line[date[i]])
                data_list.append(line[school_num[i]])
                data_date.append(line[date[i]])
result = dict(zip(data_list, data_date))
print(result)