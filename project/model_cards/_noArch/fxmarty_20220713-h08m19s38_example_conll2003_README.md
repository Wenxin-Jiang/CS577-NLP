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
**Backend args:** `{'instance_type': 'ml.g4dn.2xlarge', 'supported_instructions': None}`  
**Number of evaluation samples:** `All dataset`  

Fixed parameters:
* **model_name_or_path**: `elastic/distilbert-base-uncased-finetuned-conll03-english`
* **dataset**:
    * **path**: `conll2003`
    * **eval_split**: `validation`
    * **data_keys**: `{'primary': 'tokens'}`
    * **ref_keys**: `['ner_tags']`
    * **calibration_split**: `train`
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
* **operators_to_quantize**: `['Add']`,  `['Add', 'MatMul']`
* **node_exclusion**: `[]`,  `['layernorm', 'gelu', 'residual', 'gather', 'softmax']`

# Evaluation
## Non-time metrics
| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | precision (original) | precision (optimized) |     | recall (original) | recall (optimized) |     | f1 (original) | f1 (optimized) |     | accuracy (original) | accuracy (optimized) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :------------------: | :-------------------: | :-: | :---------------: | :----------------: | :-: | :-----------: | :------------: | :-: | :-----------------: | :------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |        0.936         |         0.934         |  \|  |       0.944       |       0.942        |  \|  |     0.940     |     0.938      |  \|  |        0.988        |        0.988         |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |        0.936         |         0.934         |  \|  |       0.944       |       0.942        |  \|  |     0.940     |     0.938      |  \|  |        0.988        |        0.988         |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |        0.936         |         0.936         |  \|  |       0.944       |       0.944        |  \|  |     0.940     |     0.940      |  \|  |        0.988        |        0.988         |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |        0.936         |         0.936         |  \|  |       0.944       |       0.944        |  \|  |     0.940     |     0.940      |  \|  |        0.988        |        0.988         |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |        0.936         |         0.904         |  \|  |       0.944       |       0.921        |  \|  |     0.940     |     0.912      |  \|  |        0.988        |        0.984         |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |        0.936         |         0.065         |  \|  |       0.944       |       0.243        |  \|  |     0.940     |     0.103      |  \|  |        0.988        |        0.357         |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |        0.936         |         0.909         |  \|  |       0.944       |       0.930        |  \|  |     0.940     |     0.919      |  \|  |        0.988        |        0.986         |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |        0.936         |         0.050         |  \|  |       0.944       |       0.160        |  \|  |     0.940     |     0.076      |  \|  |        0.988        |        0.311         |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            32.90            |             7.03             |  \|  |           30.40           |           142.20           |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            48.27            |             7.68             |  \|  |           20.73           |           130.33           |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            33.74            |            14.73             |  \|  |           29.67           |           67.93            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            33.49            |            14.17             |  \|  |           29.87           |           70.60            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            47.72            |             8.20             |  \|  |           21.00           |           121.93           |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            47.87            |            10.58             |  \|  |           20.93           |           94.60            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            45.77            |            19.00             |  \|  |           21.87           |           52.67            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            44.67            |            18.77             |  \|  |           22.40           |           53.33            |


Below, time metrics for batch size = 1, input length = 64.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            59.15            |            13.60             |  \|  |           16.93           |           73.53            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            44.01            |            12.60             |  \|  |           22.73           |           79.40            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            60.50            |            29.87             |  \|  |           16.53           |           33.53            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            45.35            |            24.10             |  \|  |           22.07           |           41.53            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            59.98            |            16.08             |  \|  |           16.73           |           62.20            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            43.23            |            19.02             |  \|  |           23.20           |           52.60            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            43.15            |            32.96             |  \|  |           23.20           |           30.40            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            44.01            |            31.68             |  \|  |           22.80           |           31.60            |


Below, time metrics for batch size = 1, input length = 128.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            55.20            |            25.72             |  \|  |           18.13           |           38.93            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            73.52            |            26.70             |  \|  |           13.67           |           37.47            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            71.60            |            53.26             |  \|  |           14.00           |           18.80            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            70.39            |            56.68             |  \|  |           14.27           |           17.67            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            71.34            |            31.75             |  \|  |           14.07           |           31.53            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            73.55            |            37.95             |  \|  |           13.60           |           26.40            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            70.28            |            62.70             |  \|  |           14.27           |           16.00            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            63.86            |            61.64             |  \|  |           15.67           |           16.27            |


