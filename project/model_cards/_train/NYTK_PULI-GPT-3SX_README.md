---

language: 
  - hu
tags:
- text-generation
license: cc-by-nc-4.0
widget:
- text: "Elmesélek egy történetet a nyelvtechnológiáról."

---

# PULI GPT-3SX (6.7 billion parameter)

For further details, see [our demo site](https://juniper.nytud.hu/demo/puli).

  - Hungarian GPT-NeoX model (6.7 billion parameter)
  - Trained with EleutherAI's GPT-NeoX [github](https://github.com/EleutherAI/gpt-neox)
  - Dataset: 36.3 billion words
  - Checkpoint: 150 000 steps

## Limitations

- max_seq_length = 2048


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
from transformers import GPTNeoXForCausalLM, GPTNeoXTokenizerFast

model = GPTNeoXForCausalLM.from_pretrained("NYTK/PULI-GPT-3SX")
tokenizer = GPTNeoXTokenizerFast.from_pretrained("NYTK/PULI-GPT-3SX")
prompt = "Elmesélek egy történetet a nyelvtechnológiáról."
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)

gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)
```
## Usage with pipeline

```python
from transformers import pipeline, GPTNeoXForCausalLM, GPTNeoXTokenizerFast

model = GPTNeoXForCausalLM.from_pretrained("NYTK/PULI-GPT-3SX")
tokenizer = GPTNeoXTokenizerFast.from_pretrained("NYTK/PULI-GPT-3SX")
prompt = "Elmesélek egy történetet a nyelvtechnológiáról."
generator = pipeline(task="text-generation", model=model, tokenizer=tokenizer)

print(generator(prompt)[0]["generated_text"])
```