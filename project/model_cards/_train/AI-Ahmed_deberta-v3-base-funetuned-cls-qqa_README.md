---
language:
- en
license: cc-by-4.0
tags:
- classification
datasets:
- SetFit/qqp
metrics:
- accuracy
- loss
thumbnail: https://github.com/AI-Ahmed
models:
- microsoft/deberta-v3-base
pipeline_tag: text-classification
widget:
- text: How is the life of a math student? Could you describe your own experiences?
    Which level of preparation is enough for the exam jlpt5?
  example_title: Difference Detection.
- text: What can one do after MBBS? What do i do after my MBBS?
  example_title: Duplicates Detection.
model-index:
- name: deberta-v3-base-funetuned-cls-qqa
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: qqp
      type: qqp
      config: sst2
      split: validation
    metrics:
    - type: accuracy
      value: 0.917969
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzA2OWM4ZjJkYzZjNmM3YmNkODNhODYzOTMxY2RjZTZmODg4ODA4ZjJmNjFhNjkwZjFmZjk3YjBiNzhjNDAzOCIsInZlcnNpb24iOjF9.TqdmhhV_3fTWYHtM7SJj35ICZgZ6Ux7qYXwPHu8j0MkDmSeZfTniFCqB8LO8pqM1bK5iHQV1-vggZUdMu4spCA
    - type: loss
      value: 0.21741
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGQzZGZjNzZjNzFjOWViNjkyNGIxMGE5ZjA5ODAxOTNiZGQ5OTY4NWM1YThlZGEyZGRjOGE2MjkwYTRjN2Q2MyIsInZlcnNpb24iOjF9.ZxmqxdbOhAA8Ywz8_Q3aFaFG2kmTogFdWjlHgEa2JnGQWhL39VVtcn6A8gtekE_e3z5jsaNS4EnSzYVSWJZjAQ
---

A fine-tuned model based on the **DeBERTaV3** model of Microsoft and fine-tuned on **Glue QQP**, which detects the linguistical similarities between two questions and whether they are duplicates questions or different.

## Model Hyperparameters

```python
epoch=4
per_device_train_batch_size=32
per_device_eval_batch_size=16
lr=2e-5
weight_decay=1e-2
gradient_checkpointing=True
gradient_accumulation_steps=8
```
## Model Performance

```JSON
{"Training Loss": 0.132400,
 "Validation Loss": 0.217410,
 "Validation Accuracy": 0.917969
}
```

## Model Dependencies

```JSON
{"Main Model": "microsoft/deberta-v3-base",
 "Dataset": "SetFit/qqp"
}
```

## Training Monitoring & Performance

- [wandb - deberta_qqa_classification](https://wandb.ai/ai-ahmed/deberta_qqa_classification?workspace=user-ai-ahmed)

## Model Testing

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
model_name = "AI-Ahmed/deberta-v3-base-funetuned-cls-qqa"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenized_input = tokenizer("How is the life of a math student? Could you describe your own experiences? Which level of preparation is enough for the exam jlpt5?", return_tensors="pt")

with torch.no_grad():
  logits = model(**tokenized_input).logits

predicted_class_id = logits.argmax().item()
model.config.id2label[predicted_class_id]
```

## Information Citation

```bibtex
@inproceedings{
he2021deberta,
title={DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION},
author={Pengcheng He and Xiaodong Liu and Jianfeng Gao and Weizhu Chen},
booktitle={International Conference on Learning Representations},
year={2021},
url={https://openreview.net/forum?id=XPZIaotutsD}
}
```