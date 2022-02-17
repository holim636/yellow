import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import csv
import os

font_path = "../yellow/res/font/NanumGothic.ttf"
PATH = "../yellow/res/data/"
dat1 = '도로교통공단_어린이 교통사고 현황_20191231.csv'
dat2 = '도로교통공단_어린이 사망교통사고 정보_20191231.csv'
dat3 = 'yellow.json'
mpl.rcParams['font.family'] = 'NanumGothic'
mpl.rcParams['font.size'] = 10

def load_data(path=PATH, name =''):
    csv_path = os.path.join(path, name)
    return pd.read_csv(csv_path,engine='python',encoding='cp949')
def load_data_json(path=PATH, name = ''):
    json_path = os.path.join(path,name)
    data = dict()
    with open(json_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return pd.DataFrame(data['yellow'])

def plot_data(name = '',year = ''):#지역 현황 그래프
    #a = load_data(name= dat1)
    b = load_data(name= dat2)
    new_b = b[b['발생지시도']=='서울']
    new_b = new_b[new_b['사고유형_대분류']=='차대사람']
    if name != '':
        new_b = new_b[b['발생지시군구']==name]
    c = load_data_json(name=dat3)
    if name !='':
        c = c[c['juso'].str.contains(name)]
    c['lat'] = pd.to_numeric(c['lat'])
    c['lon'] = pd.to_numeric(c['lon'])
    plt.figure()
    plt.scatter(new_b['경도'],new_b['위도'],color='red',alpha=.1)
    plt.scatter(c['lon'],c['lat'],color='yellow')
    plt.xlabel('경도')
    plt.ylabel('위도')
    print(c)
    plt.show()

def ac_plot_data(name = ''): #사고 통계 그래프
    #a = load_data(name= dat1)
    b = load_data(name= dat2)
    new_b = b[b['발생지시도']=='서울']
    new_b = new_b[new_b['사고유형_대분류']=='차대사람']
    if name != '':
        new_b = new_b[b['발생지시군구'] == name]
    new_b['발생년'] = pd.to_numeric(new_b['발생년'])
    p = new_b['발생년'].value_counts()
    #order = [2015,2016,2017,2018,2019]
    #p = p.loc[order]
    p.plot.bar()
    plt.xlabel('year')
    plt.ylabel('')
    plt.show()

def detail_plot_data(name = ''): #연도별 사상자 수 그래프
    #a = load_data(name= dat1)
    b = load_data(name= dat2)
    new_b = b[b['발생지시도']=='서울']
    new_b = new_b[new_b['사고유형_대분류']=='차대사람']
    if name != '':
        new_b = new_b[b['발생지시군구'] == name]
    new_b['발생년'] = pd.to_numeric(new_b['발생년'])
    new_b['사망자수'] = pd.to_numeric(new_b['사망자수'])
    new_b['부상자수'] = pd.to_numeric(new_b['부상자수'])
    new_b['중상자수'] = pd.to_numeric(new_b['중상자수'])
    new_b['경상자수'] = pd.to_numeric(new_b['경상자수'])
    new_b['부상신고자수'] = pd.to_numeric(new_b['부상신고자수'])
    p = new_b.groupby('발생년').sum()
    p = p.loc[:,['사망자수','부상자수','중상자수','경상자수','부상신고자수']]
    order = [2015,2016,2017,2018,2019]
    print(p)
    p = p.loc[order]
    p.plot.bar()
    plt.xlabel('year')
    plt.ylabel('')
    plt.show()

def ac_plot_data_2(name = ''): #사고 현황 그래프
    a = load_data(name= dat1)
    #b = load_data(name= dat2)
    new_a = a[a['발생지_시도']=='서울']
    new_a = new_a[new_a['사고유형_대분류']=='차대사람']
    if name != '':
        new_a = new_a[a['발생지_시군구'] == name]
    new_a['발생일'] = pd.to_datetime(new_a['발생일'])
    new_a['year'] = new_a['발생일'].dt.year
    #new_a['year'] = pd.to_numeric(new_a['year'])
    p = new_a['year'].value_counts()
    order = [2015,2016,2017,2018,2019]
    p = p.loc[order]
    print(p)
    p.plot.bar()
    plt.xlabel('year')
    plt.ylabel('')
    plt.show()


#여기서 구 이름만 입력해주면 됩니다
plot_data(name='')
