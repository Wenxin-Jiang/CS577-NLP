---
language: ja
thumbnail: https://github.com/rinnakk/japanese-pretrained-models/blob/master/rinna.png
tags:
- ja
- japanese
- gpt
- text-generation
- lm
- nlp
license: mit
datasets:
- cc100
- wikipedia
- c4
widget:
- text: "西田幾多郎は、"
---

# japanese-gpt-1b

![rinna-icon](./rinna.png)

This repository provides a 1.3B-parameter Japanese GPT model. The model was trained by [rinna Co., Ltd.](https://corp.rinna.co.jp/)

# How to use the model

~~~~
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-1b", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-1b")

if torch.cuda.is_available():
    model = model.to("cuda")

text = "西田幾多郎は、"
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_length=100,
        min_length=100,
        do_sample=True,
        top_k=500,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bad_words_ids=[[tokenizer.unk_token_id]]
    )

output = tokenizer.decode(output_ids.tolist()[0])
print(output)  
# sample output: 西田幾多郎は、その主著の「善の研究」などで、人間の内面に自然とその根源があると指摘し、その根源的な性格は、この西田哲学を象徴しているとして、カントの「純粋理性批判」と「判断力批判」を対比して捉えます。それは、「人が理性的存在であるかぎりにおいて、人はその当人に固有な道徳的に自覚された善悪の基準を持っている」とするもので、この理性的な善悪の観念を否定するのがカントの
~~~~

# Model architecture
A 24-layer, 2048-hidden-size transformer-based language model.

# Training
The model was trained on [Japanese C4](https://huggingface.co/datasets/allenai/c4), [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz) and [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch) to optimize a traditional language modelling objective. It reaches around 14 perplexity on a chosen validation set from the same data.
# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer. The vocabulary was first trained on a selected subset from the training data using the official sentencepiece training script, and then augmented with emojis and symbols.
# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
