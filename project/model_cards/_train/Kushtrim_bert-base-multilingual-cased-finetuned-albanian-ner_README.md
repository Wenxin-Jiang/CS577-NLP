---
language:
- sq
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikiann
model-index:
- name: bert-base-multilingual-cased-finetuned-albanian-ner
  results: []
widget:
- "Unë, biri yt, Kosovë t'i njoh dëshirat e heshtura, 
t'i njoh ëndrrat, erërat e fjetura me shekuj, 
t'i njoh vuatjet, gëzimet, vdekjet, 
t'i njoh lindjet e bardha, caqet e tuka të kulluara; 
ta di gjakun që të vlon në gji, 
dallgën kur të rrahë netëve t'pagjumta 
e të shpërthej do si vullkan:- 
më mirë se kushdo tjetër të njoh, Kosovë. 
Unë biri yt.
- Poezi nga Ali Podrimja"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-albanian-ner

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the wikiann dataset.

### Usage
```python
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Kushtrim/bert-base-multilingual-cased-finetuned-albanian-ner")
model = AutoModelForTokenClassification.from_pretrained("Kushtrim/bert-base-multilingual-cased-finetuned-albanian-ner")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy='first')
text = """ Unë, biri yt, Kosovë t'i njoh dëshirat e heshtura,  t'i njoh ëndrrat, erërat e fjetura me shekuj,  t'i njoh vuatjet, gëzimet, vdekjet,  t'i njoh lindjet e bardha, caqet e tuka të kulluara;  ta di gjakun që të vlon në gji,  dallgën kur të rrahë netëve t'pagjumta  e të shpërthej do si vullkan:-  më mirë se kushdo tjetër të njoh, Kosovë.  Unë biri yt. - Poezi nga Ali Podrimja """

results = ner(text)
pd.DataFrame.from_records(results)
```

```
@misc {kushtrim_visoka_2022,
	author       = { Kushtrim Visoka },
	title        = { bert-base-multilingual-cased-finetuned-albanian-ner (Revision 609fca2) },
	year         = 2022,
	url          = { https://huggingface.co/Kushtrim/bert-base-multilingual-cased-finetuned-albanian-ner },
	doi          = { 10.57967/hf/0006 },
	publisher    = { Hugging Face }
}
```
