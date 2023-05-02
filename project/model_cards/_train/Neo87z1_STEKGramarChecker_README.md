---
language: en
tags:
- grammar
- text2text-generation
license: cc-by-nc-sa-4.0
datasets:
- jfleg
---

# T5 Grammar Correction 

This model generates a revised version of inputted text with the goal of containing fewer grammatical errors. 
It was trained with [Happy Transformer](https://github.com/EricFillion/happy-transformer)
using a dataset called [JFLEG](https://arxiv.org/abs/1702.04066). Here's a [full article](https://www.vennify.ai/fine-tune-grammar-correction/) on how to train a similar model. 


## Usage 

`pip install happytransformer `

```python
from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)

# Add the prefix "grammar: " before each input 
result = happy_tt.generate_text("grammar: This sentences has has bads grammar.", args=args)

print(result.text) # This sentence has bad grammar.


```