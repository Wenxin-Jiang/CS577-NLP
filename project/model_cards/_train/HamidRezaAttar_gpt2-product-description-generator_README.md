---
language: en
tags:
- text-generation
license: apache-2.0
widget:
- text: "Maximize your bedroom space without sacrificing style with the storage bed."
- text: "Handcrafted of solid acacia in weathered gray, our round Jozy drop-leaf dining table is a space-saving."
- text: "Our plush and luxurious Emmett modular sofa brings custom comfort to your living space."
---

## GPT2-Home

This model is fine-tuned using GPT-2 on amazon home products metadata. 
It can generate descriptions for your **home** products by getting a text prompt.

### Model description


[GPT-2](https://openai.com/blog/better-language-models/) is a large [transformer](https://arxiv.org/abs/1706.03762)-based language model with 1.5 billion parameters, trained on a dataset of 8 million web pages. GPT-2 is trained with a simple objective: predict the next word, given all of the previous words within some text. The diversity of the dataset causes this simple goal to contain naturally occurring demonstrations of many tasks across diverse domains. GPT-2 is a direct scale-up of GPT, with more than 10X the parameters and trained on more than 10X the amount of data.

### Live Demo
For testing model with special configuration, please visit [Demo](https://huggingface.co/spaces/HamidRezaAttar/gpt2-home)

### Blog Post
For more detailed information about project development please refer to my [blog post](https://hamidrezaattar.github.io/blog/markdown/2022/02/17/gpt2-home.html).

### How to use
For best experience and clean outputs, you can use Live Demo mentioned above, also you can use the notebook mentioned in my [GitHub](https://github.com/HamidRezaAttar/GPT2-Home)

You can use this model directly with a pipeline for text generation.
```python
>>> from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
>>> tokenizer = AutoTokenizer.from_pretrained("HamidRezaAttar/gpt2-product-description-generator")
>>> model = AutoModelForCausalLM.from_pretrained("HamidRezaAttar/gpt2-product-description-generator")
>>> generator = pipeline('text-generation', model, tokenizer=tokenizer, config={'max_length':100})
>>> generated_text = generator("This bed is very comfortable.")
```

### Citation info
```bibtex
@misc{GPT2-Home,
  author = {HamidReza Fatollah Zadeh Attar},
  title = {GPT2-Home the English home product description generator},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/HamidRezaAttar/GPT2-Home}},
}
```
