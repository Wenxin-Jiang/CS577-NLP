---
language: ja
tags:
- ja
- japanese
- gpt_neox
- gpt
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

# gpt-neox-japanese-2.7b

**The [open PR](https://github.com/huggingface/transformers/pull/18814) is merged on 2022/9/14.**
You can use this model with v4.23 and higher versions of transformers as follows,
```
pip install transformers
```

This repository provides a 2.7B-parameter Japanese [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)-based model. The model was trained by [ABEJA, Inc](https://www.abejainc.com/)

# How to use

When using pipeline for text generation.

``` python
from transformers import pipeline


generator = pipeline("text-generation", model="abeja/gpt-neox-japanese-2.7b")
generated = generator(
    "人とAIが協調するためには、",
    max_length=300,
    do_sample=True,
    num_return_sequences=3,
    top_p=0.95,
    top_k=50
)
print(*generated, sep="\n")

"""
[out]
{"generated_text": "人とAIが協調するためには、「人が持っている優れた能力とAIの得意とする分野を掛け合わせる」ことが不可欠になります。"}
{"generated_text": "人とAIが協調するためには、双方の長所を活かしていくことが不可欠だと考えています。"}
{"generated_text": "人とAIが協調するためには、人間がAIを理解する、ということが重要です。人間には「AIに対してAIが何をするべきか」ということを明確に教えないと、AIはある程度の知識はあっても何をすべきかがわかりません。だから、コンピューターが考えたり、決めたりすることはAIではなく、人間が解釈して理解できるようにしなくて"}
"""
```

When using PyTorch.

``` python
from transformers import AutoTokenizer, AutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained("abeja/gpt-neox-japanese-2.7b")
model = AutoModelForCausalLM.from_pretrained("abeja/gpt-neox-japanese-2.7b")

input_text = "人とAIが協調するためには、"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
gen_tokens = model.generate(
    input_ids,
    max_length=100,
    do_sample=True,
    num_return_sequences=3,
    top_p=0.95,
    top_k=50,
)
for gen_text in tokenizer.batch_decode(gen_tokens, skip_special_tokens=True):
    print(gen_text)

```

# Dataset
The model was trained on [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz), [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch), and [Japanese OSCAR](https://huggingface.co/datasets/oscar).

# Tokenization
The model uses a [special sub-word tokenizer](https://github.com/tanreinama/Japanese-BPEEncoder_V2). Please refer the original repository or [GPT-NeoX-Japanese](https://huggingface.co/docs/transformers/model_doc/gpt_neox_japanese) in detail.

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
