---
pipeline_tag: text-classification
datasets:
- glue
metrics:
- accuracy
tags:
- roberta
---

**task**: `text-classification`

Fixed parameters:
* **model_name_or_path**: `Bhumika/roberta-base-finetuned-sst2`
* **dataset**:
    * **path**: `glue`
    * **eval_split**: `validation`
    * **data_keys**: `{'primary': 'sentence'}`
    * **ref_keys**: `['label']`
    * **name**: `sst2`
* **quantization_approach**: `dynamic`
* **node_exclusion**: `[]`
* **per_channel**: `False`
* **framework**: `onnxruntime`
* **framework_args**:
    * **opset**: `15`
    * **optimization_level**: `1`
* **aware_training**: `False`

Benchmarked parameters:
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`

## Evaluation
Below, time metrics for
* Batch size: 8
* Input length: 128
| operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |     | accuracy (original) | accuracy (optimized) |
| :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: | :-: | :-----------------: | :------------------: |
|  `['Add', 'MatMul']`  |  \|  |           619.76            |            161.66            |  \|  |           1.80            |            6.20            |  \|  |        1.000        |        1.000         |
|       `['Add']`       |  \|  |           611.74            |            478.48            |  \|  |           1.80            |            2.20            |  \|  |        1.000        |        1.000         |
