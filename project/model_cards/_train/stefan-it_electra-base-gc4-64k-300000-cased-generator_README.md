---
language: de
license: mit
datasets:
- german-nlp-group/german_common_crawl
widget:
- text: "Heute ist ein [MASK] Tag"
---

# GC4LM: A Colossal (Biased) language model for German
This repository presents a colossal (and biased) language model for German trained on the recently released
["German colossal, clean Common Crawl corpus"](https://german-nlp-group.github.io/projects/gc4-corpus.html) (GC4),
with a total dataset size of ~844GB.

---

**Disclaimer**: the presented and trained language models in this repository are for **research only** purposes.
The GC4 corpus - that was used for training - contains crawled texts from the internet. Thus, the language models can
be considered as highly biased, resulting in a model that encodes stereotypical associations along gender, race,
ethnicity and disability status. Before using and working with the released checkpoints, it is highly recommended
to read:

[On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://faculty.washington.edu/ebender/papers/Stochastic_Parrots.pdf)

from Emily M. Bender, Timnit Gebru, Angelina McMillan-Major and Shmargaret Shmitchell.

The aim of the released checkpoints is to boost research on large pre-trained language models for German, especially
for identifying biases and how to prevent them, as most research is currently done only for English.

---

Please use the new GitHub Discussions feature in order to discuss or present further research questions.
Feel free to use `#gc4lm` on Twitter 🐦.

