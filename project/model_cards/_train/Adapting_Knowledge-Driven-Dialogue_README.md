# Commit Hash
1. BART 5 epoch training: 5e2267251ec1555e81f9ed6f090e1f70355ff1c8
2. BART 10 epoch training: 2e347c5f162fe18bb8d874d2bd0b46ae3d9ff175
3. BART 13 epoch training: 58b307615eb37f44a9233318427420b330fb6cea

# Dataset
[link](https://huggingface.co/datasets/Adapting/Knowledge-Driven-Dialogues)

# Training Results
| Num of Epochs | Training Loss| Validation Loss|
| :--- | :--- | :--- |
| 1 | 1.569600 | 1.605180 |
| 2 | 1.330900 | 1.523424 |
| 3 | 1.212800 | 1.519999 |
| 4 | 1.151600 | 1.520266 |
| 5 | 1.094100 | 1.516026 |

# Usage
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("Adapting/Knowledge-Driven-Dialogue")
model_5 = AutoModelForSeq2SeqLM.from_pretrained("Adapting/Knowledge-Driven-Dialogue", revision = '5e2267251ec1555e81f9ed6f090e1f70355ff1c8')

pipe_5 = pipeline('text2text-generation',tokenizer=tokenizer,model=model_5,truncation=True, max_length=1024)

knowledge = '''[ett] 的性别是男。[ett] 的星座是天蝎座。[ett] 的代表作品是《姐姐》《孤独的人是可耻的》《爱情》《上苍保佑吃完了饭的人民》。[ett] 的出生地是湖南。[ett] 的毕业院校是陕西机械学院。[ett] 的出生日期是1968年11月17日。[ett] 的爱好是湖南菜。[ett] 的中文名是张楚。[ett] 的爱好是思考。[ett] 的别名是张红兵。[ett] 的国籍是中国。[ett] 的血型是A型。[ett] 的民族是汉。[ett] 的Information是张楚，中国大陆音乐人，原名张红兵，1968年11月生于湖南，在湖南浏阳的外婆家生活了8年，8岁时，跟随父母搬到了陕西。这些年，他走遍了中国大部分的城市，尤其是那些有自然风光的地方，有一些流浪的感觉。他大部份歌曲创作的时候都是走在路上，独自漂泊。10岁那年第一次离家出走，17岁考入原陕西机械学院，即西安理工大学，土木工程系，后又辍学。1987年只身来到北京，从此踏上了音乐之路。张楚的一首《姐姐》唱遍大江南北，并和窦唯、何勇、唐朝乐队赴香港“中国摇滚乐势力”演唱会引起极大轰动，开辟了中国摇滚的鼎盛时代，和许巍和郑钧是曾经的西安”三剑客“。。[ett] 的职业是歌'''
usr = '你知道张楚的国籍吗？'

input = f'[klg] {knowledge} [usr] {usr}'
print(pipe_5(input))

'''
[{'generated_text': '知 道 啊 ， 他 是 中 国 人 。'}]
'''

```