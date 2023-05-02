---
language:
- en
license: apache-2.0
tags:
- multiple-choice
- int8
- Intel® Neural Compressor
- PostTrainingStatic
datasets:
- swag
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-swag-int8-static
  results:
  - task:
      name: Multiple-choice
      type: multiple-choice
    dataset:
      name: Swag
      type: swag
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7838148474693298
---
# INT8 bert-base-uncased-finetuned-swag

###  Post-training static quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 
The original fp32 model comes from the fine-tuned model [thyagosme/bert-base-uncased-finetuned-swag](https://huggingface.co/thyagosme/bert-base-uncased-finetuned-swag).

The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.

The linear modules **bert.encoder.layer.2.output.dense, bert.encoder.layer.5.intermediate.dense, bert.encoder.layer.9.output.dense, bert.encoder.layer.10.output.dense** fall back to fp32 to meet the 1% relative accuracy loss.

### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-accuracy)** |0.7838|0.7915|
| **Model size (MB)**  |133|418|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForMultipleChoice
int8_model = IncQuantizedModelForMultipleChoice.from_pretrained(
    'Intel/bert-base-uncased-finetuned-swag-int8-static',
)
```
