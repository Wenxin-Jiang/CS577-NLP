---
language: es
tags:
- GPT-2
- Spanish
- review
- fake
datasets:
 - amazon_reviews_multi
widget:
- text: "Me ha gustado su"
  example_title: "Positive review"
- text: "No quiero"
  example_title: "Negative review"
license: mit
---

# GPT-2 - reviewspanish

## Model description


GPT-2 is a transformers model pretrained on a very large corpus of text data in a self-supervised fashion. This
means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots
of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely,
it was trained to guess the next word in sentences.

In our case, we created a fined-tunned model of [Spanish GTP-2](https://huggingface.co/DeepESP/gpt2-spanish) combined with
the spanish reviews of Amazon from the HG dataset [Amazon-reviews-multi](https://huggingface.co/datasets/amazon_reviews_multi).

With this strategy, we obtain a model for text generation able to create realistic product reviews, useful for bot detection in
fake reviews. 

### How to use

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we
set a seed for reproducibility:

```python
from transformers import pipeline, set_seed
generator = pipeline('text-generation', 
                    model='Amloii/gpt2-reviewspanish', 
                    tokenizer='Amloii/gpt2-reviewspanish')
set_seed(42)
generator("Me ha gustado su", max_length=30, num_return_sequences=5)

[{'generated_text': 'Me ha gustado su tamaño y la flexibilidad de las correas, al ser de plastico las hebillas que lleva para sujetar las cadenas me han quitado el'},
 {'generated_text': 'Me ha gustado su color y calidad. Lo peor de todo, es que las gafas no se pegan nada. La parte de fuera es finita'},
 {'generated_text': 'Me ha gustado su rapidez y los ajustes de la correa, lo único que para mí, es poco manejable. Además en el bolso tiene una goma'},
 {'generated_text': 'Me ha gustado su diseño y las dimensiones, pero el material es demasiado duro. Se nota bastante el uso pero me parece un poco caro para lo que'},
 {'generated_text': 'Me ha gustado su aspecto aunque para lo que yo lo quería no me ha impresionado mucho.  Las hojas tienen un tacto muy agradable que hace que puedas'}]

```
