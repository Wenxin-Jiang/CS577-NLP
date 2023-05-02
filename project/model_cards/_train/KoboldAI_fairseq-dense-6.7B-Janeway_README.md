---
language: en
license: mit
---
# Fairseq-dense 6.7B - Janeway
## Model Description
Fairseq-dense 6.7B-Janeway is a finetune created using Fairseq's MoE dense model.
## Training data
The training data contains around 2210 ebooks, mostly in the sci-fi and fantasy genres. The dataset is identical as dataset used by GPT-Neo-2.7B-Janeway.
Some parts of the dataset have been prepended using the following text: `[Genre: <genre1>,<genre2>]`
### How to use
You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:
```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='KoboldAI/fairseq-dense-13B-Janeway')
>>> generator("Welcome Captain Janeway, I apologize for the delay.", do_sample=True, min_length=50)
[{'generated_text': 'Welcome Captain Janeway, I apologize for the delay."\nIt's all right," Janeway said. "I'm certain that you're doing your best to keep me informed of what\'s going on."'}]
```
### Limitations and Biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion).

### BibTeX entry and citation info
```
Artetxe et al. (2021): Efficient Large Scale Language Modeling with Mixtures of Experts
```