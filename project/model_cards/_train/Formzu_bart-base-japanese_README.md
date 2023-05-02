---
language: 
- ja
license: mit
tags:
- bart
- pytorch
datasets:
- wikipedia
---
# bart-base-japanese

This model is converted from the original [Japanese BART Pretrained model](https://nlp.ist.i.kyoto-u.ac.jp/?BART%E6%97%A5%E6%9C%AC%E8%AA%9EPretrained%E3%83%A2%E3%83%87%E3%83%AB) released by Kyoto University.

Both the encoder and decoder outputs are identical to the original Fairseq model.

### How to use the model

The input text should be tokenized by [BartJapaneseTokenizer](https://huggingface.co/Formzu/bart-base-japanese/blob/main/tokenization_bart_japanese.py). 

Tokenizer requirements:
* [Juman++](https://github.com/ku-nlp/jumanpp)
* [zenhan](https://pypi.org/project/zenhan/)  
* [pyknp](https://pypi.org/project/pyknp/)  
* [sentencepiece](https://pypi.org/project/sentencepiece/) 

#### Simple FillMaskPipeline
```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_name = "Formzu/bart-base-japanese"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

masked_text = "天気が<mask>から散歩しましょう。"

fill_mask = pipeline("fill-mask", model=model, tokenizer=tokenizer)
out = fill_mask(masked_text)
print(out)
# [{'score': 0.19255658984184265, 'token': 1718, 'token_str': 'よく', 'sequence': '天気 が よく から 散歩 し ましょう 。'}, 
#  {'score': 0.14426815509796143, 'token': 5478, 'token_str': '良く', 'sequence': '天気 が 良く から 散歩 し ましょう 。'}, 
#  {'score': 0.05554169788956642, 'token': 6561, 'token_str': '悪い', 'sequence': '天気 が 悪い から 散歩 し ましょう 。'}, 
#  {'score': 0.05524599179625511, 'token': 3553, 'token_str': '良い', 'sequence': '天気 が 良い から 散歩 し ましょう 。'}, 
#  {'score': 0.03720080852508545, 'token': 1370, 'token_str': '良', 'sequence': '天気 が 良 から 散歩 し ましょう 。'}]
```
#### Text Generation
```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "Formzu/bart-base-japanese"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

masked_text = "天気が<mask>から散歩しましょう。"

inp = tokenizer(masked_text, return_tensors='pt').to(device)

out = model.generate(**inp, num_beams=1, min_length=0, max_length=20, early_stopping=True,  no_repeat_ngram_size=2)
res = "".join(tokenizer.decode(out.squeeze(0).tolist(), skip_special_tokens=True).split(" "))
print(res)
# 天気がよくなってから散歩しましょう。天気のよく合っているところにいる
```

### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Tokenizers 0.12.1
