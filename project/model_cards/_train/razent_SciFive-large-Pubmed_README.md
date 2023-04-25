---
language: 
  - en

tags:
- token-classification
- text-classification
- question-answering
- text2text-generation
- text-generation

datasets:
- pubmed

---


# SciFive Pubmed Large

## Introduction
Paper: [SciFive: a text-to-text transformer model for biomedical literature](https://arxiv.org/abs/2106.03598)

Authors: _Long N. Phan, James T. Anibal, Hieu Tran, Shaurya Chanana, Erol Bahadroglu, Alec Peltekian, Grégoire Altan-Bonnet_

## How to use
For more details, do check out [our Github repo](https://github.com/justinphan3110/SciFive). 
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("razent/SciFive-large-Pubmed")  
model = AutoModelForSeq2SeqLM.from_pretrained("razent/SciFive-large-Pubmed")
​
sentence = "Identification of APC2 , a homologue of the adenomatous polyposis coli tumour suppressor ."
text =  sentence + " </s>"

encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")

outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    early_stopping=True
)

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)
```