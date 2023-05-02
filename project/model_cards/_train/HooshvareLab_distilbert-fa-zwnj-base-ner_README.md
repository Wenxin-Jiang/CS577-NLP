---
language: fa
---


# DistilbertNER

This model fine-tuned for the Named Entity Recognition (NER) task on a mixed NER dataset collected from [ARMAN](https://github.com/HaniehP/PersianNER), [PEYMA](http://nsurl.org/2019-2/tasks/task-7-named-entity-recognition-ner-for-farsi/), and [WikiANN](https://elisa-ie.github.io/wikiann/) that covered ten types of entities: 

- Date (DAT)
- Event (EVE)
- Facility (FAC)
- Location (LOC)
- Money (MON)
- Organization (ORG)
- Percent (PCT)
- Person (PER)
- Product (PRO)
- Time (TIM)


## Dataset Information

|       |   Records |   B-DAT |   B-EVE |   B-FAC |   B-LOC |   B-MON |   B-ORG |   B-PCT |   B-PER |   B-PRO |   B-TIM |   I-DAT |   I-EVE |   I-FAC |   I-LOC |   I-MON |   I-ORG |   I-PCT |   I-PER |   I-PRO |   I-TIM |
|:------|----------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| Train |     29133 |    1423 |    1487 |    1400 |   13919 |     417 |   15926 |     355 |   12347 |    1855 |     150 |    1947 |    5018 |    2421 |    4118 |    1059 |   19579 |     573 |    7699 |    1914 |     332 |
| Valid |      5142 |     267 |     253 |     250 |    2362 |     100 |    2651 |      64 |    2173 |     317 |      19 |     373 |     799 |     387 |     717 |     270 |    3260 |     101 |    1382 |     303 |      35 |
| Test  |      6049 |     407 |     256 |     248 |    2886 |      98 |    3216 |      94 |    2646 |     318 |      43 |     568 |     888 |     408 |     858 |     263 |    3967 |     141 |    1707 |     296 |      78 |


## Evaluation

The following tables summarize the scores obtained by model overall and per each class.

**Overall**

|    Model   | accuracy | precision |  recall  |    f1    |
|:----------:|:--------:|:---------:|:--------:|:--------:|
| Distilbert | 0.994534 |  0.946326 |  0.95504 | 0.950663 |


**Per entities**

|     	| number 	| precision 	|  recall  	|    f1    	|
|:---:	|:------:	|:---------:	|:--------:	|:--------:	|
| DAT 	|   407  	|  0.812048 	| 0.828010 	| 0.819951 	|
| EVE 	|   256  	|  0.955056 	| 0.996094 	| 0.975143 	|
| FAC 	|   248  	|  0.972549 	| 1.000000 	| 0.986083 	|
| LOC 	|  2884  	|  0.968403 	| 0.967060 	| 0.967731 	|
| MON 	|   98   	|  0.925532 	| 0.887755 	| 0.906250 	|
| ORG 	|  3216  	|  0.932095 	| 0.951803 	| 0.941846 	|
| PCT 	|   94   	|  0.936842 	| 0.946809 	| 0.941799 	|
| PER 	|  2645  	|  0.959818 	| 0.957278 	| 0.958546 	|
| PRO 	|   318  	|  0.963526 	| 0.996855 	| 0.979907 	|
| TIM 	|   43   	|  0.760870 	| 0.813953 	| 0.786517 	|


## How To Use
You use this model with Transformers pipeline for NER.

### Installing requirements

```bash
pip install transformers
```

### How to predict using pipeline

```python
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification  # for pytorch
from transformers import TFAutoModelForTokenClassification  # for tensorflow
from transformers import pipeline


model_name_or_path = "HooshvareLab/distilbert-fa-zwnj-base-ner" 
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForTokenClassification.from_pretrained(model_name_or_path)  # Pytorch
# model = TFAutoModelForTokenClassification.from_pretrained(model_name_or_path)  # Tensorflow

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "در سال ۲۰۱۳ درگذشت و آندرتیکر و کین برای او مراسم یادبود گرفتند."

ner_results = nlp(example)
print(ner_results)
```


## Questions?
Post a Github issue on the [ParsNER Issues](https://github.com/hooshvare/parsner/issues) repo.