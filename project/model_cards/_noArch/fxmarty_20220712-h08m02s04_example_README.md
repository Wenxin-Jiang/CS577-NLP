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
**Number of evaluation samples:** `All dataset`  

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
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |        0.936         |         0.935         |  \|  |       0.944       |       0.943        |  \|  |     0.940     |     0.939      |  \|  |        0.988        |        0.988         |
|       `dynamic`       |       `['Add']`       |  \|  |        0.936         |         0.936         |  \|  |       0.944       |       0.944        |  \|  |     0.940     |     0.940      |  \|  |        0.988        |        0.988         |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |        0.936         |         0.063         |  \|  |       0.944       |       0.246        |  \|  |     0.940     |     0.100      |  \|  |        0.988        |        0.343         |
|       `static`        |       `['Add']`       |  \|  |        0.936         |         0.050         |  \|  |       0.944       |       0.160        |  \|  |     0.940     |     0.076      |  \|  |        0.988        |        0.311         |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            46.38            |             9.96             |  \|  |           21.60           |           100.47           |
|       `dynamic`       |       `['Add']`       |  \|  |            36.59            |            13.98             |  \|  |           27.33           |           71.60            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            33.84            |            14.46             |  \|  |           29.60           |           69.20            |
|       `static`        |       `['Add']`       |  \|  |            33.23            |            20.11             |  \|  |           30.13           |           49.73            |


Below, time metrics for batch size = 1, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            58.92            |            19.68             |  \|  |           17.00           |           50.87            |
|       `dynamic`       |       `['Add']`       |  \|  |            58.59            |            24.81             |  \|  |           17.13           |           40.33            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            51.41            |            29.36             |  \|  |           19.47           |           34.07            |
|       `static`        |       `['Add']`       |  \|  |            44.22            |            38.56             |  \|  |           22.67           |           25.93            |


Below, time metrics for batch size = 1, input length = 128.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            72.38            |            36.47             |  \|  |           13.87           |           27.47            |
|       `dynamic`       |       `['Add']`       |  \|  |            70.21            |            46.30             |  \|  |           14.27           |           21.60            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            70.76            |            48.24             |  \|  |           14.13           |           20.80            |
|       `static`        |       `['Add']`       |  \|  |            72.47            |            71.10             |  \|  |           13.80           |           14.07            |


Below, time metrics for batch size = 4, input length = 32.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |            69.76            |            38.50             |  \|  |           14.40           |           26.00            |
|       `dynamic`       |       `['Add']`       |  \|  |            56.02            |            51.32             |  \|  |           17.87           |           19.53            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |            55.05            |            46.80             |  \|  |           18.20           |           21.40            |
|       `static`        |       `['Add']`       |  \|  |            71.03            |            56.82             |  \|  |           14.13           |           17.67            |


Below, time metrics for batch size = 4, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           119.91            |            61.51             |  \|  |           8.40            |           16.27            |
|       `dynamic`       |       `['Add']`       |  \|  |           108.43            |            105.65            |  \|  |           9.27            |            9.47            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           119.89            |            86.76             |  \|  |           8.40            |           11.53            |
|       `static`        |       `['Add']`       |  \|  |            96.99            |            102.03            |  \|  |           10.33           |            9.87            |


Below, time metrics for batch size = 4, input length = 128.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           219.78            |            123.71            |  \|  |           4.60            |            8.13            |
|       `dynamic`       |       `['Add']`       |  \|  |           220.13            |            187.21            |  \|  |           4.60            |            5.40            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           186.39            |            176.99            |  \|  |           5.40            |            5.67            |
|       `static`        |       `['Add']`       |  \|  |           219.57            |            203.71            |  \|  |           4.60            |            4.93            |


Below, time metrics for batch size = 8, input length = 32.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           118.32            |            59.22             |  \|  |           8.47            |           16.93            |
|       `dynamic`       |       `['Add']`       |  \|  |           116.52            |            80.17             |  \|  |           8.60            |           12.53            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           116.59            |            83.55             |  \|  |           8.60            |           12.00            |
|       `static`        |       `['Add']`       |  \|  |           115.81            |            126.53            |  \|  |           8.67            |            7.93            |


Below, time metrics for batch size = 8, input length = 64.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           172.71            |            117.89            |  \|  |           5.80            |            8.53            |
|       `dynamic`       |       `['Add']`       |  \|  |           166.05            |            156.99            |  \|  |           6.07            |            6.40            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           215.00            |            148.93            |  \|  |           4.67            |            6.73            |
|       `static`        |       `['Add']`       |  \|  |           214.55            |            200.16            |  \|  |           4.67            |            5.00            |


Below, time metrics for batch size = 8, input length = 128.

| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           403.69            |            307.36            |  \|  |           2.53            |            3.27            |
|       `dynamic`       |       `['Add']`       |  \|  |           372.85            |            317.53            |  \|  |           2.73            |            3.20            |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           352.18            |            320.85            |  \|  |           2.87            |            3.13            |
|       `static`        |       `['Add']`       |  \|  |           403.55            |            410.17            |  \|  |           2.53            |            2.47            |

