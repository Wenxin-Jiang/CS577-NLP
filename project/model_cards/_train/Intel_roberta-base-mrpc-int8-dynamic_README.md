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

# INT8 roberta base finetuned MRPC

## Post-training dynamic quantization

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [Intel/roberta-base-mrpc](https://huggingface.co/Intel/roberta-base-mrpc).

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9085|0.9138|
| **Model size (MB)**  |122|476|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/roberta-base-mrpc-int8-dynamic')
```

