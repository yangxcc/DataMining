import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# nltk.download('brown')
# nltk.download('wordnet')
# 第一次运行时不能注释，让他自动下载，之后再运行便无需下载

from textblob import TextBlob
text = '''
The film is very bad.
the film is common.
The file is very good.
Perfect match for the Gund Huggybuddy I bought as a baby gift.
giant, way too big,sizing is way off, needed to be returned.
The nipple part of the pacifier is fine, but didn't seem like anything special,
The shape of the area around the face makes for a great &#34;handle&#34; 
for baby to hold on to and yank the pacifier out, My daughter continually pulled out the pacifier and would get really upset, 
so we quit using them.
'''
blob = TextBlob(text)
##  词性标注
print('词性标注')
print(blob.tags)
##  分词
print('将句子切分成词或者句子')
token = blob.words
for w in token:
    print(w)
    
 #计算句子情感值
for sentence in blob.sentences:
    print(sentence + '------>'+ str(sentence.sentiment.polarity))