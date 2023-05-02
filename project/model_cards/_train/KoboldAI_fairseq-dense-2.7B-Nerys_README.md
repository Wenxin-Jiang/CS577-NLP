---
language: en
license: mit
---
# Fairseq-dense 2.7B - Nerys
## Model Description
Fairseq-dense 2.7B-Nerys is a finetune created using Fairseq's MoE dense model.
## Training data
The training data contains around 2500 ebooks in various genres (the "Pike" dataset), a CYOA dataset called "CYS" and 50 Asian "Light Novels" (the "Manga-v1" dataset).
Most parts of the dataset have been prepended using the following text: `[Genre: <genre1>, <genre2>]`
### How to use
You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:
```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='KoboldAI/fairseq-dense-2.7B-Nerys')
>>> generator("Welcome Captain Janeway, I apologize for the delay.", do_sample=True, min_length=50)
[{'generated_text': 'Welcome Captain Janeway, I apologize for the delay."\nIt's all right," Janeway said. "I'm certain that you're doing your best to keep me informed of what\'s going on."'}]
```
### Limitations and Biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion).

### BibTeX entry and citation info
```
Artetxe et al. (2021): Efficient Large Scale Language Modeling with Mixtures of Experts
```