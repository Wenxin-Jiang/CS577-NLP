---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- PostTrainingStatic
datasets: 
- imagenet-1k
metrics:
- accuracy
---

# The INT8 model based on vit-base-patch16-224 which finetuned on imagenet-1k

### Post-training static quantization

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224).

The calibration dataloader is the train dataloader. The default calibration sampling size 1000 because of 1000 classes of imagenet-1k.

The linear modules **vit.encoder.layer.5.output.dense**, **vit.encoder.layer.9.attention.attention.query.module**, fall back to fp32 for less than 1% relative accuracy loss.

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-acc)** |80.576|81.326|
| **Model size (MB)**  |94|331|

### Load with Intel® Neural Compressor:

```python
from neural_compressor.utils.load_huggingface import OptimizedModel
int8_model = OptimizedModel.from_pretrained(
    'Intel/vit-base-patch16-224-int8-static',
)
```
