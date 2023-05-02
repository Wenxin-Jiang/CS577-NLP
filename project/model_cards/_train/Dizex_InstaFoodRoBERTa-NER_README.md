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
- RoBERTa
license: mit
---
# InstaFoodRoBERTa-NER

## Model description

**InstaFoodRoBERTa-NER** is a fine-tuned BERT model that is ready to use for **Named Entity Recognition** of Food entities on informal text (social media like). It has been trained to recognize a single entity: food (FOOD).

Specifically, this model is a *roberta-base* model that was fine-tuned on a dataset consisting of 400 English Instagram posts related to food. The [dataset](https://huggingface.co/datasets/Dizex/InstaFoodSet) is open source.


## Intended uses

#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Dizex/InstaFoodRoBERTa-NER")
model = AutoModelForTokenClassification.from_pretrained("Dizex/InstaFoodRoBERTa-NER")

pipe = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Today's meal: Fresh olive poké bowl topped with chia seeds. Very delicious!"

ner_entity_results = pipe(example, aggregation_strategy="simple")
print(ner_entity_results)
```

To get the extracted food entities as strings you can use the following code:

```python
def convert_entities_to_list(text, entities: list[dict]) -> list[str]:
        ents = []
        for ent in entities:
            e = {"start": ent["start"], "end": ent["end"], "label": ent["entity_group"]}
            if ents and -1 <= ent["start"] - ents[-1]["end"] <= 1 and ents[-1]["label"] == e["label"]:
                ents[-1]["end"] = e["end"]
                continue
            ents.append(e)

        return [text[e["start"]:e["end"]] for e in ents]

print(convert_entities_to_list(example, ner_entity_results))
```

This will result in the following output:

```python
['olive poké bowl', 'chia seeds']
```



## Performance on [InstaFoodSet](https://huggingface.co/datasets/Dizex/InstaFoodSet)
metric|val
-|-
f1 |0.91
precision |0.89
recall |0.93

