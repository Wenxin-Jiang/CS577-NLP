---
pipeline_tag: image-classification
datasets:
- beans
metrics:
- accuracy
tags:
- vit
---

**task**: `image-classification`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.g4dn.2xlarge', 'supported_instructions': None}`  
**Number of evaluation samples:** `All dataset`  

Fixed parameters:
* **model_name_or_path**: `nateraw/vit-base-beans`
* **dataset**:
    * **path**: `beans`
    * **eval_split**: `validation`
    * **data_keys**: `{'primary': 'image'}`
    * **ref_keys**: `['labels']`
    * **calibration_split**: `train`
* **quantization_approach**: `dynamic`
* **calibration**:
    * **method**: `minmax`
    * **num_calibration_samples**: `100`
* **framework**: `onnxruntime`
* **framework_args**:
    * **opset**: `11`
    * **optimization_level**: `1`
* **aware_training**: `False`

Benchmarked parameters:
* **operators_to_quantize**: `['Add']`,  `['Add', 'MatMul']`
* **node_exclusion**: `[]`,  `['layernorm', 'gelu', 'residual', 'gather', 'softmax']`
* **per_channel**: `False`,  `True`

# Evaluation
## Non-time metrics
| operators_to_quantize |                      node_exclusion                      | per_channel |     | accuracy (original) | accuracy (optimized) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-----------------: | :------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |        0.980        |        0.980         |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |        0.980        |        0.980         |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |        0.980        |        0.980         |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |        0.980        |        0.980         |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |        0.980        |        0.980         |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |        0.980        |        0.980         |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |        0.980        |        0.980         |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |        0.980        |        0.980         |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           200.50            |            63.00             |  \|  |           5.00            |           15.93            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           198.19            |            72.65             |  \|  |           5.07            |           13.80            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           191.44            |            63.27             |  \|  |           5.27            |           15.87            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           154.84            |            72.51             |  \|  |           6.47            |           13.80            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           155.84            |            130.95            |  \|  |           6.47            |            7.67            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           201.76            |            131.25            |  \|  |           5.00            |            7.67            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           198.96            |            128.82            |  \|  |           5.07            |            7.80            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           163.76            |            129.62            |  \|  |           6.13            |            7.73            |


Below, time metrics for batch size = 1, input length = 64.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           162.75            |            67.18             |  \|  |           6.20            |           14.93            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           159.69            |            72.77             |  \|  |           6.33            |           13.80            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           183.10            |            64.02             |  \|  |           5.47            |           15.67            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           157.21            |            64.16             |  \|  |           6.40            |           15.60            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           155.32            |            130.74            |  \|  |           6.47            |            7.67            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           198.56            |            162.51            |  \|  |           5.07            |            6.20            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           186.58            |            163.38            |  \|  |           5.40            |            6.13            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           199.75            |            131.46            |  \|  |           5.07            |            7.67            |


Below, time metrics for batch size = 1, input length = 128.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           160.58            |            67.65             |  \|  |           6.27            |           14.80            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           158.60            |            72.53             |  \|  |           6.33            |           13.80            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           200.46            |            62.95             |  \|  |           5.00            |           15.93            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           195.39            |            72.28             |  \|  |           5.13            |           13.87            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           197.59            |            128.80            |  \|  |           5.07            |            7.80            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           156.24            |            162.63            |  \|  |           6.47            |            6.20            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           157.25            |            129.13            |  \|  |           6.40            |            7.80            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           176.08            |            161.79            |  \|  |           5.73            |            6.20            |


Below, time metrics for batch size = 4, input length = 32.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           503.83            |            219.62            |  \|  |           2.00            |            4.60            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           603.26            |            266.15            |  \|  |           1.67            |            3.80            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           654.79            |            217.45            |  \|  |           1.53            |            4.60            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           654.33            |            219.54            |  \|  |           1.53            |            4.60            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           654.20            |            481.61            |  \|  |           1.53            |            2.13            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           609.81            |            632.73            |  \|  |           1.67            |            1.60            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           588.86            |            602.91            |  \|  |           1.73            |            1.67            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           666.98            |            655.32            |  \|  |           1.53            |            1.53            |


