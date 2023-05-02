---
language: en
datasets:
- Dizex/FoodBase
widget:
- text: "Today's meal: Fresh olive poké bowl topped with chia seeds. Very delicious!"
  example_title: "Food example 1"
- text: "Tartufo Pasta with garlic flavoured butter and olive oil, egg yolk, parmigiano and pasta water."
  example_title: "Food example 2"  
tags:
- FoodBase
- NER
license: mit
---
# FoodBaseBERT

## Model description

**FoodBaseBERT** is a fine-tuned BERT model that is ready to use for **Named Entity Recognition** of Food entities. It has been trained to recognize one entity: food (FOOD).

Specifically, this model is a *bert-base-cased* model that was fine-tuned on the [FoodBase NER](https://academic.oup.com/database/article/doi/10.1093/database/baz121/5611291) dataset. 


## Intended uses

#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Dizex/FoodBaseBERT")
model = AutoModelForTokenClassification.from_pretrained("Dizex/FoodBaseBERT")

pipe = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Today's meal: Fresh olive poké bowl topped with chia seeds. Very delicious!"

ner_entity_results = pipe(example)
print(ner_entity_results)
```
