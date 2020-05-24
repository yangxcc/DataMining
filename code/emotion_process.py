from textblob import TextBlob
import pandas as pd

def find_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            yield line

def readFile(path):
    i = 0
    star = []
    help = []
    total = []
    for line in find_file(path):
        if i == 0:
            i=i+1
            continue
        content = line.strip().split('\t')
        if(len(content[0]) > 0 and len(content[1]) > 0 and len(content[2]) > 0 and len(content[3]) > 0):
            if int(content[0]) == 1 :
                star.append(-5)
            elif int(content[0]) == 2 :
                star.append(-4)
            elif int(content[0]) == 3 :
                star.append(0)
            else:
                star.append(int(content[0]))
            help.append(int(content[1]))
            total.append(int(content[2]))
    return star, help, total

path = '486774008.txt'
star, help, total = readFile(path)
data = ""
test = pd.read_table(path)
clomn = test['review_headline']

for line in clomn:
    #line.replace(".",",")[-1]
    data = data + line.replace(".",",").replace("!","").replace("?","") + '.' + '\n'
blob = TextBlob(data)
sentences = blob.sentences
print(len(sentences))

print(len(star), len(help), len(total))
plority = []

for i in range(len(star)):
    plority.append(blob.sentences[i].polarity)
    print(star[i], help[i], total[i], blob.sentences[i].polarity)

print(len(plority))

p1 = 0.3 * sum(star) * 0.2

p2 = 0
for i in range(len(plority)):
    if plority[i] >= 0:
        p2 = p2 + plority[i] * (help[i] + 1) + (plority[i] - 1) * 0.5 * (total[i]-help[i])
    else:
        p2 = p2 + plority[i] * (help[i] + 1) + (plority[i] + 1) * 0.5 * (total[i] - help[i])

print(p1 +0.7 * p2)