Below, time metrics for batch size = 4, input length = 32.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            70.41            |            22.67             |  \|  |           14.27           |           44.13            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            71.65            |            21.44             |  \|  |           14.00           |           46.67            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            71.72            |            55.16             |  \|  |           14.00           |           18.13            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            55.56            |            43.87             |  \|  |           18.00           |           22.80            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            55.45            |            27.83             |  \|  |           18.07           |           36.00            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            66.57            |            34.45             |  \|  |           15.07           |           29.07            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            55.23            |            59.31             |  \|  |           18.13           |           16.87            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            58.80            |            66.03             |  \|  |           17.07           |           15.20            |


Below, time metrics for batch size = 4, input length = 64.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           117.71            |            43.93             |  \|  |           8.53            |           22.80            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            90.01            |            43.27             |  \|  |           11.13           |           23.13            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            94.34            |            107.02            |  \|  |           10.60           |            9.40            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           119.11            |            82.46             |  \|  |           8.40            |           12.13            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           120.57            |            54.70             |  \|  |           8.33            |           18.33            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           120.00            |            57.85             |  \|  |           8.40            |           17.33            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           119.57            |            92.50             |  \|  |           8.40            |           10.87            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           117.35            |            102.09            |  \|  |           8.53            |            9.80            |


Below, time metrics for batch size = 4, input length = 128.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           220.69            |            94.33             |  \|  |           4.53            |           10.67            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           170.04            |            81.68             |  \|  |           5.93            |           12.27            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           188.59            |            171.79            |  \|  |           5.33            |            5.87            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           219.80            |            163.62            |  \|  |           4.60            |            6.13            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           220.25            |            94.05             |  \|  |           4.60            |           10.67            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           222.90            |            135.06            |  \|  |           4.53            |            7.47            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           177.41            |            211.89            |  \|  |           5.67            |            4.73            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           168.30            |            201.88            |  \|  |           6.00            |            5.00            |


Below, time metrics for batch size = 8, input length = 32.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           106.46            |            42.35             |  \|  |           9.47            |           23.67            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            88.68            |            43.33             |  \|  |           11.33           |           23.13            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            91.32            |            92.08             |  \|  |           11.00           |           10.87            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            88.33            |            94.18             |  \|  |           11.33           |           10.67            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           107.47            |            44.74             |  \|  |           9.33            |           22.40            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           118.39            |            64.56             |  \|  |           8.47            |           15.53            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            87.05            |            111.36            |  \|  |           11.53           |            9.00            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           116.96            |            98.82             |  \|  |           8.60            |           10.13            |


Below, time metrics for batch size = 8, input length = 64.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           165.67            |            87.71             |  \|  |           6.07            |           11.47            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           214.59            |            87.88             |  \|  |           4.67            |           11.40            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           216.06            |            163.75            |  \|  |           4.67            |            6.13            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           176.69            |            209.28            |  \|  |           5.67            |            4.80            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           215.12            |            86.90             |  \|  |           4.67            |           11.53            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           215.99            |            130.39            |  \|  |           4.67            |            7.73            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           213.87            |            224.50            |  \|  |           4.73            |            4.47            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           211.16            |            193.01            |  \|  |           4.80            |            5.20            |


Below, time metrics for batch size = 8, input length = 128.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           391.16            |            183.35            |  \|  |           2.60            |            5.47            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           414.42            |            154.52            |  \|  |           2.47            |            6.53            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           314.12            |            323.94            |  \|  |           3.20            |            3.13            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           408.15            |            325.03            |  \|  |           2.47            |            3.13            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           337.57            |            205.59            |  \|  |           3.00            |            4.87            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           375.10            |            225.09            |  \|  |           2.67            |            4.47            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           409.68            |            493.00            |  \|  |           2.47            |            2.07            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           397.28            |            397.74            |  \|  |           2.53            |            2.53            |

