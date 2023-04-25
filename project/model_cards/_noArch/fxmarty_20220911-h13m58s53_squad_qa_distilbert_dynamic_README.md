---
pipeline_tag: question-answering
datasets:
- squad
metrics:
- exact_match
- f1
- total_time_in_seconds
- samples_per_second
- latency_in_seconds
tags:
- distilbert
---

**task**: `question-answering`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.m5.2xlarge', 'supported_instructions': 'avx512'}`  
**Number of evaluation samples:** `All dataset`  

Fixed parameters:
* **dataset**: [{'path': 'squad', 'eval_split': 'validation', 'data_keys': {'question': 'question', 'context': 'context'}, 'ref_keys': ['answers'], 'name': None, 'calibration_split': None}]
* **name_or_path**: `distilbert-base-uncased-distilled-squad`
* **from_transformers**: `True`
* **quantization_approach**: `dynamic`

Benchmarked parameters:
* **framework**: `onnxruntime`,  `pytorch`
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`
* **node_exclusion**: `[]`,  `['layernorm', 'gelu', 'residual', 'gather', 'softmax']`
* **per_channel**: `False`,  `True`
* **framework_args**: `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}`,  `{}`
* **reduce_range**: `True`,  `False`
* **apply_quantization**: `True`,  `False`

# Evaluation
## Non-time metrics
|   framework   | operators_to_quantize |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | exact_match |     |   f1   |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------: | :-: | :----: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |   76.764    |  \|  | 85.053 |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   69.622    |  \|  | 79.914 |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |    0.435    |  \|  | 5.887  |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   78.165    |  \|  | 85.973 |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |   76.764    |  \|  | 85.053 |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   69.622    |  \|  | 79.914 |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |    0.435    |  \|  | 5.887  |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   78.165    |  \|  | 85.973 |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |   78.884    |  \|  | 86.690 |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |   78.884    |  \|  | 86.690 |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

|   framework   | operators_to_quantize |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       14.26       |  \|  |      70.13      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.08       |  \|  |      99.20      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.60       |  \|  |      94.33      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.88       |  \|  |      91.93      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.84       |  \|  |      92.27      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.34       |  \|  |      96.73      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.41       |  \|  |      96.07      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.96       |  \|  |      91.27      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.69       |  \|  |      93.53      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       14.43       |  \|  |      69.33      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       14.52       |  \|  |      68.87      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       14.35       |  \|  |      69.73      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       14.50       |  \|  |      69.00      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       14.20       |  \|  |      70.47      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       14.24       |  \|  |      70.27      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       14.58       |  \|  |      68.67      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       14.73       |  \|  |      67.87      |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       31.49       |  \|  |      31.80      |


Below, time metrics for batch size = 1, input length = 64.

|   framework   | operators_to_quantize |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       24.83       |  \|  |      40.33      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       18.49       |  \|  |      54.13      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       18.87       |  \|  |      53.00      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       19.17       |  \|  |      52.20      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       18.92       |  \|  |      52.87      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       19.13       |  \|  |      52.33      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       18.95       |  \|  |      52.80      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       19.08       |  \|  |      52.47      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       19.14       |  \|  |      52.27      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       24.83       |  \|  |      40.33      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       24.84       |  \|  |      40.27      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       24.66       |  \|  |      40.60      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       24.76       |  \|  |      40.40      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       25.07       |  \|  |      39.93      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       25.27       |  \|  |      39.60      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       24.76       |  \|  |      40.40      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       24.70       |  \|  |      40.53      |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       41.26       |  \|  |      24.27      |


Below, time metrics for batch size = 1, input length = 128.

|   framework   | operators_to_quantize |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       46.89       |  \|  |      21.33      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       34.84       |  \|  |      28.73      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.88       |  \|  |      27.93      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       36.92       |  \|  |      27.13      |
| `onnxruntime` |  `['Add', 'MatMul']`  | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       36.25       |  \|  |      27.60      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       36.17       |  \|  |      27.67      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.59       |  \|  |      28.13      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       37.36       |  \|  |      26.80      |
| `onnxruntime` |  `['Add', 'MatMul']`  |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.97       |  \|  |      27.87      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       46.94       |  \|  |      21.33      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       47.19       |  \|  |      21.20      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       47.05       |  \|  |      21.27      |
| `onnxruntime` |       `['Add']`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       46.79       |  \|  |      21.40      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       46.87       |  \|  |      21.40      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       47.04       |  \|  |      21.27      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       47.08       |  \|  |      21.27      |
| `onnxruntime` |       `['Add']`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       47.05       |  \|  |      21.27      |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       54.61       |  \|  |      18.33      |

