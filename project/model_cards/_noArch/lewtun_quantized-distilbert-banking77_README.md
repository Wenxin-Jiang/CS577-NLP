---
tags:
- optimum
datasets:
- banking77
metrics:
- accuracy
model-index:
- name: quantized-distilbert-banking77
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: banking77
      type: banking77
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9244
---


# Quantized-distilbert-banking77

This model is a dynamically quantized version of [optimum/distilbert-base-uncased-finetuned-banking77](https://huggingface.co/optimum/distilbert-base-uncased-finetuned-banking77) on the `banking77` dataset.

The model was created using the [dynamic-quantization](https://github.com/huggingface/workshops/tree/main/mlops-world) notebook from a workshop presented at MLOps World 2022.

It achieves the following results on the evaluation set:

**Accuracy**

- Vanilla model: 92.5%
- Quantized model: 92.44%  

> The quantized model achieves 99.93% accuracy of the FP32 model

**Latency**

Payload sequence length: 128  
Instance type: AWS c6i.xlarge  

| latency | vanilla transformers | quantized optimum model | improvement |
|---------|----------------------|-------------------------|-------------|
| p95     | 63.24ms              | 37.06ms                 | 1.71x       |
| avg     | 62.87ms              | 37.93ms                 | 1.66x       |

## How to use

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import pipeline, AutoTokenizer

model = ORTModelForSequenceClassification.from_pretrained("lewtun/quantized-distilbert-banking77")
tokenizer = AutoTokenizer.from_pretrained("lewtun/quantized-distilbert-banking77")

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
classifier("What is the exchange rate like on this app?")
```