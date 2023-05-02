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
- glue
metrics:
- f1
---

# INT8 albert-base-v2-sst2

## Post-training dynamic quantization

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [Alireza1044/albert-base-v2-sst2](https://huggingface.co/Alireza1044/albert-base-v2-sst2).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-accuracy)** |0.9140|0.9232|
| **Model size (MB)**  |57|45|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/albert-base-v2-sst2-int8-dynamic')
```

