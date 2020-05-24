'''
随机产生的单词
将随机产生单词的顺序打乱
'''
import random

print("欢迎参加猜单词游戏")

WORDS=['python','java','application','console','keyng']
jumple=''
word=random.choice(WORDS)
correct=word   #非常重要！！！保留word的值，因为下面word的值变了
while word:
    position=random.randrange(len(word))
    jumple+=word[position]
    word=word[:position]+word[(position+1):]    #注意这种写法
print("乱序后的单词：",jumple)
guess=input("请你猜：")
while guess!=correct and guess!="":
    print("猜错了")
    guess=input("继续猜：")
    if guess==correct:
        print("猜对了\n")


