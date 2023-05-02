---
language: es
---
This is a smaller version of the google/mt5-base model with only Spanish and some English embeddings left following the procedure outlined here https://towardsdatascience.com/how-to-adapt-a-multilingual-t5-model-for-a-single-language-b9f94f3d9c90


The original model has 582M parameters, with 384M of them being input and output embeddings.
After shrinking the sentencepiece vocabulary from 250K to 30K (top 10K English and top 20K Spanish tokens) the number of model parameters reduced to 244M parameters, resulting on a model size reduced from 2.2GB to 0.9GB - 42% of the original one.

