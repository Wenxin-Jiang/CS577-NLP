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
      value: 0.9224
---


# Quantized-distilbert-banking77

This model is a statically quantized version of [optimum/distilbert-base-uncased-finetuned-banking77](https://huggingface.co/optimum/distilbert-base-uncased-finetuned-banking77) on the `banking77` dataset.

The model was created using the [optimum-static-quantization](https://github.com/philschmid/optimum-static-quantization) notebook.

It achieves the following results on the evaluation set:

**Accuracy**

- Vanilla model: 92.5%
- Quantized model: 92.24%  

> The quantized model achieves 99.72% accuracy of the fp32 model

**Latency**

Payload sequence length: 128  
Instance type: AWS c6i.xlarge  

| latency | vanilla transformers | quantized optimum model | improvement |
|---------|----------------------|-------------------------|-------------|
| p95     | 75.69ms              | 26.75ms                 | 2.83x       |
| avg     | 57.52ms              | 24.86ms                 | 2.31x       |

## How to use

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import pipeline, AutoTokenizer

model = ORTModelForSequenceClassification.from_pretrained("philschmid/quantized-distilbert-banking77")
tokenizer = AutoTokenizer.from_pretrained("philschmid/quantized-distilbert-banking77")

remote_clx = pipeline("text-classification",model=model, tokenizer=tokenizer)

remote_clx("What is the exchange rate like on this app?")
```