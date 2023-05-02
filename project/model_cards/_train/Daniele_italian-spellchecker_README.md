---
language:
- it
tags:
- seq2seq
license: mit
---
# Italian Contextual Spellchecker

The model is a fine-tuned version of [IT5](https://huggingface.co/models?search=it5)[1], specifically modelled for computing a spellchecking in the shape of a sequence-to-sequence task.

### USAGE

The input sequence should have the structure <b>seq: <i>your text</i>.</b>. Missing the seq token at the beginning or the final punctuation mark may lead to bad performances.