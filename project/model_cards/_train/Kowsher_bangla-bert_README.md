---
language: bn
tags:
- Bert base Bangla
- Bengali Bert
- Bengali lm
- Bangla Base Bert
- Bangla Bert language model
- Bangla Bert
datasets:
- BanglaLM dataset
---
# Bangla BERT Base
Here we published a pretrained Bangla bert language model as **bangla-bert**! which is now available in huggingface model hub. 
Here we described [bangla-bert](https://github.com/Kowsher/bert-base-bangla) which is a pretrained Bangla language model based on mask language modeling described in [BERT](https://arxiv.org/abs/1810.04805) and the GitHub  [repository](https://github.com/google-research/bert)
##  Corpus Details
We trained the Bangla bert language model using BanglaLM dataset from kaggle [BanglaLM](https://www.kaggle.com/gakowsher/bangla-language-model-dataset). There is 3 version of dataset which is almost 40GB.
After downloading the dataset, we went on the way to mask LM.


**bangla-bert Tokenizer**

```py
from transformers import AutoTokenizer, AutoModel
bnbert_tokenizer = AutoTokenizer.from_pretrained("Kowsher/bangla-bert")
text = "খাঁটি সোনার চাইতে খাঁটি আমার দেশের মাটি"
bnbert_tokenizer.tokenize(text)
# output: ['খাটি', 'সে', '##ানার', 'চাইতে', 'খাটি', 'আমার', 'দেশের', 'মাটি']
```
**MASK Generation**
here, we can use bert base bangla model as for masked language modeling:
```py
from transformers import BertForMaskedLM, BertTokenizer, pipeline
model = BertForMaskedLM.from_pretrained("Kowsher/bangla-bert")
tokenizer = BertTokenizer.from_pretrained("Kowsher/bangla-bert")

nlp = pipeline('fill-mask', model=model, tokenizer=tokenizer)
for pred in nlp(f"আমি বাংলার গান {nlp.tokenizer.mask_token}"):
  print(pred)
# {'sequence': 'আমি বাংলার গান লিখি', 'score': 0.17955434322357178, 'token': 24749, 'token_str': 'লিখি'}


nlp = pipeline('fill-mask', model=model, tokenizer=tokenizer)
for pred in nlp(f"তুই রাজাকার তুই {nlp.tokenizer.mask_token}"):
  print(pred)
# {'sequence': 'তুই রাজাকার তুই রাজাকার', 'score': 0.9975168704986572, 'token': 13401, 'token_str': 'রাজাকার'}


nlp = pipeline('fill-mask', model=model, tokenizer=tokenizer)
for pred in nlp(f"বাংলা আমার {nlp.tokenizer.mask_token}"):
  print(pred)
# {'sequence': 'বাংলা আমার অহংকার', 'score': 0.5679506063461304, 'token': 19009, 'token_str': 'অহংকার'}  
```

**Cite this work**
M. Kowsher, A. A. Sami, N. J. Prottasha, M. S. Arefin, P. K. Dhar and T. Koshiba, "Bangla-BERT: Transformer-based Efficient Model for Transfer Learning and Language Understanding," in IEEE Access, 2022, doi: 10.1109/ACCESS.2022.3197662.
## Author
[Kowsher](http://kowsher.org/)
