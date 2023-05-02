---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingStatic
datasets: 
- squad
metrics:
- f1
---

# INT8 BERT base uncased finetuned on Squad

### Post-training static quantization

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [jimypbr/bert-base-uncased-squad](https://huggingface.co/jimypbr/bert-base-uncased-squad).

The calibration dataloader is the train dataloader. The default calibration sampling size 300 isn't divisible exactly by batch size 8, so the real sampling size is 304.

The linear modules **bert.encoder.layer.2.intermediate.dense**, **bert.encoder.layer.4.intermediate.dense**, **bert.encoder.layer.9.output.dense**, **bert.encoder.layer.10.output.dense** fall back to fp32 to meet the 1% relative accuracy loss.

### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |87.3006|88.1030|
| **Model size (MB)**  |139|436|

### Load with Intel® Neural Compressor:

```python
from optimum.intel.neural_compressor import IncQuantizedModelForQuestionAnswering
int8_model = IncQuantizedModelForQuestionAnswering.from_pretrained(
    "Intel/bert-base-uncased-squad-int8-static",
)
```
