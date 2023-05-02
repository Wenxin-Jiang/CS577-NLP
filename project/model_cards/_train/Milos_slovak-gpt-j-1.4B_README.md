---
language:
- sk
tags:
- Slovak GPT-J
- pytorch
- causal-lm
license: gpl-3.0
---

# Slovak GPT-J-1.4B
Slovak GPT-J-1.4B with the whopping `1,415,283,792` parameters is the latest and the largest model released in Slovak GPT-J series. Smaller variants, [Slovak GPT-J-405M](https://huggingface.co/Milos/slovak-gpt-j-405M) and [Slovak GPT-J-162M](https://huggingface.co/Milos/slovak-gpt-j-162M), are still available.
## Model Description
Model is based on [GPT-J](https://github.com/kingoflolz/mesh-transformer-jax/) and has over 1.4B trainable parameters.

<figure>

| Hyperparameter       | Value                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| \\(n_{parameters}\\) | 1,415,283,792                                                                                                                          |
| \\(n_{layers}\\)     | 24                                                                                                                                     |
| \\(d_{model}\\)      | 2048                                                                                                                                   |
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

This model was trained for a bit more than 26.5 billion tokens over 48,001 steps on TPU v3-8 pod. The cross-entropy validation loss at the last step was `2.657`.

## Intended Use

Same as the original GPT-J, Slovak GPT-J learns an inner representation of the language that can be used to extract features useful for downstream tasks, however, the intended use is text generation from a prompt.

### How to use

This model along with the tokenizer can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Milos/slovak-gpt-j-1.4B")
model = AutoModelForCausalLM.from_pretrained("Milos/slovak-gpt-j-1.4B")
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

Based on the parameter count and our internal testing this should be by far the most capable model out of all models released in Slovak GPT-J series.
For sake of simplicity, I have omitted all the boilerplate code and swapped `\n` for new lines in the examples that follow. These were generated with both `top_p` and `temperature` set to `0.9`. 

A spin on "Mor ho!" by Samo Chalpuka 
```
PROMPT
Zleteli orly z Tatry, tiahnu na podolia, ponad vysoké hory, ponad rovné polia; preleteli cez Dunaj, cez tú šíru vodu, sadli tam za pomedzím slovenského rodu.

Duní Dunaj a luna za lunou sa valí
OUTPUT
Zleteli orly z Tatry, tiahnu na podolia, ponad vysoké hory, ponad rovné polia; preleteli cez Dunaj, cez tú šíru vodu, sadli tam za pomedzím slovenského rodu.

Duní Dunaj a luna za lunou sa valí: nad ním svieti pevný hrad na vysokom bralí. Pod tým hradom je zem slovenská, na nej je Slovensko naše.

Na tom vrchu leží slovenský národ, pod tým bralom leží krajina slovenská. A pod tým hradom leží i jeho sláva: na tom vrchu, na tom brale leží sláva slovenského národa.```
```

Jokes are a bit hit or miss. Very often they contain vulgarisms and/or are highly politically incorrect. This one is rather exception than the rule.
```
PROMPT
Nasledujú najlepšie vtipy.

Prečo
OUTPUT
Nasledujú najlepšie vtipy.

Prečo má policajt pri sebe vždy dva nože? Jeden je na sebaobranu, druhý na boj zblízka.
```

The infamous unicorn prompt from GPT-2 paper.
```
PROMPT
V šokujúcom náleze vedci objavili stádo jednorožcov žijúcich v odľahlom, predtým nepreskúmanom údolí, v Andách. Ešte prekvapivejšie pre vedcov bol fakt, že jednorožce hovorili plynule po slovensky.

OUTPUT
V šokujúcom náleze vedci objavili stádo jednorožcov žijúcich v odľahlom, predtým nepreskúmanom údolí, v Andách. Ešte prekvapivejšie pre vedcov bol fakt, že jednorožce hovorili plynule po slovensky.

V Andách ich totiž žilo približne 700 jedincov, ktoré sa živili výhradne materským mliekom. Slováci sú tak pravdepodobne prvými Európanmi, ktorí v Andách stretli jednorožca. "Je to dôkaz, že tieto zvieratá sú inteligentné a že žijú v Andách už stovky rokov," povedal pre webový portál televízie JOJ profesor geológie, geografie a zoológie, Milan Kováč.

Podľa profesora Kováča si v Andách zvieratá vytvárajú svoj vlastný jazyk. Je to zároveň dôkaz, že jednorožce žili v minulosti aj v slovenských pohoriach. "Jednorožce sa tam síce vyskytovali, ale neboli tak dobre preskúmané, ako teraz v Andách."

Na Slovensku však ľudia o jednorožcoch donedávna vedeli veľmi málo.<|endoftext|>
```

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
@misc{slovak-gpt-j-1.4B,
  author = {Kondela, Milos},
  title = {{Slovak GPT-J-1.4B}},
  howpublished = {\url{https://huggingface.co/Milos/slovak-gpt-j-1.4B}},
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