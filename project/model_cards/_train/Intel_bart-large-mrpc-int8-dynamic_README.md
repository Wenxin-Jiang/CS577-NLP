---
language:
- en
license: apache-2.0
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- PostTrainingDynamic
- onnx
datasets:
- glue
metrics:
- f1
model-index:
- name: bart-large-mrpc-int8-dynamic
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - name: F1
      type: f1
      value: 0.9050847457627118
---
# INT8 bart-large-mrpc

##  Post-training dynamic quantization

### PyTorch

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [bart-large-mrpc](https://huggingface.co/Intel/bart-large-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9051|0.9120|
| **Model size (MB)**  |547|1556.48|

#### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(
    'Intel/bart-large-mrpc-int8-dynamic',
)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [bart-large-mrpc](https://huggingface.co/Intel/bart-large-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9134|0.9120|
| **Model size (MB)**  |395|1555|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/bart-large-mrpc-int8-dynamic')
```