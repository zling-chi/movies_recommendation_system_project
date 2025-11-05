import pandas as pd
from functools import reduce

pd.set_option('display.max_rows', None)      # 不省略行
pd.set_option('display.max_columns', None)   # 不省略列
pd.set_option('display.width', None)         # 不换行
pd.set_option('display.max_colwidth', None)  # 列内容不被截断

links = pd.read_csv(r"D:\ml_25m_project\ml-25m\links.csv")
movies = pd.read_csv(r"D:\ml_25m_project\ml-25m\movies.csv")
ratings = pd.read_csv(r"D:\ml_25m_project\ml-25m\ratings.csv")
tags = pd.read_csv(r"D:\ml_25m_project\ml-25m\tags.csv")
genome_score = pd.read_csv(r"D:\ml_25m_project\ml-25m\genome-scores.csv")
genome_tags = pd.read_csv(r"D:\ml_25m_project\ml-25m\genome-tags.csv")

# 转换时间戳
# 1. 秒 → UTC 时间
ratings['utc_time'] = pd.to_datetime(ratings['timestamp'], unit='s')
# 2. 再转东八区
ratings['cst_time'] = (ratings['utc_time']
                  .dt.tz_localize('UTC')        # 先声明这是 UTC 时间
                  .dt.tz_convert('Asia/Shanghai'))
# print(ratings.head(10))
# 3.删除 timestamp 和 utc_time
ratings = ratings.drop(columns = ['timestamp','utc_time'])

# 合并 csv 文件
small = reduce(lambda l, r: pd.merge(l, r, on='movieId', how='left'),
               [movies, links])          # 只有 6 万行
# 最后再左连大表（大表放最右边，避免中间爆炸）
movie = pd.merge(small, ratings, on='movieId', how='left')

#连接 tags，删除 timestamp
movie = pd.merge(movie,tags,on = ("movieId","userId"),how = 'left')
movie = movie.drop(columns='timestamp')

#提取标题title 括号中的年份
movie['year'] = movie['title'].str.extract(r'\((\d{4})\)')

#删除 imdbId，tmdbId
movie = movie.drop(columns=["imdbId","tmdbId"])

movie.to_csv('movies_preprocess.csv',index=False,encoding='utf-8-sig', float_format='%.6f')

