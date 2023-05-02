---
language:
- en
license: mit
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- PostTrainingStatic
- onnx
datasets:
- glue
metrics:
- f1
model-index:
- name: electra-small-discriminator-mrpc-int8-static
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
      value: 0.900709219858156
---

# INT8 electra-small-discriminator-mrpc

##  Post-training static quantization

### PyTorch

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [electra-small-discriminator-mrpc](https://huggingface.co/Intel/electra-small-discriminator-mrpc).

The calibration dataloader is the train dataloader. The default calibration sampling size 300 isn't divisible exactly by batch size 8, so
 the real sampling size is 304.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9007|0.8983|
| **Model size (MB)**  |14|51.8|

#### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(
    'Intel/electra-small-discriminator-mrpc-int8-static',
)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [electra-small-discriminator-mrpc](https://huggingface.co/Intel/electra-small-discriminator-mrpc).

The calibration dataloader is the eval dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8. So the real sampling size is 104.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8993|0.8983|
| **Model size (MB)**  |32|52|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/electra-small-discriminator-mrpc-int8-static')
```
