# movies_recommendation_system_project
## 📚数据集说明⬇️⬇️⬇️
### 该数据集（ml-25m）描述了来自MovieLens的 5 星评分和自由文本标签活动，这是一个电影推荐服务。它包含 25,000,095 条评分和 1,093,360 条标签记录，涉及 62,423 部电影。这些数据由 162,541 位用户在 1995 年 1 月 9 日至 2019 年 11 月 21 日期间创建。该数据集生成于 2019 年 11 月 21 日。
### 用户是随机选取的。所有被选中用户至少评价过 20 部电影。数据集中不包含任何人口统计信息。每个用户仅通过 ID 表示，没有提供其他信息。
### 数据包含在以下文件中：genome-scores.csv、genome-tags.csv、links.csv、movies.csv、ratings.csv 和 tags.csv。下文将提供这些文件的内容和使用细节。
### 该数据集及 GroupLens 的其他数据集可在 http://grouplens.org/datasets/免费获取。

### 用户ID：用户随机选取，使用匿名ID进行标识。
### 电影ID：数据集中的电影只包含被评分或打标签过。
### Datasets
#### ratings.csv  保存所有评分记录。
####               |——————  userId
####               |——————  movieId
####               |——————  rating  //评分为5星制，支持0.5-5.0星。
####               |——————  timestamp  //时间戳为自 UTC 1970 年 1 月 1 日午夜以来的秒数。
#### tags.csv  保存所有标签记录。
####               |——————  userId
####               |——————  movieId
####               |——————  tag  //标签是用户自行生成的元数据，通常为单词或短语。标签的含义和用途取决于用户。
####               |——————  timestamp
#### movies.csv  保存所有电影信息。
####               |——————  movieId
####               |——————  title  //标题中包含发行年份，可能存在错误或不一致。
####               |——————  genres  //类型用“|”分隔，类型选择如下：
##### Action  动作、Adventure  冒险、Animation  动画、Children's  儿童、Comedy  喜剧、Crime  犯罪、Documentary  纪录片、Drama  剧情、Fantasy  奇幻、Film-Noir  黑色电影、Horror  恐怖、Musical  音乐、Romance  悬疑、Sci-Fi  科幻、Thriller  惊悚、War  战争、Western  西部、(no genres listed)  未标明类型。
#### links.csv  保存链接到其他电影源的标识符
####               |——————  movieId  //MovieLens 网站使用的电影 ID
####               |——————  imdbId  //IMDb 平台的电影 ID
####               |——————  tmdbId  //The Movie Database 的电影 ID
#### genome-scores.csv & genome-tags.csv  //标签基因组是一个数据结构，包含电影与标签的相关度分数。它是一个稠密矩阵：每部电影在基因组中对每个标签都有一个值。
##### 如[该文献][genome-paper]所述，标签基因组编码了电影在标签描述的属性上表现的强度（如“氛围感”、“发人深省”、“现实主义”等）。其基于用户贡献的标签、评分和文本评论，通过机器学习算法构建。
##### genome-scores.csv  //电影-标签相关度
#####                             |——————  movieId
#####                             |——————  tagId  
#####                             |——————  relevance
##### genome-tags.csv  //标签描述
#####                             |——————  tagId  //tagId 值可能在不同版本的数据集中不一致。
#####                             |——————  tag
