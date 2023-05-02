---
language: cs

license: cc-by-nc-sa-4.0
datasets:
- csTenTen17
---

# CzeGPT-2
CzeGPT-2 is a Czech version of GPT-2 language model by OpenAI with LM Head on top. The model has the same architectural dimensions as the GPT-2 small (12 layers, 12 heads, 1024 tokens on input/output, and embedding vectors with 768 dimensions) resulting in 124 M trainable parameters. It was trained on a 5 GB slice of cleaned csTenTen17 dataset. 

The model is a good building block for any down-stream task requiring autoregressive text generation. 

# Tokenizer
Along, we also provide a tokenizer (vocab and merges) with vocab size of 50257 that was used during the pre-training phase. It is the byte-level BPE tokenizer used in the original paper and was trained on the whole 5 GB train set.

# Training results
The model's perplexity on a 250 MB random slice of csTenTen17 dataset is **42.12**. This value is unfortunately not directly comparable to any other model, since there is no competition in Czech autoregressive models yet (and comparison with models for other languages is meaningless, because of different tokenization and test data). 

# Running the predictions
The repository includes a simple Jupyter Notebook that can help with the first steps when using the model.

## How to cite
@unpublished{hajek_horak2022,<br>
  author = "Adam Hájek and Aleš Horák",<br>
  title  = "CzeGPT-2 – New Model for Czech Summarization Task",<br>
  note   = "preprint available at \url{https://openreview.net/forum?id=H43eQtxZefq}",<br>
  month  = "3",<br>
  year   = "2022",<br>
}
