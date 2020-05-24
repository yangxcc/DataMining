import urllib
import sys
import re
from bs4 import BeautifulSoup   #Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库
from collections import deque
import lxml
import sqlite3
import jieba

url='https://www.dlmu.edu.cn/'

unvisited=deque()
visited=set()
unvisited.append(url)

conn=sqlite3.connect('viewsdu.db')
cur=conn.cursor()
cur.execute('create table if not exists doc(id int primary key,link text)')
cur.execute('create table if not exists word(term varchar(25) primary key,list text)')
conn.commit()
cur.close()
print('********开始爬取********')
count=0
print('开始。。。。')
while unvisited:
    url=unvisited.popleft()
    visited.add(url)
    count+=1
    print('开始抓取第',count,'个链接:',url)
    #爬取网页内容
    try:
        response=urllib.request.urlopen(url)
        content=response.read().decode('utf-8')
    except:
        continue
    #寻找下一个可爬的链接，因为搜索范围是在网站内，所以对连接格式有要求，是网站具体情况而定
    #解析网页内容，可能有几种情况，这也是根据这个网站网页的具体情况写的
    soup=BeautifulSoup(content,'lxml')
    all_a=soup.find_all('a',{'class':"c67214"})   #  这个class应该是不对的
    for a in all_a:
        x=a.attrs['href']
        if re.match(r'https.+',x):
            if not re.match(r'https\:\/\/www\.dlmu\.edu\.cn\.+',x):
                continue
        if re.match(r'\/info\/.+',x):
            x='https://www.dlmu.edu.cn'+x
        elif re.match(r'info/.+',x):
            x='https://www.dlmu.edu.cn/'+x
        elif re.match(r'\.\.\/info/.+',x):
            x='https://www.dlmu.edu.cn.'+x[2:]  #???
        elif re.match(r'\.\.\/\.\.\/info/.+',x):
            x='https://www.dlmu.edu.cn.'+x[5:]
        if (x not in visited) and (x not in unvisited):
            unvisited.append(x)
    a=soup.find('a',{'class':"Next"})
    if a!=None:
        x=a.attrs['href']
        if re.match(r'xwdt\/.+',x):
            x='https://www.dlmu.edu.cn/index/'+x
        else:
            x='https://www.dlmu.edu.cn/index/xwdt/'+x
        if (x not in visited) and (x not in unvisited):
            unvisited.append(x)

#爬取网页内容
