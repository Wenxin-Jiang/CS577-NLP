---
language: en
license: mit
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

# INT8 MiniLM finetuned MRPC

### QuantizationAwareTraining

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [Intel/MiniLM-L12-H384-uncased-mrpc](https://huggingface.co/Intel/MiniLM-L12-H384-uncased-mrpc).

### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-f1)** |0.9068|0.9097|
| **Model size (MB)**  |33.1|127|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSequenceClassification 
int8_model = IncQuantizedModelForSequenceClassification(
    'Intel/MiniLM-L12-H384-uncased-mrpc-int8-qat',
)
```

### Training hyperparameters
    
The following hyperparameters were used during training:
- learning_rate: 1e-05
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0
- train_batch_size: 16
- eval_batch_size: 8