Below, time metrics for batch size = 4, input length = 64.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           656.87            |            216.32            |  \|  |           1.53            |            4.67            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           507.24            |            265.62            |  \|  |           2.00            |            3.80            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           655.36            |            219.61            |  \|  |           1.53            |            4.60            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           613.28            |            220.96            |  \|  |           1.67            |            4.53            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           656.30            |            652.72            |  \|  |           1.53            |            1.53            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           521.09            |            472.90            |  \|  |           1.93            |            2.13            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           655.37            |            473.77            |  \|  |           1.53            |            2.13            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           653.62            |            468.82            |  \|  |           1.53            |            2.13            |


Below, time metrics for batch size = 4, input length = 128.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           654.24            |            216.82            |  \|  |           1.53            |            4.67            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           657.16            |            240.11            |  \|  |           1.53            |            4.20            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           504.14            |            217.47            |  \|  |           2.00            |            4.60            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           655.94            |            220.12            |  \|  |           1.53            |            4.60            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           653.99            |            479.06            |  \|  |           1.53            |            2.13            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           642.48            |            666.28            |  \|  |           1.60            |            1.53            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           656.34            |            661.24            |  \|  |           1.53            |            1.53            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           661.86            |            472.49            |  \|  |           1.53            |            2.13            |


Below, time metrics for batch size = 8, input length = 32.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           1294.07           |            472.54            |  \|  |           0.80            |            2.13            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           1287.58           |            542.72            |  \|  |           0.80            |            1.87            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           1033.37           |            433.32            |  \|  |           1.00            |            2.33            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           1030.14           |            542.36            |  \|  |           1.00            |            1.87            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           953.27            |            926.14            |  \|  |           1.07            |            1.13            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           1173.01           |            995.22            |  \|  |           0.87            |            1.07            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           1280.07           |            926.97            |  \|  |           0.80            |            1.13            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           1283.70           |            927.87            |  \|  |           0.80            |            1.13            |


Below, time metrics for batch size = 8, input length = 64.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           1273.61           |            435.27            |  \|  |           0.80            |            2.33            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           1157.00           |            542.75            |  \|  |           0.87            |            1.87            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           968.85            |            537.65            |  \|  |           1.07            |            1.87            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           1107.66           |            472.53            |  \|  |           0.93            |            2.13            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           1270.30           |           1092.10            |  \|  |           0.80            |            0.93            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           1263.29           |           1012.66            |  \|  |           0.80            |            1.00            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           1007.19           |           1331.12            |  \|  |           1.07            |            0.80            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           1286.51           |           1317.96            |  \|  |           0.80            |            0.80            |


Below, time metrics for batch size = 8, input length = 128.

| operators_to_quantize |                      node_exclusion                      | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :------------------------------------------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           1188.98           |            537.58            |  \|  |           0.87            |            1.87            |
|  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           951.31            |            489.40            |  \|  |           1.07            |            2.07            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   |  \|  |           1278.73           |            537.52            |  \|  |           0.80            |            1.87            |
|  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    |  \|  |           1005.38           |            440.01            |  \|  |           1.07            |            2.33            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   |  \|  |           1265.55           |           1304.51            |  \|  |           0.80            |            0.80            |
|       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    |  \|  |           1186.54           |            934.09            |  \|  |           0.87            |            1.13            |
|       `['Add']`       |                           `[]`                           |   `False`   |  \|  |           1276.38           |           1319.84            |  \|  |           0.80            |            0.80            |
|       `['Add']`       |                           `[]`                           |   `True`    |  \|  |           981.81            |            940.69            |  \|  |           1.07            |            1.07            |

