import pandas as pd
from textblob import TextBlob

path = '197856712.txt'
num_data=""
data = ""
i=0
j= 0
k=0
total=0

test = pd.read_table(path)
clomn = test['review_headline']

for line in clomn:
    #line.replace(".",",")[-1]
    i = i + 1
    data = data + line.replace(".",",").replace("!","") + '.' + '\n'


# print(data)
#print(clomn)
# with open(path, 'r') as f:
#     for line in f:
#         data += line
#         #value = line[:-1] #去掉换行符
#         # line.replace('.',',')
#         i=i+1
#         # new_line = new_line[:-1].replace("!",",")
#         # new_line = new_line[:-1].replace("?",",")
#         # new_line = new_line[:-1].replace(";",",")
#         #file_data += line
#
# print(data)


blob = TextBlob(data)
sentences = blob.sentences
print("1分句：",len(sentences))
print(i)

for sentence in blob.sentences:
    print(sentence + '------>'+ str(sentence.sentiment.polarity))
    total = total + sentence.sentiment.polarity
    if sentence.sentiment.polarity > 0:
        j = j +1
    if sentence.sentiment.polarity < 0:
        k = k+1
print(j)
print(k)

print(total)

