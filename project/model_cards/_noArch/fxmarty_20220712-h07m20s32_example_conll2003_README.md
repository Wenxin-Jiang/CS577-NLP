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
**Backend args:** `{'instance_type': 'ml.g4dn.2xlarge', 'supported_instructions': 'avx512_vnni'}`  
**Number of evaluation samples:** `1000`  

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
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |        0.937         |         0.937         |  \|  |       0.953       |       0.953        |  \|  |     0.945     |     0.945      |  \|  |        0.988        |        0.988         |
|       `dynamic`       |       `['Add']`       |  \|  |        0.937         |         0.937         |  \|  |       0.953       |       0.953        |  \|  |     0.945     |     0.945      |  \|  |        0.988        |        0.988         |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |        0.937         |         0.074         |  \|  |       0.953       |       0.253        |  \|  |     0.945     |     0.114      |  \|  |        0.988        |        0.363         |
|       `static`        |       `['Add']`       |  \|  |        0.937         |         0.065         |  \|  |       0.953       |       0.186        |  \|  |     0.945     |     0.096      |  \|  |        0.988        |        0.340         |

## Time metrics
Time benchmarks were run for 3 seconds per config.


Below, time metrics for batch size = 1, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            57.64            |            12.30             |  \|  |           17.67           |           81.33            |
|       `dynamic`       |       `['Add']`       |  \|  |            43.51            |            29.42             |  \|  |           23.00           |           34.00            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            43.05            |            21.11             |  \|  |           23.33           |           47.67            |
|       `static`        |       `['Add']`       |  \|  |            43.50            |            37.93             |  \|  |           23.00           |           26.67            |


Below, time metrics for batch size = 4, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           119.50            |            39.92             |  \|  |           8.67            |           25.33            |
|       `dynamic`       |       `['Add']`       |  \|  |           119.62            |            107.42            |  \|  |           8.67            |            9.33            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           120.23            |            56.94             |  \|  |           8.33            |           17.67            |
|       `static`        |       `['Add']`       |  \|  |           119.10            |            130.78            |  \|  |           8.67            |            7.67            |


Below, time metrics for batch size = 8, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           165.84            |            75.45             |  \|  |           6.33            |           13.33            |
|       `dynamic`       |       `['Add']`       |  \|  |           214.65            |            211.41            |  \|  |           4.67            |            5.00            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           166.53            |            129.00            |  \|  |           6.33            |            8.00            |
|       `static`        |       `['Add']`       |  \|  |           214.81            |            256.95            |  \|  |           4.67            |            4.00            |

