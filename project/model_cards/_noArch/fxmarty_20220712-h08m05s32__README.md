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
* **quantization_approach**: `dynamic`
* **node_exclusion**: `[]`
* **framework**: `onnxruntime`
* **framework_args**:
    * **opset**: `11`
    * **optimization_level**: `1`
* **aware_training**: `False`

Benchmarked parameters:
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`,  `[]`
* **per_channel**: `False`,  `True`

# Evaluation
## Non-time metrics
| operators_to_quantize | per_channel |     | accuracy (original) | accuracy (optimized) |
| :-------------------: | :---------: | :-: | :-----------------: | :------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |        0.980        |        0.980         |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |        0.980        |        0.980         |
|       `['Add']`       |   `False`   |  \|  |        0.980        |        0.980         |
|       `['Add']`       |   `True`    |  \|  |        0.980        |        0.980         |
|         `[]`          |   `False`   |  \|  |        0.980        |        0.980         |
|         `[]`          |   `True`    |  \|  |        0.980        |        0.980         |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           201.25            |            70.30             |  \|  |           5.00            |           14.27            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           203.52            |            72.48             |  \|  |           4.93            |           13.80            |
|       `['Add']`       |   `False`   |  \|  |           166.03            |            150.93            |  \|  |           6.07            |            6.67            |
|       `['Add']`       |   `True`    |  \|  |           200.82            |            163.17            |  \|  |           5.00            |            6.13            |
|         `[]`          |   `False`   |  \|  |           190.99            |            162.06            |  \|  |           5.27            |            6.20            |
|         `[]`          |   `True`    |  \|  |           155.15            |            162.52            |  \|  |           6.47            |            6.20            |


Below, time metrics for batch size = 1, input length = 64.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           165.85            |            70.60             |  \|  |           6.07            |           14.20            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           161.41            |            72.71             |  \|  |           6.20            |           13.80            |
|       `['Add']`       |   `False`   |  \|  |           200.45            |            129.40            |  \|  |           5.00            |            7.73            |
|       `['Add']`       |   `True`    |  \|  |           154.68            |            136.42            |  \|  |           6.47            |            7.40            |
|         `[]`          |   `False`   |  \|  |           166.97            |            162.15            |  \|  |           6.00            |            6.20            |
|         `[]`          |   `True`    |  \|  |           166.32            |            162.81            |  \|  |           6.07            |            6.20            |


Below, time metrics for batch size = 1, input length = 128.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           199.48            |            70.98             |  \|  |           5.07            |           14.13            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           199.65            |            71.78             |  \|  |           5.07            |           13.93            |
|       `['Add']`       |   `False`   |  \|  |           199.08            |            137.97            |  \|  |           5.07            |            7.27            |
|       `['Add']`       |   `True`    |  \|  |           189.93            |            162.45            |  \|  |           5.33            |            6.20            |
|         `[]`          |   `False`   |  \|  |           191.63            |            162.54            |  \|  |           5.27            |            6.20            |
|         `[]`          |   `True`    |  \|  |           200.38            |            162.55            |  \|  |           5.00            |            6.20            |


Below, time metrics for batch size = 4, input length = 32.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           655.84            |            243.33            |  \|  |           1.53            |            4.13            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           661.27            |            221.16            |  \|  |           1.53            |            4.53            |
|       `['Add']`       |   `False`   |  \|  |           662.84            |            529.28            |  \|  |           1.53            |            1.93            |
|       `['Add']`       |   `True`    |  \|  |           512.47            |            470.66            |  \|  |           2.00            |            2.13            |
|         `[]`          |   `False`   |  \|  |           562.81            |            501.77            |  \|  |           1.80            |            2.00            |
|         `[]`          |   `True`    |  \|  |           505.81            |            521.20            |  \|  |           2.00            |            1.93            |


Below, time metrics for batch size = 4, input length = 64.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           654.58            |            258.54            |  \|  |           1.53            |            3.93            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           617.44            |            234.05            |  \|  |           1.67            |            4.33            |
|       `['Add']`       |   `False`   |  \|  |           661.51            |            478.81            |  \|  |           1.53            |            2.13            |
|       `['Add']`       |   `True`    |  \|  |           657.01            |            660.23            |  \|  |           1.53            |            1.53            |
|         `[]`          |   `False`   |  \|  |           661.64            |            474.28            |  \|  |           1.53            |            2.13            |
|         `[]`          |   `True`    |  \|  |           661.29            |            471.09            |  \|  |           1.53            |            2.13            |


Below, time metrics for batch size = 4, input length = 128.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           654.80            |            219.38            |  \|  |           1.53            |            4.60            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           663.50            |            222.37            |  \|  |           1.53            |            4.53            |
|       `['Add']`       |   `False`   |  \|  |           625.56            |            529.02            |  \|  |           1.60            |            1.93            |
|       `['Add']`       |   `True`    |  \|  |           655.08            |            499.41            |  \|  |           1.53            |            2.07            |
|         `[]`          |   `False`   |  \|  |           655.92            |            473.01            |  \|  |           1.53            |            2.13            |
|         `[]`          |   `True`    |  \|  |           505.54            |            659.92            |  \|  |           2.00            |            1.53            |


Below, time metrics for batch size = 8, input length = 32.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           968.83            |            443.80            |  \|  |           1.07            |            2.27            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           1255.70           |            489.55            |  \|  |           0.80            |            2.07            |
|       `['Add']`       |   `False`   |  \|  |           1301.35           |            938.14            |  \|  |           0.80            |            1.07            |
|       `['Add']`       |   `True`    |  \|  |           1279.54           |            931.91            |  \|  |           0.80            |            1.13            |
|         `[]`          |   `False`   |  \|  |           1292.66           |           1318.07            |  \|  |           0.80            |            0.80            |
|         `[]`          |   `True`    |  \|  |           1290.35           |           1314.74            |  \|  |           0.80            |            0.80            |


Below, time metrics for batch size = 8, input length = 64.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           1305.45           |            438.06            |  \|  |           0.80            |            2.33            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           1296.68           |            450.40            |  \|  |           0.80            |            2.27            |
|       `['Add']`       |   `False`   |  \|  |           968.21            |            949.81            |  \|  |           1.07            |            1.07            |
|       `['Add']`       |   `True`    |  \|  |           1012.35           |           1317.46            |  \|  |           1.00            |            0.80            |
|         `[]`          |   `False`   |  \|  |           1213.91           |            961.79            |  \|  |           0.87            |            1.07            |
|         `[]`          |   `True`    |  \|  |           956.39            |            945.41            |  \|  |           1.07            |            1.07            |


Below, time metrics for batch size = 8, input length = 128.

| operators_to_quantize | per_channel |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :---------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|  `['Add', 'MatMul']`  |   `False`   |  \|  |           1120.12           |            497.17            |  \|  |           0.93            |            2.07            |
|  `['Add', 'MatMul']`  |   `True`    |  \|  |           1289.50           |            443.46            |  \|  |           0.80            |            2.27            |
|       `['Add']`       |   `False`   |  \|  |           1294.65           |            930.97            |  \|  |           0.80            |            1.13            |
|       `['Add']`       |   `True`    |  \|  |           1181.21           |            933.82            |  \|  |           0.87            |            1.13            |
|         `[]`          |   `False`   |  \|  |           1245.61           |           1318.07            |  \|  |           0.87            |            0.80            |
|         `[]`          |   `True`    |  \|  |           1285.81           |           1318.82            |  \|  |           0.80            |            0.80            |

