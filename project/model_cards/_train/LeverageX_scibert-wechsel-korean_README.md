# scibert-wechsel-korean

Scibert(🇺🇸) converted into Korean(🇰🇷) using WECHSEL technique.

### Description
- SciBERT is trained on papers from the corpus of semanticscholar.org. Corpus size is 1.14M papers, 3.1B tokens. 
- Wechsel is converting embedding layer's subword tokens from source language to target language. 
- SciBERT trained with English language is converted into Korean langauge using Wechsel technique.
- Korean tokenizer is selected with KLUE PLMs' tokenizers due to its similar vocab size(32000) and performance.

### Reference
- [Scibert](https://github.com/allenai/scibert)
- [WECHSEL](https://github.com/CPJKU/wechsel)
- [Korean Language Understanding Evaluation](https://github.com/KLUE-benchmark/KLUE)