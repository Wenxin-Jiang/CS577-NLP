---
language: ["fa", "en"]
tags:
- farsi/persian
---
This is a smaller version of the [google/mt5-base](https://huggingface.co/google/mt5-base) model with only Farsi and some English embeddings left. 

* The original model has 582M parameters, with 384M of them being input and output embeddings. 
* After shrinking the `sentencepiece` vocabulary from 250K to 30K (top 10K English and top 20K Russian tokens) the number of model parameters was reduced to 244M parameters, and the model size was reduced from 2.2GB to 0.9GB - 42% of the original one.

The creation of this model is described in the post [How to adapt a multilingual T5 model for a single language](https://cointegrated.medium.com/how-to-adapt-a-multilingual-t5-model-for-a-single-language-b9f94f3d9c90) along with the source code.
