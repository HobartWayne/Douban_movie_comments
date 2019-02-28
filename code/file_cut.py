# 将电影影评按照电影分成28个文件，并去掉不需要的数据
import pandas as pd
import numpy as np

input_file = 'E:\学习\大四下\毕业设计\douban-movie-short-comments\DMSC.csv'
output_file = ['E:\学习\大四下\毕业设计\code\data\data-{}.csv'.format(i) for i in range(28)]
df = pd.DataFrame(pd.read_csv(input_file, encoding='utf-16'))
name_list = list(df["Movie_Name_EN"].drop_duplicates())
df_name = df.set_index("Movie_Name_EN")

for i in range(28):
    df_output = df_name.loc[name_list[i]].drop(['ID', 'Crawl_Date', 'Number', 'Username'], axis=1, inplace=False)
    df_output.to_csv(output_file[i],encoding='utf-8',index=True)