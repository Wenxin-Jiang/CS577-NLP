---
language: en
license: apache-2.0
datasets:
- sst2
- glue
metrics:
- accuracy
tags:
- text-classfication
- int8
- onnx
- Intel® Neural Compressor
---

# Dynamically quantized DistilBERT base uncased finetuned SST-2

## Table of Contents
- [Model Details](#model-details)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)

## Model Details
**Model Description:** This model is a [DistilBERT](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) fine-tuned on SST-2 dynamically quantized with [optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 
- **Model Type:** Text Classification
- **Language(s):** English
- **License:** Apache-2.0
- **Parent Model:** For more details on the original model, we encourage users to check out [this](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) model card.

## How to Get Started With the Model

### PyTorch

To load the quantized model, you can do as follows:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification

model = IncQuantizedModelForSequenceClassification.from_pretrained("Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-dynamic")
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [DistilBERT](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-accuracy)** |0.9037|0.9106|
| **Model size (MB)**  |73|256|

#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-dynamic')
```
