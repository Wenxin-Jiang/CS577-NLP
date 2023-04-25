---
inference: false
tags:
- onnx
- text-classification
- adapterhub:rc/multirc
- roberta
- adapter-transformers
language:
- en
---

# ONNX export of Adapter `AdapterHub/roberta-base-pf-multirc` for roberta-base
## Conversion of [AdapterHub/roberta-base-pf-multirc](https://huggingface.co/AdapterHub/roberta-base-pf-multirc) for UKP SQuARE


## Usage
```python
onnx_path = hf_hub_download(repo_id='UKP-SQuARE/roberta-base-pf-multirc-onnx', filename='model.onnx') # or model_quant.onnx for quantization
onnx_model = InferenceSession(onnx_path, providers=['CPUExecutionProvider'])

context = 'ONNX is an open format to represent models. The benefits of using ONNX include interoperability of frameworks and hardware optimization.'
question = 'What are advantages of ONNX?'
choices = ["Cat", "Horse", "Tiger", "Fish"]tokenizer = AutoTokenizer.from_pretrained('UKP-SQuARE/roberta-base-pf-multirc-onnx')

raw_input = [[context, question +  + choice] for choice in choices]
inputs = tokenizer(raw_input, padding=True, truncation=True, return_tensors="np")
inputs['token_type_ids'] = np.expand_dims(inputs['token_type_ids'], axis=0)
inputs['input_ids'] =  np.expand_dims(inputs['input_ids'], axis=0)
inputs['attention_mask'] =  np.expand_dims(inputs['attention_mask'], axis=0)
outputs = onnx_model.run(input_feed=dict(inputs), output_names=None)
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