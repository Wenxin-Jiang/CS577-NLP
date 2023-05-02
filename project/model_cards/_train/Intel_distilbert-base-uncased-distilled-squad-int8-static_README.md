---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- PostTrainingStatic
- onnx
datasets: 
- squad
metrics:
- f1
---

# INT8 DistilBERT base uncased finetuned on Squad

## Post-training static quantization

### PyTorch

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [distilbert-base-uncased-distilled-squad](https://huggingface.co/distilbert-base-uncased-distilled-squad).

The calibration dataloader is the train dataloader. The default calibration sampling size 300 isn't divisible exactly by batch size 8, so the real sampling size is 304.

The linear module **distilbert.transformer.layer.1.ffn.lin2** falls back to fp32 to meet the 1% relative accuracy loss.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |86.1069|86.8374|
| **Model size (MB)**  |74.7|265|

#### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForQuestionAnswering
int8_model = IncQuantizedModelForQuestionAnswering(
    'Intel/distilbert-base-uncased-distilled-squad-int8-static',
)
```

### ONNX

This is an INT8 ONNX model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor).

The original fp32 model comes from the fine-tuned model [distilbert-base-uncased-distilled-squad](https://huggingface.co/distilbert-base-uncased-distilled-squad).

The calibration dataloader is the eval dataloader. The default calibration sampling size is 100.

#### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.8626|0.8687|
| **Model size (MB)**  |153|254|


#### Load ONNX model:

```python
from optimum.onnxruntime import ORTModelForQuestionAnswering
model = ORTModelForQuestionAnswering.from_pretrained('Intel/distilbert-base-uncased-distilled-squad-int8-static')
```