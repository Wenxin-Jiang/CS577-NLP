---
language: bn
datasets:
- wikiann
examples:
widget:
- text: "মারভিন দি মারসিয়ান"
  example_title: "Sentence_1"
- text: "লিওনার্দো দা ভিঞ্চি"
  example_title: "Sentence_2"
- text: "বসনিয়া ও হার্জেগোভিনা"
  example_title: "Sentence_3"
- text: "সাউথ ইস্ট ইউনিভার্সিটি"
  example_title: "Sentence_4"
- text: "মানিক বন্দ্যোপাধ্যায় লেখক"
  example_title: "Sentence_5"
---

<h1>Bengali Named Entity Recognition</h1>
Fine-tuning bert-base-multilingual-cased on Wikiann dataset for performing NER on Bengali language.


## Label ID and its corresponding label name

| Label ID | Label Name|
| -------- | ----- |
|0 | O |
| 1 | B-PER |
| 2 | I-PER |
| 3 | B-ORG|
| 4 | I-ORG | 
| 5 | B-LOC |
| 6 | I-LOC |

<h1>Results</h1>

| Name | Overall F1 | LOC F1 | ORG F1 | PER F1 |
| ---- | -------- | ----- | ---- | ---- |
| Train set | 0.997927 | 0.998246 | 0.996613 | 0.998769 |
| Validation set | 0.970187 | 0.969212 | 0.956831 | 0.982079 |
| Test set | 0.9673011 | 0.967120 |  0.963614 | 0.970938 |

Example
```py
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Suchandra/bengali_language_NER")
model = AutoModelForTokenClassification.from_pretrained("Suchandra/bengali_language_NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "মারভিন দি মারসিয়ান"

ner_results = nlp(example)
ner_results
```
