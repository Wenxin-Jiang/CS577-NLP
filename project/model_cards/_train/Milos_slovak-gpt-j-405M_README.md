---
language:
- sk
tags:
- Slovak GPT-J
- pytorch
- causal-lm
license: gpl-3.0
---

# Slovak GPT-J-405M
Slovak GPT-J-405M is the second model released in Slovak GPT-J series after its smaller variant [Slovak GPT-J-162M](https://huggingface.co/Milos/slovak-gpt-j-162M). Since then a larger [Slovak GPT-J-1.4B](https://huggingface.co/Milos/slovak-gpt-j-1.4B) was released.
## Model Description
Model is based on [GPT-J](https://github.com/kingoflolz/mesh-transformer-jax/) and has over 405M trainable parameters.

<figure>

| Hyperparameter       | Value                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| \\(n_{parameters}\\) | 405,677,136                                                                                                                            |
| \\(n_{layers}\\)     | 24                                                                                                                                     |
| \\(d_{model}\\)      | 1024                                                                                                                                   |
| \\(d_{ff}\\)         | 16384                                                                                                                                  |
| \\(n_{heads}\\)      | 16                                                                                                                                     |
| \\(d_{head}\\)       | 256                                                                                                                                    |
| \\(n_{ctx}\\)        | 2048                                                                                                                                   |
| \\(n_{vocab}\\)      | 50256 (same tokenizer as GPT-2/3&dagger;)                                                                                              |
| Positional Encoding  | [Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864)                                                                   |
| RoPE Dimensions      | [64](https://github.com/kingoflolz/mesh-transformer-jax/blob/f2aa66e0925de6593dcbb70e72399b97b4130482/mesh_transformer/layers.py#L223) |

<p><strong>&dagger;</strong> ByteLevelBPETokenizer was trained on the same Slovak corpus.</p></figure>

## Training data

Slovak GPT-J models were trained on a privately collected dataset consisting of predominantly Slovak text spanning different categories, e.g. web, news articles or even biblical texts - in total, over 40GB of text data was used to train this model.
The dataset was preprocessed and cleaned in a specific way that involves minor but a few caveats, so in order to achieve the expected performance, feel free to refer to [How to use] section. Please, keep in mind that despite the effort to remove inappropriate corpus, the model still might generate sensitive content or leak sensitive information.

## Training procedure

This model was trained for a bit more than 36.5 billion tokens over 69,001 steps on TPU v3-8 pod. The cross-entropy validation loss at the last step was `2.821`.

## Intended Use

Same as the original GPT-J, Slovak GPT-J learns an inner representation of the language that can be used to extract features useful for downstream tasks, however, the intended use is text generation from a prompt.

### How to use

This model along with the tokenizer can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Milos/slovak-gpt-j-405M")
model = AutoModelForCausalLM.from_pretrained("Milos/slovak-gpt-j-405M")
```

When generating a prompt keep in mind these three things, and you should be good to go:
1. Never leave trailing whitespaces. There's a difference between how tokenizer encodes "Mám rád slovenčinu" (no space after `slovenčinu`) and "Mám rád slovenčinu " (trailing space after `slovenčinu`), i.e `[12805, 2872, 46878]` != `[12805, 2872, 46878, 221]`.
2. Always use good ol' US English primary double quotation marks, i.e. `""` instead of `„“`.
3. In case of a new line always enter `\n\n` instead of a single `\n`

To illustrate an example of a basic text generation:
```
>>> prompt = "Tradičné jedlo na Orave sú"
>>> encoded_input = tokenizer(prompt, return_tensors='pt')
>>> output = model.generate(**encoded_input)
>>> tokenizer.decode(output[0])
'Tradičné jedlo na Orave sú bryndzové halušky\n\nNa Orave sa v minulosti varilo viac druhov'
```

### Capabilities, Limitations, and Biases

The capability of this particular model is somewhat decent despite its small size totalling 405M parameters. With relative ease it can manage to generate interesting and grammatically correct content.
For example, you can try few of the following prompts. (For sake of simplicity, I have omitted all the boilerplate code and swapped `\n` for new lines).

Try generating "How to" articles:
```
PROMPT
Ako napísať pôsobivú esej krok za krokom
OUTPUT
Ako napísať pôsobivú esej krok za krokom

V tomto článku sa dozviete, ako napísať esej, ktorá bude mať v sebe niečo, čo zaujme a bude sa vám páčiť.

V prvom rade si musíte uvedomiť, že esej je vlastne písaný text, ktorý má byť napísaný na počítači.'
```
However, relying on the model to produce factually correct information isn't recommended.

Or try to generate chat conversations:
```
PROMPT
Peter: Ako sa mas?

Lucia: Ale celkom dobre. Co si robil?

Peter:
OUTPUT
Peter: Ako sa mas?

Lucia: Ale celkom dobre. Co si robil?

Peter: No, bol som na chate.

Lucia: A co si tam robil?

Peter: No, bol som tam s kamošmi.

Lucia: A co si tam robil?

Peter: No, bol som tam s kamošmi.
```
Apparently either Peters are more likely to act suspiciously in this particular context or there's a problem with the model. Let's assume that the second explanation may hold some merit. In general, GPT models can (and often will) get into a repeating cycle of generating same content. This is a common problem beyond the scope of this README, however, see [generate's documentation](https://huggingface.co/docs/transformers/master/en/main_classes/model#transformers.generation_utils.GenerationMixin.generate) on how to introduce a frequency/repetition penalty. 

Since the dataset contains profanity, politically incorrect language, and (unintentionally) even a bits of text in Czech, the model can generate them in some extent too. Here's an example of the model output when prompt is in Czech:
```
>>> prompt = "Věta nesmí být sprostá a musí být zcela"
>>> encoded_input = tokenizer(prompt, return_tensors='pt')
>>> output = model.generate(**encoded_input, max_length=16)
>>> tokenizer.decode(output[0])
'Věta nesmí být sprostá a musí být zcela pravdivá.'
```

## Citation and Related Information

This was done as a moonlighting project during summer of 2021 to better understand transformers. I didn't have much free time to open source it properly, so it all sat on my hard drive until now :)

If you use this model or have any questions about it feel free to hit me up at [twitter](https://twitter.com/miloskondela) or check out my [github](https://github.com/kondela) profile.

### BibTeX entry
To cite this model:
```bibtex
@misc{slovak-gpt-j-405m,
  author = {Kondela, Milos},
  title = {{Slovak GPT-J-405M}},
  howpublished = {\url{https://huggingface.co/Milos/slovak-gpt-j-405M}},
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