import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

def getCasualties():
    data = pd.read_csv('../yellow/res/data/도로교통공단_어린이 교통사고 현황_20191231.csv', encoding="cp949")
    df = pd.DataFrame(data)

    df1 = df[['발생일', '사망자수', '중상자수', '경상자수', '부상신고자수', '발생지_시도', '발생지_시군구', '피해자_당사자종별']]
    df2 = df1.loc[df['피해자_당사자종별'] == '보행자']
    df3 = df2.loc[df['발생지_시도'] == '서울']
    gangnam = ['양천구', '구로구', '영등포구', '금천구', '동작구', '관악구', '강남구', '송파구']
    dates = ['2015', '2016', '2017', '2018', '2019']

    gangnam_casualties = dict()
    guDict = dict()
    guList = list()

    for gu in gangnam:
        df_1 = df3.loc[df['발생지_시군구'] == gu]
        df_1 = df_1.set_index(['발생일'])
        yearDict = dict()


        for date in dates:
            df_1_1 = df_1.loc[f'{date}-01-01':f'{date}-12-31']

            yearDict[date] = len(df_1_1.index)

        guDict[gu] = yearDict

    gangnam_casualties['강남'] = guDict
    return gangnam_casualties

    # total_stores_json = json.dumps(gangnam_casualties, ensure_ascii=False)
    # with open('gangnam_casualties.json', 'w', encoding='utf_8') as f:
    #     f.write(total_stores_json)

def barGraph(gangnam):
    gugun = gangnam['강남']
    guList = ['양천구', '구로구', '영등포구', '금천구', '동작구', '관악구', '강남구', '송파구']
    yearList = ['2015', '2016', '2017', '2018', '2019']
    accident = list()

    for year in yearList:
        sum = 0
        for gu in guList:
            sum = sum + gugun[gu][year]

        accident.append(sum)

    print(accident)






if __name__ == '__main__':
    gangnam = getCasualties()
    print(gangnam)

    barGraph(gangnam)

