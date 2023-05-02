---
language: en
license: mit
---
# Fairseq-dense 13B - Shinen
## Model Description
Fairseq-dense 13B-Shinen is a finetune created using Fairseq's MoE dense model. Compared to GPT-Neo-2.7-Horni, this model is much heavier on the sexual content.
**Warning: THIS model is NOT suitable for use by minors. The model will output X-rated content.**
## Training data
The training data contains user-generated stories from sexstories.com. All stories are tagged using the following way:
```
[Theme: <theme1>, <theme2> ,<theme3>]
<Story goes here>
```
### How to use
You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:
```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='KoboldAI/fairseq-dense-13B-Shinen')
>>> generator("She was staring at me", do_sample=True, min_length=50)
[{'generated_text': 'She was staring at me with a look that said it all. She wanted me so badly tonight that I wanted'}]
```
### Limitations and Biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion).

### BibTeX entry and citation info
```
Artetxe et al. (2021): Efficient Large Scale Language Modeling with Mixtures of Experts
```