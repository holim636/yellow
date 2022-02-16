import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os


PATH = "../yellow/res/data/"
dat1 = '도로교통공단_어린이 교통사고 현황_20191231.csv'
dat2 = '도로교통공단_어린이 사망교통사고 정보_20191231.csv'
dat3 = 'yellow.json'

def load_data(path=PATH, name =''):
    csv_path = os.path.join(path, name)
    return pd.read_csv(csv_path,engine='python',encoding='cp949')
def load_data_json(path=PATH, name = ''):
    json_path = os.path.join(path,name)
    data = dict()
    with open(json_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return pd.DataFrame(data['yellow'])

def plot_data(name = ''):
    a = load_data(name= dat1)
    b = load_data(name= dat2)
    new_b = b[b['발생지시도']=='서울']
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
#여기서 구 이름만 입력해주면 됩니다
plot_data(name='동대문구')
