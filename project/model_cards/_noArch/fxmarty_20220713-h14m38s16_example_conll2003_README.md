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
* **quantization_approach**: `static`
* **operators_to_quantize**: `['Add', 'MatMul']`
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
* **node_exclusion**: `[]`,  `['layernorm', 'gelu', 'residual', 'gather', 'softmax']`

# Evaluation
## Non-time metrics
|                      node_exclusion                      |     | precision (original) | precision (optimized) |     | recall (original) | recall (optimized) |     | f1 (original) | f1 (optimized) |     | accuracy (original) | accuracy (optimized) |
| :------------------------------------------------------: | :-: | :------------------: | :-------------------: | :-: | :---------------: | :----------------: | :-: | :-----------: | :------------: | :-: | :-----------------: | :------------------: |
| `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |        0.936         |         0.904         |  \|  |       0.944       |       0.921        |  \|  |     0.940     |     0.912      |  \|  |        0.988        |        0.984         |
|                           `[]`                           |  \|  |        0.936         |         0.065         |  \|  |       0.944       |       0.243        |  \|  |     0.940     |     0.103      |  \|  |        0.988        |        0.357         |

## Time metrics
Time benchmarks were run for 15 seconds per config.


Below, time metrics for batch size = 4, input length = 64.

|                      node_exclusion                      |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |
| :------------------------------------------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: |
| `['layernorm', 'gelu', 'residual', 'gather', 'softmax']` |  \|  |           114.51            |            53.59             |  \|  |           8.73            |           18.67            |
|                           `[]`                           |  \|  |            90.67            |            59.55             |  \|  |           11.07           |           16.87            |

