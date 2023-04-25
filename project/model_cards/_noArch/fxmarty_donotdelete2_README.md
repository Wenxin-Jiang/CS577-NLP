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

Fixed parameters:
* **model_name_or_path**: `distilbert-base-uncased-distilled-squad`
* **dataset**:
    * **path**: `squad`
    * **name**: `None`
    * **calibration_split**: `train`
    * **eval_split**: `validation`
    * **data_keys**: `{'question': 'question', 'context': 'context'}`
    * **ref_keys**: `['answers']`
    * **max_seq_length**: `128`
* **node_exclusion**: `[]`
* **per_channel**: `False`
* **calibration**:
    * **method**: `minmax`
    * **num_calibration_samples**: `20`
    * **calibration_histogram_percentile**: `None`
    * **calibration_moving_average**: `None`
    * **calibration_moving_average_constant**: `None`
* **framework**: `onnxruntime`
* **framework_args**:
    * **opset**: `15`
    * **optimization_level**: `1`
* **aware_training**: `False`

Benchmarked parameters:
* **quantization_approach**: `dynamic`,  `static`
* **operators_to_quantize**: `['Add', 'MatMul']`,  `['Add']`

## Evaluation
Below, time metrics for
* Batch size: 8
* Input length: 128
| quantization_approach | operators_to_quantize |     | latency_mean (original, ms) | latency_mean (optimized, ms) |     | throughput (original, /s) | throughput (optimized, /s) |     | exact_match (original) | exact_match (optimized) |     | f1 (original) | f1 (optimized) |
| :-------------------: | :-------------------: | :-: | :-------------------------: | :--------------------------: | :-: | :-----------------------: | :------------------------: | :-: | :--------------------: | :---------------------: | :-: | :-----------: | :------------: |
|       `dynamic`       |  `['Add', 'MatMul']`  |  \|  |           247.65            |            75.80             |  \|  |           4.50            |           13.50            |  \|  |         90.000         |         85.000          |  \|  |    90.000     |     86.667     |
|       `dynamic`       |       `['Add']`       |  \|  |           234.61            |            191.78            |  \|  |           4.50            |            5.50            |  \|  |         90.000         |         90.000          |  \|  |    90.000     |     90.000     |
|       `static`        |  `['Add', 'MatMul']`  |  \|  |           238.04            |            131.81            |  \|  |           4.50            |            8.00            |  \|  |         90.000         |         50.000          |  \|  |    90.000     |     59.362     |
|       `static`        |       `['Add']`       |  \|  |           241.84            |            257.85            |  \|  |           4.50            |            4.00            |  \|  |         90.000         |         70.000          |  \|  |    90.000     |     76.333     |
