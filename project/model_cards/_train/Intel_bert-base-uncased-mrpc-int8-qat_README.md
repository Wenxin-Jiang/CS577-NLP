---
language: en
license: apache-2.0
tags:
- text-classfication
- int8
- Intel® Neural Compressor
- QuantizationAwareTraining
datasets: 
- mrpc
metrics:
- f1
---

# INT8 BERT base uncased finetuned MRPC

### QuantizationAwareTraining

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [Intel/bert-base-uncased-mrpc](https://huggingface.co/Intel/bert-base-uncased-mrpc).

### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9142|0.9042|
| **Model size (MB)**  |107|418|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification 
int8_model = IncQuantizedModelForSequenceClassification(
    'Intel/bert-base-uncased-mrpc-int8-qat',
)
```

### Training hyperparameters
    
The following hyperparameters were used during training:
- learning_rate: 2e-05
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0
- train_batch_size: 8
- eval_batch_size: 8
- eval_steps: 100
- load_best_model_at_end: True
- metric_for_best_model: f1
- early_stopping_patience = 6
- early_stopping_threshold = 0.001
