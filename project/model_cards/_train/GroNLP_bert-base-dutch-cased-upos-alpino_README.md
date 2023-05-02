---
language: nl
tags:
- BERTje
- pos
---

Wietse de Vries • Martijn Bartelds • Malvina Nissim • Martijn Wieling

# Adapting Monolingual Models: Data can be Scarce when Language Similarity is High

This model is part of this paper + code:

- 📝 [Paper](https://arxiv.org/abs/2105.02855)
- 💻 [Code](https://github.com/wietsedv/low-resource-adapt)

## Models

The best fine-tuned models for Gronings and West Frisian are available on the HuggingFace model hub:

### Lexical layers
These models are identical to [BERTje](https://github.com/wietsedv/bertje), but with different lexical layers (`bert.embeddings.word_embeddings`).

 - 🤗 [`GroNLP/bert-base-dutch-cased`](https://huggingface.co/GroNLP/bert-base-dutch-cased) (Dutch; source language)
 - 🤗 [`GroNLP/bert-base-dutch-cased-gronings`](https://huggingface.co/GroNLP/bert-base-dutch-cased-gronings) (Gronings)
 - 🤗 [`GroNLP/bert-base-dutch-cased-frisian`](https://huggingface.co/GroNLP/bert-base-dutch-cased-frisian) (West Frisian)

### POS tagging
These models share the same fine-tuned Transformer layers + classification head, but with the retrained lexical layers from the models above.

 - 🤗 [`GroNLP/bert-base-dutch-cased-upos-alpino`](https://huggingface.co/GroNLP/bert-base-dutch-cased-upos-alpino) (Dutch)
 - 🤗 [`GroNLP/bert-base-dutch-cased-upos-alpino-gronings`](https://huggingface.co/GroNLP/bert-base-dutch-cased-upos-alpino-gronings) (Gronings)
 - 🤗 [`GroNLP/bert-base-dutch-cased-upos-alpino-frisian`](https://huggingface.co/GroNLP/bert-base-dutch-cased-upos-alpino-frisian) (West Frisian)
