---
language:
  - uk
tags:
  - text2text-generation
  - punctuation prediction
  - punctuation
library_name: generic
license: mit
metrics:
  - f1
datasets:
- ubertext2.0
widget:
- text: "доброго вечора ми з україни"
---

# Ukrainian model to restore punctuation and capitalization

This is the NeMo model to restore punctuation and capitalization in sentences, trained on 10m+ sentences from UberText 2.0 corpus (yet unreleased). Basic transformer under the hood is `bert-base-multilingual-cased`.

Model restores the following punctuations -- [? . ,].

It also restores capitalization of words.

Copyright: [Dmytro Chaplynskyi](https://twitter.com/dchaplinsky), [lang-uk](https://lang.org.ua) project, 2022