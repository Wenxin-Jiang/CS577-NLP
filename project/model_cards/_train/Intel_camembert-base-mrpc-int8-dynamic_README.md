---
language:
- en
license: mit
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingDynamic
- onnx
datasets:
- glue
metrics:
- f1
model-index:
- name: camembert-base-mrpc-int8-dynamic
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
      value: 0.8842832469775476
---
# INT8 camembert-base-mrpc

##  Post-training dynamic quantization

### PyTorch

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [camembert-base-mrpc](https://huggingface.co/Intel/camembert-base-mrpc).

The linear module **roberta.encoder.layer.6.attention.self.query** falls back to fp32 to meet the 1% relative accuracy loss.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8843|0.8928|
| **Model size (MB)**  |180|422|

#### Load with Intel® Neural Compressor:

```python
from optimum.intel.neural_compressor import IncQuantizedModelForSequenceClassification

model_id = "Intel/camembert-base-mrpc-int8-dynamic"
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(model_id)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [camembert-base-mrpc](https://huggingface.co/Intel/camembert-base-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8847|0.8928|
| **Model size (MB)**  |115|423|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/camembert-base-mrpc-int8-dynamic')
```
