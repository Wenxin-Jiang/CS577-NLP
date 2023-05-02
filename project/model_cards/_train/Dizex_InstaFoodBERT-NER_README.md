---
language: en
datasets:
- Dizex/InstaFoodSet
widget:
- text: "Today's meal: Fresh olive poké bowl topped with chia seeds. Very delicious!"
  example_title: "Food example 1"
- text: "Tartufo Pasta with garlic flavoured butter and olive oil, egg yolk, parmigiano and pasta water."
  example_title: "Food example 2"  
tags:
- Instagram
- NER
- Named Entity Recognition
- Food Entity Extraction
- Social Media
- Informal text
license: mit
---
# InstaFoodBERT-NER

## Model description

**InstaFoodBERT-NER** is a fine-tuned BERT model that is ready to use for **Named Entity Recognition** of Food entities on informal text (social media like). It has been trained to recognize a single entity: food (FOOD).

Specifically, this model is a *bert-base-cased* model that was fine-tuned on a dataset consisting of 400 English Instagram posts related to food. The [dataset](https://huggingface.co/datasets/Dizex/InstaFoodSet) is open source.


## Intended uses

#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Dizex/InstaFoodBERT-NER")
model = AutoModelForTokenClassification.from_pretrained("Dizex/InstaFoodBERT-NER")

pipe = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Today's meal: Fresh olive poké bowl topped with chia seeds. Very delicious!"

ner_entity_results = pipe(example)
print(ner_entity_results)
```

