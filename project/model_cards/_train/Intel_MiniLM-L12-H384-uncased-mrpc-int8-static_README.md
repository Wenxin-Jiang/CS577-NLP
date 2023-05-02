---
language: en
license: mit
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- PostTrainingStatic
datasets: 
- mrpc
metrics:
- f1
---

# INT8 MiniLM finetuned MRPC

## Post-training static quantization

### PyTorch

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 
The original fp32 model comes from the fine-tuned model [Intel/MiniLM-L12-H384-uncased-mrpc](https://huggingface.co/Intel/MiniLM-L12-H384-uncased-mrpc).

The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.

The linear module **bert.encoder.layer.6.attention.self.key** falls back to fp32 to meet the 1% relative accuracy loss.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9039|0.9097|
| **Model size (MB)**  |33.5|127|

#### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification 
int8_model = IncQuantizedModelForSequenceClassification(
    'Intel/MiniLM-L12-H384-uncased-mrpc-int8-static',
)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [Intel/MiniLM-L12-H384-uncased-mrpc](https://huggingface.co/Intel/MiniLM-L12-H384-uncased-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9137|0.9097|
| **Model size (MB)**  |120|128|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/MiniLM-L12-H384-uncased-mrpc-int8-static')
```