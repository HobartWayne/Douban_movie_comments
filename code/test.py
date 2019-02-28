import pandas as pd
import numpy as np

url = 'E:\Python36\doubanMovies\data\data-0.csv'
df = pd.DataFrame(pd.read_csv(url,encoding='utf-8'))

star = 5
df_star = df.set_index('Star')
# print(df_star.loc[star]['Comment'])
df_new = df_star.loc[star]
print(df_new.drop(['Crawl_Date','Number','Username'],axis=1,inplace=False))
df_new.drop(['Crawl_Date','Number','Username'],axis=1,inplace=False).to_csv('./test.csv',encoding='utf-8',index=True)