---
license: mit
datasets:
- DarwinAnim8or/grug
language:
- en
pipeline_tag: text-generation
tags:
- grug
- caveman
- fun
---

# GPT-Grug-125m
A finetuned version of [GPT-Neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M) on the 'grug' dataset.
A demo is available [here](https://huggingface.co/spaces/DarwinAnim8or/grug-chat)

NOTE: A larger, more capable version can be found [here](https://huggingface.co/DarwinAnim8or/GPT-Grug-355m)

# Training Procedure
This was trained on the 'grug' dataset, using the "HappyTransformers" library on Google Colab.
This model was trained for 4 epochs with learning rate 1e-2.
The notebook used to train has been included in this repo.

# Biases & Limitations
This likely contains the same biases and limitations as the original GPT-Neo-125M that it is based on, and additionally heavy biases from the grug datasets.

# Intended Use
This model is meant for fun, please do not take anything this caveman says seriously.

# Sample Use
```python
#Import model:
from happytransformer import HappyGeneration
happy_gen = HappyGeneration("GPT-NEO", "DarwinAnim8or/gpt-grug-125m")

#Set generation settings:
from happytransformer import GENSettings
args_top_k = GENSettings(no_repeat_ngram_size=3, do_sample=True,top_k=50, temperature=0.7, max_length=50, early_stopping=False)

#Generate a response:
result = happy_gen.generate_text("""Person: "Hello grug"
Grug: "hello person"
###
Person: "how are you grug"
Grug: "grug doing ok. grug find many berry. good for tribe."
###
Person: "what does grug think of new spear weapon?"
Grug: "grug no like new spear weapon. grug stick bigger. spear too small, break easy"
###
Person: "what does grug think of football?"
Grug: \"""", args=args_top_k)

print(result)
print(result.text)
```