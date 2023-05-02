---
language: en
license: apache-2.0
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- PostTrainingDynamic
- onnx
datasets: 
- mrpc
metrics:
- f1
---

# INT8 BERT base uncased finetuned MRPC

## Post-training dynamic quantization

### PyTorch

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [Intel/bert-base-uncased-mrpc](https://huggingface.co/Intel/bert-base-uncased-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8997|0.9042|
| **Model size (MB)**  |174|418|

#### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(
    'Intel/bert-base-uncased-mrpc-int8-dynamic',
)
```

### ONNX


This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [Intel/bert-base-uncased-mrpc](https://huggingface.co/Intel/bert-base-uncased-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8958|0.9042|
| **Model size (MB)**  |107|418|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/bert-base-uncased-mrpc-int8-dynamic')
```

