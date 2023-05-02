# SkyText
SkyText is a Chinese GPT3 pre-trained large model released by Singularity-AI, which can perform different tasks such as chatting, Q&A, and Chinese-English translation. SkyText is an open source project of the Chinese GPT3 pre-training model.

## Project Highlights

Technical advantage 1: data cleaning of more than 30 processes

With the development of NLP technology, pre-training large models has gradually become one of the core technologies of artificial intelligence. Pre-training large models usually requires a large amount of text for training, and network text naturally becomes the most important source of corpus. The quality of the training corpus undoubtedly directly affects the effect of the model. In order to train a model with outstanding capabilities, Singularity-AI has used more than 30 cleaning processes in data cleaning. Excellence in details, casting excellent model effect.

Technical advantage 2: optimized and innovative Chinese coding method for Chinese

In the field of pre-training large models, it has always been dominated by the English community, and the importance of Chinese pre-training large models is self-evident. Unlike English, the Chinese input method（pinyin text) of the Chinese pre-trained large model should obviously be different. According to the characteristics of Chinese, Singularity-AI has optimized and innovated a unique Chinese encoding method, which is more in line with Chinese language habits, and rebuilt a Chinese dictionary that is more conducive to model understanding.


# News of Singularity-AI
- [2022.12.15] [AIGC Press Conference of Singularity-AI](https://live.vhall.com/v3/lives/subscribe/697547540)

## Installation

```
Recommend:
transformers>=4.18.0
```

## Model Usage

```python
# -*- coding: utf-8 -*-
from transformers import GPT2LMHeadModel
from transformers import AutoTokenizer
from transformers import TextGenerationPipeline

model = GPT2LMHeadModel.from_pretrained("SkyWork/SkyTextTiny")
tokenizer = AutoTokenizer.from_pretrained("SkyWork/SkyTextTiny", trust_remote_code=True)
text_generator = TextGenerationPipeline(model, tokenizer, device=0)
input_str = "今天是个好天气"
max_new_tokens = 20
print(text_generator(input_str, max_new_tokens=max_new_tokens, do_sample=True))
```

# License
[MIT License]

# Join in the developer group
[Scan the QR code with WeChat](https://user-images.githubusercontent.com/120169448/211474572-4e084a69-04d7-4d34-ab93-ef5fc3007b6f.jpg) to join in the developer group. 


——————————————————————————————

# SkyTextTiny

SkyTextTiny是由奇点智源发布的中文GPT3预训练模型，参数量30亿左右，可以进行聊天、问答、中英互译等不同的[任务](https://openapi.singularity-ai.com/index.html#/examplesIndex)。


## 项目亮点

1. 技术优势一 ：30多道流程的数据清洗
   
   随着NLP技术的发展，预训练大模型逐渐成为了人工智能的核心技术之一。预训练大模型通常需要海量的文本来进行训练，网络文本自然成为了最重要的语料来源。而训练语料的质量无疑直接影响着模型的效果。为了训练出能力出众的模型，奇点智源在数据清洗时使用了30多道的清洗流程。精益求精的细节处理，铸造了卓越的模型效果。

2. 技术优势二：针对中文优化创新的中文编码方式
   
   曾经在预训练大模型领域，一直是被英文社区主导着，而中文预训练大模型的重要性不言而喻。不同于英文的拼音文字，中文预训练大模型的中文输入方式显然应该有所不同。奇点智源针对中文的特点，优化创新使用了独特的中文编码方式，更加符合中文的语言习惯，重新构建出更利于模型理解的中文字典。



# 奇点新闻

- [2022.12.15] [昆仑天工AIGC发布会](https://live.vhall.com/v3/lives/subscribe/697547540)
  
  

## 依赖

```
推荐
transformers>=4.18.0
```

## 模型使用

```python
# -*- coding: utf-8 -*-
from transformers import GPT2LMHeadModel
from transformers import AutoTokenizer
from transformers import TextGenerationPipeline

model = GPT2LMHeadModel.from_pretrained("SkyWork/SkyTextTiny")
tokenizer = AutoTokenizer.from_pretrained("SkyWork/SkyTextTiny", trust_remote_code=True)
text_generator = TextGenerationPipeline(model, tokenizer, device=0)
input_str = "今天是个好天气"
max_new_tokens = 20
print(text_generator(input_str, max_new_tokens=max_new_tokens, do_sample=True))
```

# 版权许可

[MIT License]

# 加入开发者群
[微信扫描此二维码](https://user-images.githubusercontent.com/120169448/211474572-4e084a69-04d7-4d34-ab93-ef5fc3007b6f.jpg) 加入SkyText开发者群。
