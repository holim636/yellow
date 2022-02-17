import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import json


def getCasualties():
    data = pd.read_csv('../yellow/res/data/도로교통공단_어린이 교통사고 현황_20191231.csv', encoding="cp949")
    df = pd.DataFrame(data)

    # 표시할 df 열
    df1 = df[['발생일', '사망자수', '중상자수', '경상자수', '부상신고자수', '발생지_시도', '발생지_시군구', '피해자_당사자종별', '주야']]
    df2 = df1.loc[df['피해자_당사자종별'] == '보행자']        # 피해자_당사자종별 중 보행자만
    df3 = df2.loc[df['발생지_시도'] == '서울']              # 발생지_시도 중 서울만
    # df3 = df2_2.loc[df['주야'] == '주']

    # 강남의 ~~구들
    gangnam = ['양천구', '구로구', '영등포구', '금천구', '동작구', '관악구', '강남구', '송파구']
    dates = ['2015', '2016', '2017', '2018', '2019']      # 연도별 데이터터

    gangnam_casualties = dict()
    guDict = dict()

    for gu in gangnam:
        df_1 = df3.loc[df['발생지_시군구'] == gu]           # 시군구가 gu인 df
        df_1 = df_1.set_index(['발생일'])                  # 발생일을 index로
        yearDict = dict()


        for date in dates:        # date가 2015라면 2015-01-01부터 2015-12-31까지의 df를 가지고 옴
            df_1_1 = df_1.loc[f'{date}-01-01':f'{date}-12-31']
            yearDict[date] = int(len(df_1_1.index))

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

    # 강남의 각 연도별 사고 횟수 합계
    for year in yearList:
        sum = 0
        for gu in guList:
            sum = sum + gugun[gu][year]

        accident.append(sum)

    # print(accident)
    x = np.arange(5)                # x축이 5개
    plt.bar(x, accident)            # y축이 연도별 총 사고 횟수
    plt.ylim(0, 400)  # y축이 0부터 100까지
    plt.xticks(x, yearList)         # x축이 각각의 연도

    # plt.show()

    # plt를 이미지로 저장  /   경로지정 현제 pd_df.py기준으로 상대경로를 작성하면 됩니다.
    plt.savefig('gangnamTotal.png')     # yellow 폴더에 png를 저장하고 싶다면 ../그림.png 라고 저장하면 됨
    plt.clf()           # plt 초기화

def plotGraph(gu):
    with open(jsonData1, 'r', encoding='utf_8') as f:
        gangnam = json.load(f)

    with open(jsonData2, 'r', encoding='utf_8') as f:
        accident = json.load(f)

    gugun = gangnam['강남']
    gugun1 = accident['강남']
    yearList = ['2015', '2016', '2017', '2018', '2019']
    accident = list()
    accident1 = list()
    persent = list()

    # 선택한 구의 연도별 사고 현황을 accident라는 list에 저장
    for year in yearList:
        accident.append(gugun[gu][year])
        accident1.append(gugun1[gu][year])
        a = round(float(gugun1[gu][year]/gugun[gu][year])*100, 2)
        persent.append(a)

    print(accident, accident1, persent)
    with plt.rc_context({'axes.edgecolor':'lightgray'}):
        fig, ax = plt.subplots()
        ax.plot(yearList, accident, color='#ffd400', marker='o', label='사상자')
        ax.plot(yearList, accident1, color='#ff7b5a', marker='o', label='사망자')
        ax.plot(yearList, persent, color='#1e90ff', marker='v', label='사망률[%]')
        plt.grid(axis='y')

        plt.yticks(list(range(0, 100, 10)))
        plt.legend(loc=1)
        plt.title(gu)

    # plt 파일로 저장
    plt.savefig(f'{gu}.png')
    plt.clf()                       # plt 초기화


if __name__ == '__main__':
    gangnam = getCasualties()
    # print(gangnam)

    barGraph(gangnam)

    plotGraph(gangnam, '강남구')

