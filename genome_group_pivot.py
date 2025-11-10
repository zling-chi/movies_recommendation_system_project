# 标签基因组最常见的Pipeline:加载 → 构建电影-标签矩阵 → 计算相似度 → 为用户推荐

import pandas as pd
import numpy as np
# 导入计算余弦相似度的工具
from sklearn.metrics.pairwise import cosine_similarity

# 导入 csv 文件
scores = pd.read_csv(r"C:\Users\wchenzl7\Desktop\ml-25m\ml-25m\genome-scores.csv")
tags = pd.read_csv(r"C:\Users\wchenzl7\Desktop\ml-25m\ml-25m\genome-tags.csv")
movies = pd.read_csv(r"C:\Users\wchenzl7\Desktop\ml-25m\ml-25m\movies.csv")

# 合并 csv 文件
scores = scores.merge(tags,on='tagId',how='left')

# 处理 movies['title'] 的括号及内容
movies['title'] = movies['title'].str.replace(r'\s*\(.*?\)', '', regex=True).str.strip()
# 构建电影-标签矩阵
movie_tag = (scores.pivot_table(
    index='movieId',#列 --> 行索引
    columns='tag',#列 --> 列索引
    values='relevance',#汇总的数据列
    aggfunc='mean'#聚合函数：对剩余数值列做统计
    ).fillna(0))
#pivot_table Python版的数据透视表，长表变宽表
# 矩阵结构如下：
#| movieId | action | romantic | dark | ... |
#| ------- | ------ | -------- | ---- | --- |
#| 1       | 0.76   | 0.85     | 0.12 | ... |
#| 2       | 0.10   | 0.23     | 0.75 | ... |
#| ...     | ...    | ...      | ...  | ... |

# 计算电影之间的相似度（余弦）：
# 把每部电影的“标签向量”当成空间中的一个点，然后计算所有电影两两之间的“夹角余弦”，得到一张相似度矩阵
# 值域为[-1,1],越大越相似。
movie_vectors = movie_tag.values  # 形状：(n_movies, n_tags)
sim_matrix = cosine_similarity(movie_vectors)  # 形状：(n_movies, n_movies)

# 为方便查询，保持 movieId 到矩阵索引的映射
# 实现知道 movieId --> 查到它在第几排
# 知道 第几排 --> 反查到 movieId
## 把 movie_tag 的索引依次编号0，1，2，...,得到 movieId --> 矩阵行号 的正向字典
## 例：{1:0, 260:1, 1196:2, …}
movieid_to_idx = {mid:idx for idx, mid in enumerate(movie_tag.index)}
## 把上面得到的字典键值翻转，得到 矩阵行号 --> movieId 的反向字典
## 例：{0:1, 1:260, 2:1196, …}
idx_to_movieid = {idx:mid for mid, idx in movieid_to_idx.items()}
# 取 movies 的 movieId 和 title 两列，做正向字典
# 例：{1: 'Toy Story (1995)', 260: 'Star Wars: Episode IV (1977)', ...}
id_title = movies.set_index("movieId")["title"].to_dict()
# 再做一个反向字典
title_id = (movies.drop_duplicates('title', keep='first'
                                  ).set_index('title')['movieId']
                                   .to_dict())

# 给定一个 movieId，找最相似的 K 部电影
def similar_movies(movieId, K=10):
    idx = movieid_to_idx[movieId]  # 用字典把 movieId 转换成 idx
    sims = sim_matrix[idx]  # 把把这排对应的整条“相似度向量”(和所有电影的相似度分数)取出
    top_idx = np.argsort(-sims)[1:K+1]  # np.argsort(-sim) 把相似度从高到低排序，返回索引顺序，并跳过自己
    return [idx_to_movieid[i] for i in top_idx]  # 把 K 个 idx --> movieId,函数返回一份“最相似”名单

# 给定电影片名，找到最相似的 K 部电影
def recommend_by_title(title, K=5):
    # 片名 → ID
    if title not in title_id:
        return [f'未找到影片：{title}']
    movie_id = title_id[title]
    # 复用旧函数拿 ID 列表
    rec_ids = similar_movies(movie_id, K)
    # ID → 片名
    rec_titles = [id_title[i] for i in rec_ids]
    return rec_titles

# 测试
want = input('请输入喜欢的电影全称：')   # 如 "Toy Story (1995)"
print('为您推荐：')
for t in recommend_by_title(want, 10):
     print(' -', t)