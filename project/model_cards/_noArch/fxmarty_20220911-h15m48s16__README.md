---
pipeline_tag: text-classification
datasets:
- glue
metrics:
- accuracy
- total_time_in_seconds
- samples_per_second
- latency_in_seconds
tags:
- distilbert
---

**task**: `text-classification`  
**Backend:** `sagemaker-training`  
**Backend args:** `{'instance_type': 'ml.m5.2xlarge', 'supported_instructions': 'avx512'}`  
**Number of evaluation samples:** `All dataset`  

Fixed parameters:
* **dataset**: [{'path': 'glue', 'eval_split': 'validation', 'data_keys': {'primary': 'sentence'}, 'ref_keys': ['label'], 'name': 'sst2', 'calibration_split': None}]
* **name_or_path**: `distilbert-base-uncased-finetuned-sst-2-english`
* **from_transformers**: `True`
* **quantization_approach**: `dynamic`
* **node_exclusion**: `[]`

Benchmarked parameters:
* **framework**: `onnxruntime`,  `pytorch`
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`
* **per_channel**: `False`,  `True`
* **framework_args**: `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}`,  `{}`
* **apply_quantization**: `True`,  `False`

# Evaluation
## Non-time metrics
|   framework   | operators_to_quantize | per_channel |                           framework_args                            | apply_quantization |     | accuracy |
| :-----------: | :-------------------: | :---------: | :-----------------------------------------------------------------: | :----------------: | :-: | :------: |
| `onnxruntime` |        `None`         |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |      `False`       |  \|  |  0.911   |
| `onnxruntime` |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |  0.898   |
| `onnxruntime` |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |  0.490   |
| `onnxruntime` |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |  0.911   |
| `onnxruntime` |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |  0.911   |
|   `pytorch`   |        `None`         |   `None`    |                                `{}`                                 |       `None`       |  \|  |  0.911   |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 1, input length = 224.

|   framework   | operators_to_quantize | per_channel |                           framework_args                            | apply_quantization |     | latency_mean (ms) |     | throughput (/s) |
| :-----------: | :-------------------: | :---------: | :-----------------------------------------------------------------: | :----------------: | :-: | :---------------: | :-: | :-------------: |
| `onnxruntime` |        `None`         |   `None`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |      `False`       |  \|  |       83.23       |  \|  |      12.07      |
| `onnxruntime` |  `['Add', 'MatMul']`  |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |       64.31       |  \|  |      15.60      |
| `onnxruntime` |  `['Add', 'MatMul']`  |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |       64.78       |  \|  |      15.47      |
| `onnxruntime` |       `['Add']`       |   `False`   | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |       82.63       |  \|  |      12.13      |
| `onnxruntime` |       `['Add']`       |   `True`    | `{'opset': 13, 'optimization_level': 1, 'intra_op_num_threads': 4}` |       `True`       |  \|  |       83.82       |  \|  |      11.93      |
|   `pytorch`   |        `None`         |   `None`    |                                `{}`                                 |       `None`       |  \|  |       84.34       |  \|  |      11.87      |

