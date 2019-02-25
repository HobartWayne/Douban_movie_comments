#将电影影评按照电影分成28个文件，并去掉不需要的数据
import pandas as pd
import numpy as np

input_file = 'E:\学习\大四下\毕业设计\code\data\data-0.csv'
# output_file = ['data-{}.csv'.format(i)for i in range(28)]
df = pd.DataFrame(pd.read_csv(input_file,encoding='utf-16'))
data_all =