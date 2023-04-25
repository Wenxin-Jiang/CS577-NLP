---
inference: false
tags:
- onnx
- question-answering
- bert
- adapter-transformers
datasets:
- quoref
language:
- en
---

# ONNX export of Adapter `AdapterHub/bert-base-uncased-pf-quoref` for bert-base-uncased
## Conversion of [AdapterHub/bert-base-uncased-pf-quoref](https://huggingface.co/AdapterHub/bert-base-uncased-pf-quoref) for UKP SQuARE


## Usage
```python
onnx_path = hf_hub_download(repo_id='UKP-SQuARE/bert-base-uncased-pf-quoref-onnx', filename='model.onnx') # or model_quant.onnx for quantization
onnx_model = InferenceSession(onnx_path, providers=['CPUExecutionProvider'])

context = 'ONNX is an open format to represent models. The benefits of using ONNX include interoperability of frameworks and hardware optimization.'
question = 'What are advantages of ONNX?'
tokenizer = AutoTokenizer.from_pretrained('UKP-SQuARE/bert-base-uncased-pf-quoref-onnx')

inputs = tokenizer(question, context, padding=True, truncation=True, return_tensors='np')
inputs_int64 = {key: np.array(inputs[key], dtype=np.int64) for key in inputs}
outputs = onnx_model.run(input_feed=dict(inputs_int64), output_names=None)
```

## Architecture & Training

The training code for this adapter is available at https://github.com/adapter-hub/efficient-task-transfer.
In particular, training configurations for all tasks can be found [here](https://github.com/adapter-hub/efficient-task-transfer/tree/master/run_configs).


## Evaluation results

Refer to [the paper](https://arxiv.org/pdf/2104.08247) for more information on results.

## Citation

If you use this adapter, please cite our paper ["What to Pre-Train on? Efficient Intermediate Task Selection"](https://arxiv.org/pdf/2104.08247):

```bibtex
@inproceedings{poth-etal-2021-pre,
    title = "{W}hat to Pre-Train on? {E}fficient Intermediate Task Selection",
    author = {Poth, Clifton  and
      Pfeiffer, Jonas  and
      R{"u}ckl{'e}, Andreas  and
      Gurevych, Iryna},
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.827",
    pages = "10585--10605",
}
```