---
license: mit
tags:
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingStatic
datasets: 
- mnli
metrics:
- accuracy
---

# INT8 RoBERT large finetuned on MNLI

### Post-training static quantization

This is an INT8  PyTorch model quantized with [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [roberta-large-mnli](https://huggingface.co/roberta-large-mnli).

The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.

The linear modules **roberta.encoder.layer.16.output.dense**, **roberta.encoder.layer.17.output.dense**, **roberta.encoder.layer.18.output.dense**, fall back to fp32 for less than 1% relative accuracy loss.

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-acc)** |89.8624|90.5960|
| **Model size (MB)**  |381M|1.4G|

### Load with Intel® Neural Compressor:

```python
from optimum.intel.neural_compressor import IncQuantizedModelForSequenceClassification

model_id = "Intel/roberta-base-squad2-int8-static"
int8_model = IncQuantizedModelForSequenceClassification.from_pretrained(model_id)
```
