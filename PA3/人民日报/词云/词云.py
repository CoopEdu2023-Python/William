import jieba
import jieba.analyse
import pandas as pd
from wordcloud import WordCloud
import re
import requests
from PIL import Image

words = []

# Load user dictionary
jieba.load_userdict("dict.txt")

data = pd.read_csv('../评论信息.csv')
comments = data['评论内容']
for comment in comments:
    comment = str(comment)

    # Exclude emoji
    comment = re.sub(r'\[.*?\]', '', comment)

    # Exclude @username
    comment = re.sub(r'@.*? ', '', comment)

    # Cut sentence by jieba
    words += jieba.cut(comment)

with open('评论stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = f.read().split('\n')

# Exclude stopwords from words
words = [word for word in words if word not in stopwords]

wordcloud = WordCloud(
    width=6400,
    height=3200,
    font_path='C:/Windows/Fonts/Microsoft YaHei UI/msyhbd.ttc',
    background_color='white',
    random_state=40,
)

# Generate wordcloud
wordcloud.generate(' '.join(words))

# Save as png
wordcloud.to_file(f'评论词云.png')

keywords = jieba.analyse.extract_tags(' '.join(words), topK=5)
print(keywords)
