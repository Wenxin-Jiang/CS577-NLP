# Brief introduction of SkyCode
SkyCode is a multi-language open source programming model released by Singularity-AI. It adopts the GPT3 model structure and uses a large amount of code for training. Support Java, JavaScript, C, C++, Python, Go, shell and other mainstream programming languages, and can understand Chinese comments. The model can complete the code, solve problems and other operations, freeing you from programming and focusing on solving larger problems.

## Project Highlights
1. Technical advantage 1: covering multiple programming languages

Different programming languages focus on solving problems in different platforms and environments, and different programming languages have their own reasons for existence. The codes that Singularity-AI SkyCode can generate not only include widely used JavaScript, python, Java, C, etc., but also cover more than ten programming languages such as php, go, and swift, so that users of different languages can experience SkyCode has powerful code generation capabilities.

2. Technical advantage 2: optimize for Chinese annotations

In the field of pre-training large models, it has always been dominated by the English community. The code generation model based on GPT3 has the same problem. Relying on the experience of deeply cultivating Chinese models, Singularity-AI optimized and innovated a unique Chinese encoding method according to the characteristics of Chinese, which is more in line with Chinese language habits, making the model's ability to understand Chinese annotations better.

3. Technical advantage 3: excellent problem-solving ability
  
  On the HumanEval data set that reflects the problem-solving ability of the code generation model, the problem-solving ability of SkyCode is also much higher than that of other open source models.
   | model          | pass@1 | pass@10 | pass@100 |
   |:-------------- | ------:|:-------:| -------- |
   | GPT-Neo 1.3B   | 4.79%  | 7.47%   | 16.30%   |
   | GPT-Neo 2.7B   | 6.41%  | 11.27%  | 21.37%   |
   | GPT-J 6B       | 11.62% | 15.74%  | 27.74%   |
   | SKY_code(2.6B) | 12.84% | 21.07%  | 35.97%   |
  It can be seen that SkyCode with a parameter quantity of 2.6B is not only much higher than the GPT-Neo 1.3B model with fewer parameters, but also much higher than the GPT-Neo 2.7B model with a comparable parameter quantity. Even compared to the GPT-J 6B model with a higher number of parameters, SkyCode's problem-solving ability is stronger. In the pass@100 indicator that better reflects the upper limit of problem-solving ability, SkyCode's net value exceeds GPT-J by 8.23%.

# News of Singularity-AI
- [2022.12.15] [AIGC Press Conference of Singularity-AI](https://live.vhall.com/v3/lives/subscribe/697547540)


## Reliance
```
Recommend:
transformers>=4.18.0
```

## Model usage
```python
# -*- coding: utf-8 -*-
from transformers import GPT2LMHeadModel
from transformers import AutoTokenizer
from transformers import TextGenerationPipeline

model = GPT2LMHeadModel.from_pretrained("SkyWork/SkyCode")
tokenizer = AutoTokenizer.from_pretrained("SkyWork/SkyCode", trust_remote_code=True)
text_generator = TextGenerationPipeline(model, tokenizer, device=0)
input_str = "if __name__"
max_new_tokens = 40
print(text_generator(input_str, max_new_tokens=max_new_tokens, do_sample=True))### 
```


# Licence
[MIT License](LICENSE)

# Join in developer group
[Scan the QR Code with WeChat](https://user-images.githubusercontent.com/120169448/211475709-75b5f652-366f-45a1-b8c0-0bd64e8256bb.jpg)  to join in the developer group of SkyCode.

——————————————————————————————————————————————————————————————————————————————

# SkyCode

SkyCode是由奇点智源发布的多语言开源编程大模型，采用GPT3模型结构，使用海量的代码进行训练。支持Java, JavaScript, C, C++, Python, Go, shell等多种主流编程语言，并能理解中文注释。模型可以对代码进行补全，进行解题等操作，使您从编程中解放出来，专心于解决更大的问题。


## 项目亮点

1. 技术优势一 ：涵盖多种编程语言
   
   不同的编程语言着重于解决不同平台、环境下的问题，不同的编程语言都有自己存在的理由。奇点智源SkyCode能够生成的代码，不仅包括使用广泛的JavaScript、python、Java、C等，还涵盖了php、go、swift等共计十余种编程语言，使不同语言的使用者都能来体验SkyCode强大的代码生成能力。

2. 技术优势二：针对中文注释进行优化
   
   曾经在预训练大模型领域，一直是被英文社区主导着，依托于GPT3的代码生成模型有着同样的问题。奇点智源凭借深耕中文模型的经验，针对中文的特点，优化创新使用了独特的中文编码方式，更加符合中文的语言习惯，使得模型对中文注释的理解能力更为优秀。

3. 技术优势三：极其出色的解题能力
   
   在体现代码生成模型解题能力的HumanEval数据集上，奇点智源SkyCode的解题能力也远高出其他开源模型。
   
   | model          | pass@1 | pass@10 | pass@100 |
   |:-------------- | ------:|:-------:| -------- |
   | GPT-Neo 1.3B   | 4.79%  | 7.47%   | 16.30%   |
   | GPT-Neo 2.7B   | 6.41%  | 11.27%  | 21.37%   |
   | GPT-J 6B       | 11.62% | 15.74%  | 27.74%   |
   | SKY_code(2.6B) | 12.84% | 21.07%  | 35.97%   |
   
   可以看到，参数量2.6B的SkyCode在解题能力上不仅高出参数较少的GPT-Neo 1.3B许多，也远高于参数量相当的GPT-Neo 2.7B模型。即使对比参数量更高的GPT-J 6B模型，SkyCode的解题能力也更强。在更能体现解题能力上限的pass@100指标上，SkyCode超出GPT-J的净值为8.23%。


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

model = GPT2LMHeadModel.from_pretrained("SkyWork/SkyCode")
tokenizer = AutoTokenizer.from_pretrained("SkyWork/SkyCode", trust_remote_code=True)
text_generator = TextGenerationPipeline(model, tokenizer, device=0)
input_str = "if __name__"
max_new_tokens = 40
print(text_generator(input_str, max_new_tokens=max_new_tokens, do_sample=True))### 
```

# 版权许可

[MIT License](LICENSE)

# 加入SkyCode开发者群
[微信扫描此二维码](https://user-images.githubusercontent.com/120169448/211475709-75b5f652-366f-45a1-b8c0-0bd64e8256bb.jpg) 加入SkyCode开发者群。