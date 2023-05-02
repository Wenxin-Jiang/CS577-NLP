---
language:
- en
license: mit
tags:
- text-classfication
- int8
- neural-compressor
- Intel® Neural Compressor
- PostTrainingStatic
- onnx
datasets:
- glue
metrics:
- f1
model-index:
- name: xlnet-base-cased-mrpc-int8-static
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
      value: 0.8892794376098417
---
# INT8 xlnet-base-cased-mrpc

## Post-training static quantization

### PyTorch

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [xlnet-base-cased-mrpc](https://huggingface.co/Intel/xlnet-base-cased-mrpc).

The calibration dataloader is the train dataloader. The default calibration sampling size 300 isn't divisible exactly by batch size 8, so the real sampling size is 304.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8893|0.8897|
| **Model size (MB)**  |215|448|

#### Load with Intel® Neural Compressor:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification

int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(
    "Intel/xlnet-base-cased-mrpc-int8-static",
)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [xlnet-base-cased-mrpc](https://huggingface.co/Intel/xlnet-base-cased-mrpc).

The calibration dataloader is the eval dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8. So the real sampling size is 104.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8935|0.8986|
| **Model size (MB)**  |286|448|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model = ORTModelForSequenceClassification.from_pretrained('Intel/xlnet-base-cased-mrpc-int8-static')
```

