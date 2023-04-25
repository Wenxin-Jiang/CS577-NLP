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
**Number of evaluation samples:** `10`  

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
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |        0.970         |         0.969         |  \|  |       0.970       |       0.939        |  \|  |     0.970     |     0.954      |  \|  |        0.993        |        0.990         |
|       `dynamic`       |       `['Add']`       |  \|  |        0.970         |         0.970         |  \|  |       0.970       |       0.970        |  \|  |     0.970     |     0.970      |  \|  |        0.993        |        0.993         |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |        0.970         |         0.104         |  \|  |       0.970       |       0.212        |  \|  |     0.970     |     0.140      |  \|  |        0.993        |        0.691         |
|       `static`        |       `['Add']`       |  \|  |        0.970         |         0.037         |  \|  |       0.970       |       0.121        |  \|  |     0.970     |     0.057      |  \|  |        0.993        |        0.110         |

## Time metrics
Time benchmarks were run for 3 seconds per config.


Below, time metrics for batch size = 1, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            60.12            |            18.13             |  \|  |           16.67           |           55.33            |
|       `dynamic`       |       `['Add']`       |  \|  |            59.49            |            29.12             |  \|  |           17.00           |           34.67            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            58.89            |            24.30             |  \|  |           17.00           |           41.33            |
|       `static`        |       `['Add']`       |  \|  |            43.19            |            38.12             |  \|  |           23.33           |           26.33            |

