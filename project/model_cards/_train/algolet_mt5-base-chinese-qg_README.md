<h3 align="center">
    <p>MT5 Base Model for Chinese Question Generation</p>
</h3>
<h3 align="center">
    <p>基于mt5的中文问题生成任务</p>
</h3>

#### 可以通过安装question-generation包开始用
```
pip install question-generation
```
使用方法请参考github项目：https://github.com/algolet/question_generation

#### 在线使用
可以直接在线使用我们的模型：https://www.algolet.com/applications/qg

#### 通过transformers调用
``` python
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("algolet/mt5-base-chinese-qg")
model = AutoModelForSeq2SeqLM.from_pretrained("algolet/mt5-base-chinese-qg")
model.eval()

text = "在一个寒冷的冬天，赶集完回家的农夫在路边发现了一条冻僵了的蛇。他很可怜蛇，就把它放在怀里。当他身上的热气把蛇温暖以后，蛇很快苏醒了，露出了残忍的本性，给了农夫致命的伤害——咬了农夫一口。农夫临死之前说：“我竟然救了一条可怜的毒蛇，就应该受到这种报应啊！”"

text = "question generation: " + text
inputs = tokenizer(text,
                   return_tensors='pt',
                   truncation=True,
                   max_length=512)

with torch.no_grad():
  outs = model.generate(input_ids=inputs["input_ids"],
                        attention_mask=inputs["attention_mask"],
                        max_length=128,
                        no_repeat_ngram_size=4,
                        num_beams=4)

question = tokenizer.decode(outs[0], skip_special_tokens=True) 
questions = [q.strip() for q in  question.split("<sep>") if len(q.strip()) > 0]
print(questions)
['在寒冷的冬天,农夫在哪里发现了一条可怜的蛇?', '农夫是如何看待蛇的?', '当农夫遇到蛇时,他做了什么?'] 
``` 

#### 指标
rouge-1: 0.4041

rouge-2: 0.2104

rouge-l: 0.3843

---
language: 
  - zh
  
tags:
- mt5
- question generation

metrics:
- rouge

---
