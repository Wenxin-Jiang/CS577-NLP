---
language:
- en
license: mit
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingStatic
datasets:
- glue
metrics:
- f1
model-index:
- name: roberta-base-mrpc-int8-static
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
      value: 0.924693520140105
---
# INT8 roberta-base-mrpc

##  Post-training static quantization

### PyTorch

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [roberta-base-mrpc](https://huggingface.co/Intel/roberta-base-mrpc).

The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9177|0.9138|
| **Model size (MB)**  |127|499|

#### Load with Intel® Neural Compressor:

```python
from optimum.intel.neural_compressor import IncQuantizedModelForSequenceClassification

model_id = "Intel/roberta-base-mrpc-int8-static"
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(model_id)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [roberta-base-mrpc](https://huggingface.co/Intel/roberta-base-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9073|0.9138|
| **Model size (MB)**  |243|476|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/roberta-base-mrpc-int8-static')
```