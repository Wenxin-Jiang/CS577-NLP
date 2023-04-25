---
pipeline_tag: question-answering
datasets:
- squad
metrics:
- exact_match
- f1
tags:
- distilbert
---

**task**: `question-answering`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.g4dn.2xlarge', 'supported_instructions': None}`  
**Number of evaluation samples:** `1000`  

Fixed parameters:
* **model_name_or_path**: `distilbert-base-uncased-distilled-squad`
* **dataset**:
    * **path**: `squad`
    * **eval_split**: `validation`
    * **data_keys**: `{'question': 'question', 'context': 'context'}`
    * **ref_keys**: `['answers']`
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
| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | exact_match (original) | exact_match (optimized) |     | f1 (original) | f1 (optimized) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :--------------------: | :---------------------: | :-: | :-----------: | :------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |         82.300         |         80.600          |  \|  |    87.232     |     86.097     |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |         82.300         |         80.600          |  \|  |    87.232     |     86.097     |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |         82.300         |         82.300          |  \|  |    87.232     |     87.232     |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |         82.300         |         82.300          |  \|  |    87.232     |     87.232     |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |         82.300         |         72.900          |  \|  |    87.232     |     79.964     |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |         82.300         |         54.500          |  \|  |    87.232     |     64.292     |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |         82.300         |         76.900          |  \|  |    87.232     |     83.014     |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |         82.300         |         59.800          |  \|  |    87.232     |     69.217     |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            47.87            |             7.23             |  \|  |           20.93           |           138.40           |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            48.10            |             7.14             |  \|  |           20.80           |           140.13           |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            43.83            |            17.16             |  \|  |           22.87           |           58.33            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            34.13            |            17.02             |  \|  |           29.33           |           58.80            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            35.07            |             9.21             |  \|  |           28.53           |           108.53           |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            48.27            |            11.62             |  \|  |           20.73           |           86.13            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            34.11            |            19.23             |  \|  |           29.33           |           52.00            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            48.54            |            21.18             |  \|  |           20.67           |           47.27            |


Below, time metrics for batch size = 1, input length = 64.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            59.92            |            12.60             |  \|  |           16.73           |           79.40            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            59.64            |            13.25             |  \|  |           16.80           |           75.47            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            60.13            |            29.65             |  \|  |           16.67           |           33.73            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            59.62            |            29.51             |  \|  |           16.80           |           33.93            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            58.94            |            15.13             |  \|  |           17.00           |           66.13            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            60.49            |            18.62             |  \|  |           16.53           |           53.73            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            43.32            |            28.00             |  \|  |           23.13           |           35.73            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            44.19            |            32.72             |  \|  |           22.67           |           30.60            |


Below, time metrics for batch size = 1, input length = 128.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            73.39            |            26.56             |  \|  |           13.67           |           37.67            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            57.64            |            23.42             |  \|  |           17.40           |           42.73            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            64.04            |            50.14             |  \|  |           15.67           |           20.00            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            72.81            |            57.05             |  \|  |           13.80           |           17.53            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            70.57            |            27.59             |  \|  |           14.20           |           36.27            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            71.04            |            37.94             |  \|  |           14.13           |           26.40            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            57.65            |            57.95             |  \|  |           17.40           |           17.27            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            71.66            |            58.67             |  \|  |           14.00           |           17.07            |


Below, time metrics for batch size = 4, input length = 32.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            72.11            |            21.80             |  \|  |           13.93           |           45.93            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            73.15            |            20.70             |  \|  |           13.73           |           48.33            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            72.05            |            53.68             |  \|  |           13.93           |           18.67            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            55.97            |            53.60             |  \|  |           17.87           |           18.67            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            70.46            |            24.88             |  \|  |           14.20           |           40.20            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            56.57            |            30.90             |  \|  |           17.73           |           32.40            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            62.38            |            53.64             |  \|  |           16.07           |           18.67            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |            60.19            |            67.29             |  \|  |           16.67           |           14.87            |


Below, time metrics for batch size = 4, input length = 64.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           121.20            |            40.12             |  \|  |           8.27            |           24.93            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            90.97            |            41.51             |  \|  |           11.00           |           24.13            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           120.85            |            106.50            |  \|  |           8.33            |            9.40            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           118.58            |            106.55            |  \|  |           8.47            |            9.40            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           120.57            |            54.25             |  \|  |           8.33            |           18.47            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           104.93            |            57.90             |  \|  |           9.60            |           17.33            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            90.85            |            110.46            |  \|  |           11.07           |            9.07            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           120.57            |            103.62            |  \|  |           8.33            |            9.67            |


Below, time metrics for batch size = 4, input length = 128.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           172.14            |            94.78             |  \|  |           5.87            |           10.60            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           220.38            |            84.18             |  \|  |           4.60            |           11.93            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           221.22            |            221.37            |  \|  |           4.53            |            4.53            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           203.90            |            175.16            |  \|  |           4.93            |            5.73            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           192.63            |            113.82            |  \|  |           5.20            |            8.80            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           220.32            |            122.36            |  \|  |           4.60            |            8.20            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           220.58            |            207.51            |  \|  |           4.60            |            4.87            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           221.94            |            246.87            |  \|  |           4.53            |            4.07            |


Below, time metrics for batch size = 8, input length = 32.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           112.67            |            43.26             |  \|  |           8.93            |           23.13            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            95.78            |            40.66             |  \|  |           10.47           |           24.60            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           117.38            |            104.28            |  \|  |           8.53            |            9.60            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |            89.81            |            91.00             |  \|  |           11.20           |           11.00            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |            89.14            |            52.09             |  \|  |           11.27           |           19.20            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |            92.77            |            64.21             |  \|  |           10.80           |           15.60            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           119.10            |            114.43            |  \|  |           8.40            |            8.80            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           119.28            |            127.79            |  \|  |           8.40            |            7.87            |


Below, time metrics for batch size = 8, input length = 64.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           215.03            |            78.03             |  \|  |           4.67            |           12.87            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           214.76            |            87.19             |  \|  |           4.67            |           11.53            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           216.48            |            162.64            |  \|  |           4.67            |            6.20            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           204.29            |            212.33            |  \|  |           4.93            |            4.73            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           215.47            |            104.45            |  \|  |           4.67            |            9.60            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           209.66            |            106.43            |  \|  |           4.80            |            9.40            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           166.13            |            220.92            |  \|  |           6.07            |            4.53            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           214.69            |            209.01            |  \|  |           4.67            |            4.80            |


Below, time metrics for batch size = 8, input length = 128.

| quantization_approach | operators_to_quantize |                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :-------------------: | :-------------------: | :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           407.90            |            151.49            |  \|  |           2.47            |            6.67            |
|       `dynamic`       |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           407.34            |            154.55            |  \|  |           2.47            |            6.53            |
|       `dynamic`       |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           406.51            |            394.85            |  \|  |           2.47            |            2.60            |
|       `dynamic`       |       `['Add']`       |                           `[]`                           |  \|  |           309.53            |            445.24            |  \|  |           3.27            |            2.27            |
|       `static`        |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           407.54            |            224.46            |  \|  |           2.47            |            4.47            |
|       `static`        |  `['Add', 'MatMul']`  |                           `[]`                           |  \|  |           408.14            |            236.94            |  \|  |           2.47            |            4.27            |
|       `static`        |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           309.91            |            357.87            |  \|  |           3.27            |            2.80            |
|       `static`        |       `['Add']`       |                           `[]`                           |  \|  |           310.00            |            406.54            |  \|  |           3.27            |            2.47            |

