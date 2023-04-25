---
language: 
  - en

tags:
- text2text-generation
- mednli

datasets:
- pubmed
- pmc/open_access
widget:
- text: "mednli: sentence1: In the ED, initial VS revealed T 98.9, HR 73, BP 121/90, RR 15, O2 sat 98% on RA. sentence2: The patient is hemodynamically stable"
---

# SciFive Pubmed+PMC Large on MedNLI

## Introduction

Finetuned SciFive Pubmed+PMC Large model achieved state-of-the-art results on [MedNLI (Medical Natural Language Inference)](https://paperswithcode.com/sota/natural-language-inference-on-mednli)

Paper: [SciFive: a text-to-text transformer model for biomedical literature](https://arxiv.org/abs/2106.03598)

Authors: _Long N. Phan, James T. Anibal, Hieu Tran, Shaurya Chanana, Erol Bahadroglu, Alec Peltekian, Grégoire Altan-Bonnet_

## How to use
For more details, do check out [our Github repo](https://github.com/justinphan3110/SciFive). 
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("razent/SciFive-large-Pubmed_PMC-MedNLI")  
model = AutoModelForSeq2SeqLM.from_pretrained("razent/SciFive-large-Pubmed_PMC-MedNLI")
model.cuda()
​
sent_1 = "In the ED, initial VS revealed T 98.9, HR 73, BP 121/90, RR 15, O2 sat 98% on RA."
sent_2 = "The patient is hemodynamically stable"
text =  f"mednli: sentence1: {sent_1} sentence2: {sent_2}"

encoding = tokenizer.encode_plus(text, padding='max_length', max_length=256, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")

outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=8,
    early_stopping=True
)

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)
```