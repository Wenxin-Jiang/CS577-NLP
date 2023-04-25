---
language: en
license: apache-2.0
datasets:
- sst2
- glue
tags:
- openvino
---

## [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) exported to the OpenVINO IR.

## Model Details
**Model Description:** This model is a fine-tune checkpoint of DistilBERT-base-uncased, fine-tuned on SST-2. This model reaches an accuracy of 91.3 on the dev set.

## Usage example

You can use this model with Transformers *pipeline*.

```python
from transformers import AutoTokenizer, pipeline
from optimum.intel.openvino import OVModelForSequenceClassification

model_id = "echarlaix/distilbert-base-uncased-finetuned-sst-2-english-openvino"
model = OVModelForSequenceClassification.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
cls_pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)
text = "He's a dreadful magician."
outputs = cls_pipe(text)
```
