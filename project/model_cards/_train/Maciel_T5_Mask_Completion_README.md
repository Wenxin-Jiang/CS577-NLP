---
language: 
- zh
tags:
- conditional text generation
- data augmentation

license: apache-2.0
datasets:
- beyond/chinese_clean_passages_80m


widget:
- text: "[mask]疫情[mask]公园[mask]散步[mask]"
  example_title: "案例1"
- text: "今天[mask]篮球[mask]学校[mask]"
  example_title: "案例2"
- text: "[mask]感染新冠[mask]身体不舒服[mask]多休息[mask]"
  example_title: "案例3"

inference:
  parameters:
    max_length: 128
    num_beams: 10
    no_repeat_ngram_size: 5
    do_sample: True
    min_length: 10
    early_stopping: True
---

## 功能介绍
该模型主要功能是针对mask部分进行补全生成，能够生成较流利丰富的自然文本。

参考案例如下：

1）今天[mask]篮球[mask]学校[mask]

2）[mask]疫情[mask]公园[mask]散步[mask]

3）[mask]感染新冠[mask]身体不舒服[mask]多休息[mask]

## 如何使用
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
pretrained = "Maciel/T5_Mask_Completion"
tokenizer = AutoTokenizer.from_pretrained(pretrained)
model = AutoModelForSeq2SeqLM.from_pretrained(pretrained)

sentence = "[mask]疫情[mask]公园[mask]散步[mask]"
max_input_length = 128
input_encodings = tokenizer(sentence, 
                            max_length=max_input_length, 
                            truncation=True, 
                            return_tensors="pt")
if "token_type_ids" in input_encodings.keys():
    input_encodings.pop("token_type_ids")
output = model.generate(**input_encodings, 
                        num_beams=10,
                        no_repeat_ngram_size=5,
                        do_sample=True, 
                        early_stopping=True,
                        min_length=10,
                        max_length=64,
                        return_dict_in_generate=True,
                        output_scores=True)
decoded_output = tokenizer.batch_decode(output.sequences, skip_special_tokens=True)[0]
completion = decoded_output.strip()
print(completion)
```

## 案例展示
```
1) 原始文本：今天[mask]篮球[mask]学校[mask]
   补全文本：今天,我们来谈谈篮球与学校的关系。

2) 原始文本：[mask]疫情[mask]公园[mask]散步[mask]
   补全文本：在疫情发生之前,人们可以在公园里散步。

3) 原始文本：[mask]感染新冠[mask]身体不舒服[mask]多休息[mask]
   补全文本：如果你感染新冠了,身体不舒服,建议你多休息,不要吃辛辣刺激性的食物,以免加重病情。
```