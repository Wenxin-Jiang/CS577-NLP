---
pipeline_tag: token-classification
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
tags:
- distilbert
---

**task**: `token-classification`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.m5.2xlarge', 'supported_instructions': 'avx512'}`  
**Number of evaluation samples:** `100`  

Fixed parameters:
* **model_name_or_path**: `elastic/distilbert-base-uncased-finetuned-conll03-english`
* **dataset**:
    * **path**: `conll2003`
    * **eval_split**: `validation`
    * **data_keys**: `{'primary': 'tokens'}`
    * **ref_keys**: `['ner_tags']`
    * **calibration_split**: `train`
* **node_exclusion**: `[]`
* **per_channel**: `False`
* **calibration**:
    * **method**: `minmax`
    * **num_calibration_samples**: `100`
* **framework**: `onnxruntime`
* **framework_args**:
    * **opset**: `11`
    * **optimization_level**: `1`
* **aware_training**: `False`

Benchmarked parameters:
* **quantization_approach**: `dynamic`,  `static`
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`

# Evaluation
## Non-time metrics
| quantization_approach | operators_to_quantize |     | precision (original) | precision (optimized) |     | recall (original) | recall (optimized) |     | f1 (original) | f1 (optimized) |     | accuracy (original) | accuracy (optimized) |
| :-------------------: | :-------------------: | :-: | :------------------: | :-------------------: | :-: | :---------------: | :----------------: | :-: | :-----------: | :------------: | :-: | :-----------------: | :------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |        0.974         |         0.974         |  \|  |       0.955       |       0.949        |  \|  |     0.964     |     0.962      |  \|  |        0.990        |        0.989         |
|       `dynamic`       |       `['Add']`       |  \|  |        0.974         |         0.974         |  \|  |       0.955       |       0.955        |  \|  |     0.964     |     0.964      |  \|  |        0.990        |        0.990         |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |        0.974         |         0.081         |  \|  |       0.955       |       0.222        |  \|  |     0.964     |     0.118      |  \|  |        0.990        |        0.467         |
|       `static`        |       `['Add']`       |  \|  |        0.974         |         0.073         |  \|  |       0.955       |       0.182        |  \|  |     0.964     |     0.105      |  \|  |        0.990        |        0.290         |

## Time metrics
Time benchmarks were run for 3 seconds per config.


Below, time metrics for batch size = 1, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            59.35            |            21.91             |  \|  |           17.00           |           45.67            |
|       `dynamic`       |       `['Add']`       |  \|  |            59.18            |            29.24             |  \|  |           17.00           |           34.33            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            59.25            |            28.31             |  \|  |           17.00           |           35.33            |
|       `static`        |       `['Add']`       |  \|  |            58.77            |            31.80             |  \|  |           17.33           |           31.67            |

