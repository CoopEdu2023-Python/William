from cemotion import Cemotion
import pandas as pd

c = Cemotion()
emo_list = []
comment = pd.read_csv('../评论信息.csv')['评论内容']
for i in comment:
    emo = c.predict(i)
    emo_list.append(emo)
    print(emo, i)

with open('情绪值.csv', 'w', encoding='utf-8') as f:
    f.write('emo_num,\n')
with open('情绪值.csv', 'a+', encoding='utf-8') as f:
    for i in emo_list:
        f.write(f'{i},\n')
print(emo_list)