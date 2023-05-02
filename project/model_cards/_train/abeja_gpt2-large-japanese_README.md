---
language: ja
tags:
- ja
- japanese
- gpt2
- text-generation
- lm
- nlp
license: mit
datasets:
- cc100
- wikipedia
- oscar
widget:
- text: "人とAIが協調するためには、"
---

# gpt2-large-japanese

This repository provides a large sized Japanese GPT-2 model. The model was trained by [ABEJA, Inc](https://abejainc.com/)

# How to use
First, install sentencepiece. We have confirmed behavior with the latest version August 2022. (Skip if not necessary.)

``` shell
pip install sentencepiece
```

When using pipeline for text generation.

``` python
from transformers import pipeline


generator = pipeline("text-generation", model="abeja/gpt2-large-japanese")
generated = generator(
    "人とAIが協調するためには、",
    max_length=30,
    do_sample=True,
    num_return_sequences=3,
    top_p=0.95,
    top_k=50,
    pad_token_id=3
)
print(*generated, sep="\n")

"""
[out]
{'generated_text': '人とAIが協調するためには、社会的なルールをきちんと理解して、人と共存し、協働して生きていくのが重要だという。'}
{'generated_text': '人とAIが協調するためには、それぞれが人間性を持ち、またその人間性から生まれるインタラクションを調整しなければならないことはいうまで'}
{'generated_text': '人とAIが協調するためには、AIが判断すべきことを人間が決める必要がある。人工知能の目的は、人間の知性、記憶、理解、'}
"""
```

When using PyTorch.

``` python
from transformers import AutoTokenizer, AutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained("abeja/gpt2-large-japanese")
model = AutoModelForCausalLM.from_pretrained("abeja/gpt2-large-japanese")

input_text = "人とAIが協調するためには、"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

gen_tokens = model.generate(
    input_ids,
    max_length=100,
    do_sample=True,
    num_return_sequences=3,
    top_p=0.95,
    top_k=50,
    pad_token_id=tokenizer.pad_token_id
)
for gen_text in tokenizer.batch_decode(gen_tokens, skip_special_tokens=True):
    print(gen_text)
```

When using TensorFlow.

```python
from transformers import AutoTokenizer, TFAutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained("abeja/gpt2-large-japanese")
model = TFAutoModelForCausalLM.from_pretrained("abeja/gpt2-large-japanese", from_pt=True)

input_text = "人とAIが協調するためには、"
input_ids = tokenizer.encode(input_text, return_tensors="tf")

gen_tokens = model.generate(
    input_ids,
    max_length=100,
    do_sample=True,
    num_return_sequences=3,
    top_p=0.95,
    top_k=50,
    pad_token_id=tokenizer.pad_token_id
)
for gen_text in tokenizer.batch_decode(gen_tokens, skip_special_tokens=True):
    print(gen_text)
```

# Dataset
The model was trained on [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz), [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch), and [Japanese OSCAR](https://huggingface.co/datasets/oscar).

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer, the vocabulary was trained on the Japanese Wikipedia.

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
