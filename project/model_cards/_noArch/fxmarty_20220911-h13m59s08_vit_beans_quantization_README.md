---
pipeline_tag: image-classification
datasets:
- beans
metrics:
- accuracy
- total_time_in_seconds
- samples_per_second
- latency_in_seconds
tags:
- vit
---

**task**: `image-classification`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.m5.2xlarge', 'supported_instructions': 'avx512'}`  
**Number of evaluation samples:** `All dataset`  

Fixed parameters:
* **dataset**: [{'path': 'beans', 'eval_split': 'validation', 'data_keys': {'primary': 'image'}, 'ref_keys': ['labels'], 'name': None, 'calibration_split': 'train'}]
* **name_or_path**: `nateraw/vit-base-beans`
* **from_transformers**: `True`
* **node_exclusion**: `[]`
* **calibration**:
    * **method**: `percentile`
    * **num_calibration_samples**: `128`
    * **calibration_histogram_percentile**: `99.999`

Benchmarked parameters:
* **framework**: `onnxruntime`,  `pytorch`
* **quantization_approach**: `dynamic`,  `static`
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`
* **per_channel**: `False`,  `True`
* **framework_args**: `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}`,  `{}`
* **reduce_range**: `True`,  `False`
* **apply_quantization**: `True`,  `False`

# Evaluation
## Non-time metrics
|   framework   | quantization_approach | operators_to_quantize | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | accuracy |
| :-----------: | :-------------------: | :-------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :------: |
| `onnxruntime` |        `None`         |        `None`         |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.977   |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.421   |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.421   |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.316   |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.451   |
| `onnxruntime` |       `static`        |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.361   |
| `onnxruntime` |       `static`        |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.361   |
| `onnxruntime` |       `static`        |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |  0.361   |
| `onnxruntime` |       `static`        |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |  0.361   |
|   `pytorch`   |        `None`         |        `None`         |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |  0.977   |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 224.

|   framework   | quantization_approach | operators_to_quantize | per_channel |                           framework_args                            | reduce_range | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :-------------------: | :---------: | :-----------------------------------------------------------------: | :----------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |        `None`         |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `None`    |      `False`       |  \|  |      130.41       |  \|  |      7.73       |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      102.44       |  \|  |      9.80       |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      101.57       |  \|  |      9.87       |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      102.37       |  \|  |      9.80       |
| `onnxruntime` |       `dynamic`       |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      102.36       |  \|  |      9.80       |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      130.67       |  \|  |      7.67       |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      131.29       |  \|  |      7.67       |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      132.65       |  \|  |      7.60       |
| `onnxruntime` |       `dynamic`       |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      131.03       |  \|  |      7.67       |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      127.99       |  \|  |      7.87       |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      128.27       |  \|  |      7.80       |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      131.10       |  \|  |      7.67       |
| `onnxruntime` |       `static`        |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      130.29       |  \|  |      7.73       |
| `onnxruntime` |       `static`        |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      164.55       |  \|  |      6.13       |
| `onnxruntime` |       `static`        |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      168.61       |  \|  |      5.93       |
| `onnxruntime` |       `static`        |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |   `False`    |       `True`       |  \|  |      164.52       |  \|  |      6.13       |
| `onnxruntime` |       `static`        |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |    `True`    |       `True`       |  \|  |      165.31       |  \|  |      6.07       |
|   `pytorch`   |        `None`         |        `None`         |   `None`    |                                `{}`                                 |    `None`    |       `None`       |  \|  |      149.23       |  \|  |      6.73       |

