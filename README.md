# movies_recommendation_system_project
## 📚数据集⬇️⬇️⬇️
### Datasets
#### ratings.csv  保存所有评分记录。
####               |—————  userId
####               |—————  movieId
####               |—————  rating  //评分为5星制，支持0.5-5.0星。
####               |—————  timestamp  //时间戳为自 UTC 1970 年 1 月 1 日午夜以来的秒数。
#### tags.csv  保存所有标签记录。
####               |—————  userId
####               |—————  movieId
####               |—————  tag  //标签是用户自行生成的元数据，通常为单词或短语。标签的含义和用途取决于用户。
####               |—————  timestamp
#### movies.csv  保存所有电影信息。
####               |—————  movieId
####               |—————  title  //标题中包含发行年份，可能存在错误或不一致。
####               |—————  genres  //类型用“|”分隔，类型选择如下：
##### Action  动作、Adventure  冒险、Animation  动画、Children's  儿童、Comedy  喜剧、Crime  犯罪、Documentary  纪录片、Drama  剧情、Fantasy  奇幻、Film-Noir  黑色电影、Horror  恐怖、Musical  音乐、Romance  悬疑、Sci-Fi  科幻、Thriller  惊悚、War  战争、Western  西部、(no genres listed)  未标明类型。
#### links.csv  保存链接到其他电影源的标识符
####               |—————  movieId  //MovieLens 网站使用的电影 ID
####               |—————  imdbId  //IMDb 平台的电影 ID
####               |—————  tmdbId  //The Movie Database 的电影 ID
#### genome-scores.csv & genome-tags.csv  //标签基因组是一个数据结构，包含电影与标签的相关度分数。它是一个稠密矩阵：每部电影在基因组中对每个标签都有一个值。
##### 如[该文献][genome-paper]所述，标签基因组编码了电影在标签描述的属性上表现的强度（如“氛围感”、“发人深省”、“现实主义”等）。其基于用户贡献的标签、评分和文本评论，通过机器学习算法构建。
#### genome-scores.csv  //电影-标签相关度
####               |—————  movieId
####               |—————  tagId  
####               |—————  relevance  //描述某部电影在某个标签上表现的强弱（0-1）
#### genome-tags.csv  //标签描述
####               |—————  tagId  //tagId 值可能在不同版本的数据集中不一致。
####               |—————  tag
#### output  //通过TMDB网站的API获取所有电影的中文标题，每个batch_*.csv包含1000行数据
#### |———————— batch_*.csv  
#### |———————————————— title
#### |———————————————— chinese_name
#### movies_translated.csv  //合并所有batch_*.csv
#### |———————— title
#### |———————— chinese_name
#### movies_translated_preprocess.csv


## 🧮数据预处理⬇️⬇️⬇️
### 1.处理时间戳timestamp
#### 将 ratings.csv 存在的时间戳转换为东八区具体时间，并新建列cst_time,删除timestamp和utc_time
### 2.将movie.csv,ratungs.csv,tags.csv合并
### 3.提取电影标题title内括号的年份，新建列“year”
### 4.生成新的csv文件movies_prepprocess.csv

## 🔎explore⬇️⬇️⬇️
### 将movies_preprocess.csv👉DataFrame
### 获取数据的基本信息
#### movies_preprocess.csv 共25627476行，20万部电影中，包含从 1874 年至 2019 年上映的影片，所有电影的平均评分在3.54星。
#### 在6万部电影中，有855部电影的平均评分为5.0；有543部电影的平均评分为0.5。
#### 在16万位用户中，推荐电影数量最多的用户推荐了32202部，仅推荐20部电影的用户有4504位。
#### 在1874-2019年间，上映电影数量最多为2015年，上映了2513部，上映电影数量最少为1874年，1878年，1880年，1883年，1887年，均仅上映一部电影。
