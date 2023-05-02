---

language: 
  - hu
tags:
- fill-mask
license: cc-by-nc-4.0
widget:
- text: "Mesélek egy [MASK] az oroszlánról."
---

# PULI BERT-Large

For further details, see [our demo site](https://juniper.nytud.hu/demo/nlp).

  - Hungarian BERT large model (MegatronBERT)
  - Trained with Megatron-DeepSpeed [github](https://github.com/microsoft/Megatron-DeepSpeed)
  - Dataset: 36.3 billion words
  - Checkpoint: 1 500 000 steps

## Limitations

- max_seq_length = 1024


## Citation
If you use this model, please cite the following paper:

```
@inproceedings {yang-puli,
    title = {Jönnek a nagyok! BERT-Large, GPT-2 és GPT-3 nyelvmodellek magyar nyelvre},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Hungary},
	author = {Yang, Zijian Győző and Dodé, Réka and Ferenczi, Gergő and Héja, Enikő and Jelencsik-Mátyus, Kinga and Kőrös, Ádám and Laki, László János and Ligeti-Nagy, Noémi and Vadász, Noémi and Váradi, Tamás},
	pages = {247--262}
}
```

## Usage

```python
from transformers import BertTokenizer, MegatronBertModel

tokenizer = BertTokenizer.from_pretrained('NYTK/PULI-BERT-Large')
model = MegatronBertModel.from_pretrained('NYTK/PULI-BERT-Large')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt', do_lower_case=False)
output = model(**encoded_input)

```
