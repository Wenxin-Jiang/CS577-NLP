---
language:
- sk
tags:
- Slovak GPT-J
- pytorch
- causal-lm
license: gpl-3.0
---

# Slovak GPT-J-162M
Slovak GPT-J-162M is the first model released in Slovak GPT-J series and the very first publicly available transformer trained predominantly on Slovak corpus. Since the initial release two other models were made public, [Slovak GPT-J-405M](https://huggingface.co/Milos/slovak-gpt-j-405M) and the largest [Slovak GPT-J-1.4B](https://huggingface.co/Milos/slovak-gpt-j-1.4B).

## Model Description
Model is based on [GPT-J](https://github.com/kingoflolz/mesh-transformer-jax/) and has over 162M trainable parameters.

<figure>

| Hyperparameter       | Value                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------|
| \\(n_{parameters}\\) | 162,454,608                                                                                                                   |
| \\(n_{layers}\\)     | 12                                                                                                                            |
| \\(d_{model}\\)      | 768                                                                                                                           |
| \\(d_{ff}\\)         | 16384                                                                                                                         |
| \\(n_{heads}\\)      | 16                                                                                                                            |
| \\(d_{head}\\)       | 256                                                                                                                           |
| \\(n_{ctx}\\)        | 2048                                                                                                                          |
| \\(n_{vocab}\\)      | 50256 (same tokenizer as GPT-2/3&dagger;)                                                                                     |
| Positional Encoding  | [Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864)                                                          |
| RoPE Dimensions      | [64](https://github.com/kingoflolz/mesh-transformer-jax/blob/f2aa66e0925de6593dcbb70e72399b97b4130482/mesh_transformer/layers.py#L223) |

<p><strong>&dagger;</strong> ByteLevelBPETokenizer was trained on the same Slovak corpus.</p></figure>

## Training data

Slovak GPT-J-162M was trained on a privately collected dataset consisting of predominantly Slovak text spanning different categories, e.g. web, news articles or even biblical texts - in total, over 40GB of text data was used to train this model.
The dataset was preprocessed and cleaned in a specific way that involves minor but a few caveats, so in order to achieve the expected performance, feel free to refer to [How to use] section. Please, keep in mind that despite the effort to remove inappropriate parts of the corpus, the model still might generate sensitive content or leak sensitive information.

## Training procedure

This model was trained for almost 37 billion tokens over 69,001 steps on TPU v3-8 pod. The cross-entropy validation loss at the last step was 3.065.

## Intended Use

Same as the original GPT-J, Slovak GPT-J learns an inner representation of the language that can be used to extract features useful for downstream tasks, however, the intended use is text generation from a prompt.

### How to use

This model along with the tokenizer can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Milos/slovak-gpt-j-162M")
model = AutoModelForCausalLM.from_pretrained("Milos/slovak-gpt-j-162M")
```

When generating a prompt keep in mind these three things, and you should be good to go:
1. Never leave trailing whitespaces. There's a difference between how tokenizer encodes "Mám rád slovenčinu" (no space after `slovenčinu`) and "Mám rád slovenčinu " (trailing space after `slovenčinu`), i.e `[12805, 2872, 46878]` != `[12805, 2872, 46878, 221]`.
2. Always use good ol' US English primary double quotation marks, i.e. `""` instead of `„“`.
3. In case of a new line always enter `\n\n` instead of a single `\n`

To illustrate an example of a basic text generation:
```
>>> prompt = "Moje najobľubenejšie mesto na severe Slovenska je"
>>> encoded_input = tokenizer(prompt, return_tensors='pt')
>>> output = model.generate(**encoded_input)
>>> tokenizer.decode(output[0])
'Moje najobľubenejšie mesto na severe Slovenska je Žilina.\n\nV Žiline sa nachádza množstvo zaujímavých miest'
```

### Capabilities, Limitations, and Biases

First and foremost, the capability of this particular model is very limited due to its relatively small size totalling only 162M parameters, hence the intended use of this particular model is to educate and have fun! :)

Since the dataset contains profanity, politically incorrect language, and (unintentionally) even a bits of text in Czech, the model can generate them in some extent too. Here's an example of the model output when prompt is in Czech:
```
>>> prompt = "Věta nesmí být sprostá a musí být zcela"
>>> encoded_input = tokenizer(prompt, return_tensors='pt')
>>> output = model.generate(**encoded_input, max_length=16)
>>> tokenizer.decode(output[0])
'Věta nesmí být sprostá a musí být zcela věrná.'
```

## Citation and Related Information

This was done as a moonlighting project during summer of 2021 to better understand transformers. I didn't have much free time to open source it properly, so it all sat on my hard drive until now. Based on the popularity and interest in this model I might release _substantially_ larger versions of Slovak GPT-J models that are way more capable.

If you use this model or have any questions about it feel free to hit me up at [twitter](https://twitter.com/miloskondela) or check out my [github](https://github.com/kondela) profile.

### BibTeX entry
To cite this model:
```bibtex
@misc{slovak-gpt-j-162m,
  author = {Kondela, Milos},
  title = {{Slovak GPT-J-162M}},
  howpublished = {\url{https://huggingface.co/Milos/slovak-gpt-j-162M}},
  year = 2022,
  month = February
}
```

To cite the codebase that trained this model:
```bibtex
@misc{mesh-transformer-jax,
  author = {Wang, Ben},
  title = {{Mesh-Transformer-JAX: Model-Parallel Implementation of Transformer Language Model with JAX}},
  howpublished = {\url{https://github.com/kingoflolz/mesh-transformer-jax}},
  year = 2021,
  month = May
}
```

## Acknowledgements
This project was generously supported by [TPU Research Cloud (TRC) program](https://sites.research.google/trc/about/). Shoutout also goes to [Ben Wang](https://github.com/kingoflolz) and great [EleutherAI community](https://www.eleuther.ai/).