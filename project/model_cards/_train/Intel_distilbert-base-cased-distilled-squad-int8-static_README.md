---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- PostTrainingStatic
datasets: 
- squad
metrics:
- f1
---

# INT8 DistilBERT base cased finetuned on Squad

### Post-training static quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [distilbert-base-cased-distilled-squad](https://huggingface.co/distilbert-base-cased-distilled-squad).

The calibration dataloader is the train dataloader. The default calibration sampling size 300 isn't divisible exactly by batch size 8, so the real sampling size is 304.

The linear module **distilbert.transformer.layer.1.ffn.lin2** falls back to fp32 to meet the 1% relative accuracy loss.

### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |86.0005|86.8373|
| **Model size (MB)**  |71.2|249|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForQuestionAnswering
int8_model = IncQuantizedModelForQuestionAnswering(
    'Intel/distilbert-base-cased-distilled-squad-int8-static',
)
```
