import numpy as np
import pandas as pd
import requests


stopwords_url = 'https://raw.githubusercontent.com/goto456/stopwords/master/hit_stopwords.txt'
stopwords = requests.get(stopwords_url).text.split('\n')
print(stopwords)
with open('视频名stopwords.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('视频名stopwords.txt', 'a+', encoding='utf-8') as f:
    for i in stopwords:
        f.write(f'{i}\n')

