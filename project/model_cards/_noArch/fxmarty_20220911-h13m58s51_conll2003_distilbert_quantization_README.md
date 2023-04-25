---
pipeline_tag: token-classification
datasets:
- conll2003
metrics:
- overall_precision
- overall_recall
- overall_f1
- overall_accuracy
- total_time_in_seconds
- samples_per_second
- latency_in_seconds
tags:
- distilbert
---

**task**: `token-classification`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.m5.2xlarge', 'supported_instructions': 'avx512'}`  
**Number of evaluation samples:** `All dataset`  

Fixed parameters:
* **dataset**: [{'path': 'conll2003', 'eval_split': 'validation', 'data_keys': {'primary': 'tokens'}, 'ref_keys': ['ner_tags'], 'name': None, 'calibration_split': 'train'}]
* **name_or_path**: `elastic/distilbert-base-uncased-finetuned-conll03-english`
* **from_transformers**: `True`
* **operators_to_quantize**: `['Add', 'MatMul']`
* **calibration**:
    * **method**: `percentile`
    * **num_calibration_samples**: `128`
    * **calibration_histogram_percentile**: `99.999`

Benchmarked parameters:
* **framework**: `onnxruntime`,  `pytorch`
* **quantization_approach**: `dynamic`,  `static`
* **node_exclusion**: `[]`,  `['layernorm', 'gelu', 'residual', 'gather', 'softmax']`
* **per_channel**: `False`,  `True`
* **framework_args**: `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}`,  `{}`
* **reduce_range**: `True`,  `False`
* **apply_quantization**: `True`,  `False`

# Evaluation
## Non-time metrics
|   framework   | quantization_approach |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | overall_precision |     | overall_recall |     | overall_f1 |     | overall_accuracy |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :------------: | :-: | :--------: | :-: | :--------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       0.936       |  \|  |     0.944      |  \|  |   0.940    |  \|  |      0.988       |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.935       |  \|  |     0.943      |  \|  |   0.939    |  \|  |      0.988       |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.926       |  \|  |     0.931      |  \|  |   0.929    |  \|  |      0.987       |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.000       |  \|  |     0.000      |  \|  |   0.000    |  \|  |      0.833       |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.934       |  \|  |     0.944      |  \|  |   0.939    |  \|  |      0.988       |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.935       |  \|  |     0.943      |  \|  |   0.939    |  \|  |      0.988       |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.926       |  \|  |     0.931      |  \|  |   0.929    |  \|  |      0.987       |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.000       |  \|  |     0.000      |  \|  |   0.000    |  \|  |      0.833       |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.934       |  \|  |     0.944      |  \|  |   0.939    |  \|  |      0.988       |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.913       |  \|  |     0.792      |  \|  |   0.848    |  \|  |      0.969       |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.913       |  \|  |     0.792      |  \|  |   0.848    |  \|  |      0.969       |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.000       |  \|  |     0.000      |  \|  |   0.000    |  \|  |      0.833       |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.896       |  \|  |     0.783      |  \|  |   0.836    |  \|  |      0.968       |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.925       |  \|  |     0.844      |  \|  |   0.883    |  \|  |      0.975       |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.925       |  \|  |     0.844      |  \|  |   0.883    |  \|  |      0.975       |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       0.045       |  \|  |     0.004      |  \|  |   0.008    |  \|  |      0.825       |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       0.922       |  \|  |     0.839      |  \|  |   0.879    |  \|  |      0.975       |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       0.936       |  \|  |     0.944      |  \|  |   0.940    |  \|  |      0.988       |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 32.

|   framework   | quantization_approach |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       14.22       |  \|  |      70.33      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.22       |  \|  |      97.87      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.16       |  \|  |      98.47      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.52       |  \|  |      95.07      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.70       |  \|  |      93.47      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.22       |  \|  |      97.87      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.24       |  \|  |      97.67      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.36       |  \|  |      96.53      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       10.50       |  \|  |      95.27      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       10.98       |  \|  |      91.07      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       11.31       |  \|  |      88.47      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       11.23       |  \|  |      89.07      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       11.48       |  \|  |      87.20      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       13.54       |  \|  |      73.87      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       13.74       |  \|  |      72.80      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       13.80       |  \|  |      72.53      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       14.08       |  \|  |      71.07      |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       31.23       |  \|  |      32.07      |


Below, time metrics for batch size = 1, input length = 64.

|   framework   | quantization_approach |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       24.52       |  \|  |      40.80      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       18.47       |  \|  |      54.20      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       18.53       |  \|  |      54.00      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       18.85       |  \|  |      53.07      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       19.14       |  \|  |      52.27      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       18.50       |  \|  |      54.07      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       18.50       |  \|  |      54.07      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       18.69       |  \|  |      53.53      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       19.46       |  \|  |      51.40      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       20.42       |  \|  |      49.00      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       19.91       |  \|  |      50.27      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       20.20       |  \|  |      49.53      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       20.74       |  \|  |      48.27      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       24.91       |  \|  |      40.20      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       24.35       |  \|  |      41.13      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       24.99       |  \|  |      40.07      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       24.95       |  \|  |      40.13      |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       41.31       |  \|  |      24.27      |


Below, time metrics for batch size = 1, input length = 128.

|   framework   | quantization_approach |                      node_exclusion                      | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :------------------------------------------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |                          `None`                          |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |       46.79       |  \|  |      21.40      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       35.84       |  \|  |      27.93      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.07       |  \|  |      28.53      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       35.71       |  \|  |      28.00      |
| `onnxruntime` |       `dynamic`       | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.91       |  \|  |      27.87      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       35.42       |  \|  |      28.27      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.22       |  \|  |      28.40      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       35.51       |  \|  |      28.20      |
| `onnxruntime` |       `dynamic`       |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       35.90       |  \|  |      27.87      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       39.88       |  \|  |      25.13      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       39.27       |  \|  |      25.47      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       39.37       |  \|  |      25.40      |
| `onnxruntime` |       `static`        | `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       39.16       |  \|  |      25.60      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       44.43       |  \|  |      22.53      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       46.13       |  \|  |      21.73      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |       45.48       |  \|  |      22.00      |
| `onnxruntime` |       `static`        |                           `[]`                           |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |       45.82       |  \|  |      21.87      |
|   `pytorch`   |        `None`         |                          `None`                          |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |       53.93       |  \|  |      18.60      |

