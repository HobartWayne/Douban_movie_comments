import pandas as pd
import numpy as np
import jieba
from collections import defaultdict

with open('E:\学习\大四下\毕业设计\code\source\BosonNLP_sentiment_score.txt', 'r', encoding='utf-8')as f:
    senList = f.readlines()
    senDcit = defaultdict()
for line in senList:
    line = line.rstrip('\n').split(' ')
    if(len(line) > 1):
        senDcit[line[0]] = line[1]

##使用jieba分词对影评进行分词处理
input_data = ['E:\学习\大四下\毕业设计\code\data\data-{}.csv'.format(i) for i in range(28)]
output_data = ['E:\学习\大四下\毕业设计\code\data-sentiment-score\data-sentiment-score-{}.csv'.format(i) for i in range(28)]
for i in range(28):
    df = pd.DataFrame(pd.read_csv(open(input_data[i], encoding='utf-8'))).head(100)
    score_list = []
    for line in df['Comment']:
        score = 0
        comments_list = jieba.lcut(line)
        for word in comments_list:
            if word in senDcit.keys():
                score += float(senDcit[word])
        score_list.append(score)
    df['Sentiment_Score'] = score_list
    df.to_csv(output_data[i], encoding='utf-8', index=False)
