import pandas as pd
from datetime import datetime

def read_data():
    #df = pd.read_csv('final1.txt', index_col='TravelDate')
    df = pd.read_csv('3.txt', index_col='reviewdate')
    # 将字符串索引转换成时间索引
    df.index = pd.to_datetime(df.index)
    #ts = df['Passengers']
    ts = df['number']
    return ts

def find_file(path):
    with open(path) as file:
        for line in file:
            yield line

def file_to_data(path):
    for line in find_file(path):
        content = line.strip().split(',')
        print(content[0])


#file_to_data('AirPassengers.csv')

'''
ts = read_data()

print(ts.head())
print(ts.head().index)

print(ts['1949-01-01'])
print(ts[datetime(1949,1,1)])

print(ts['1949'])

print(ts['1949-1':'1949-6'])
'''
