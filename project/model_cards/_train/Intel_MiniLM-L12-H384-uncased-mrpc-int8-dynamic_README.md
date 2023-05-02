---
language: en
license: mit
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

# INT8 MiniLM-L12-H384-uncased-mrpc

## Post-training dynamic quantization

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [Intel/MiniLM-L12-H384-uncased-mrpc](https://huggingface.co/Intel/MiniLM-L12-H384-uncased-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9107|0.9097|
| **Model size (MB)**  |33|128|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/MiniLM-L12-H384-uncased-mrpc-int8-dynamic')
```

