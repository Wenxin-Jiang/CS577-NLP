---

language: 
  - hu
tags:
- text-generation
license: cc-by-nc-4.0
widget:
- text: "Elmesélek egy történetet a nyelvtechnológiáról."
---

# PULI GPT-2

For further details, see [our demo site](https://juniper.nytud.hu/demo/gpt2).

  - Hungarian GPT-2 model
  - Trained with Megatron-DeepSpeed [github](https://github.com/microsoft/Megatron-DeepSpeed)
  - Dataset: 36.3 billion words
  - Checkpoint: 500 000 steps

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
from transformers import GPT2Tokenizer, GPT2Model

tokenizer = GPT2Tokenizer.from_pretrained('NYTK/PULI-GPT-2')
model = GPT2Model.from_pretrained('NYTK/PULI-GPT-2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

```
## Usage with pipeline

```python
from transformers import pipeline

prompt = "Elmesélek egy történetet a nyelvtechnológiáról."
generator = pipeline(task="text-generation", model="NYTK/PULI-GPT-2")

print(generator(prompt)[0]["generated_text"])
```