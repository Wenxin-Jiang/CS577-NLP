---
language:
- en
license: apache-2.0
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingStatic
datasets:
- glue
metrics:
- accuracy
model_index:
- name: sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9254587155963303
---
# INT8 albert-base-v2-sst2

##  Post-training static quantization

### PyTorch

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [Alireza1044/albert-base-v2-sst2](https://huggingface.co/Alireza1044/albert-base-v2-sst2).

The calibration dataloader is the train dataloader. The default calibration sampling size 300 isn't divisible exactly by batch size 8, so the real sampling size is 304.

The linear modules **albert.encoder.albert_layer_groups.0.albert_layers.0.ffn_output.module, albert.encoder.albert_layer_groups.0.albert_layers.0.ffn.module** fall back to fp32 to meet the 1% relative accuracy loss.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-accuracy)** |0.9255|0.9232|
| **Model size (MB)**  |25|44.6|

#### Load with Intel® Neural Compressor:

```python
from optimum.intel.neural_compressor import IncQuantizedModelForSequenceClassification

model_id = "Intel/albert-base-v2-sst2-int8-static"
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(model_id)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [Alireza1044/albert-base-v2-sst2](https://huggingface.co/Alireza1044/albert-base-v2-sst2).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-accuracy)** |0.9186|0.9232|
| **Model size (MB)**  |89|45|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/albert-base-v2-sst2-int8-static')
```