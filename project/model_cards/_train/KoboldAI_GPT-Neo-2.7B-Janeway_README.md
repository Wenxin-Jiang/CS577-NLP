---
language: en
license: mit
---
# GPT-Neo 2.7B - Janeway
## Model Description
GPT-Neo 2.7B-Janeway is a finetune created using EleutherAI's GPT-Neo 2.7B model.
## Training data
The training data contains around 2210 ebooks, mostly in the sci-fi and fantasy genres. The dataset is based on the same dataset used by GPT-Neo-2.7B-Picard, with 20% more data in various genres.
Some parts of the dataset have been prepended using the following text: `[Genre: <genre1>,<genre2>]`
### How to use
You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:
```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='KoboldAI/GPT-Neo-2.7B-Janeway')
>>> generator("Welcome Captain Janeway, I apologize for the delay.", do_sample=True, min_length=50)
[{'generated_text': 'Welcome Captain Janeway, I apologize for the delay."\nIt's all right," Janeway said. "I'm certain that you're doing your best to keep me informed of what\'s going on."'}]
```
### Limitations and Biases
GPT-Neo was trained as an autoregressive language model. This means that its core functionality is taking a string of text and predicting the next token. While language models are widely used for tasks other than this, there are a lot of unknowns with this work.
GPT-Neo was trained on the Pile, a dataset known to contain profanity, lewd, and otherwise abrasive language. Depending on your usecase GPT-Neo may produce socially unacceptable text. See Sections 5 and 6 of the Pile paper for a more detailed analysis of the biases in the Pile.
As with all language models, it is hard to predict in advance how GPT-Neo will respond to particular prompts and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results. 
### BibTeX entry and citation info
The model is made using the following software:
```bibtex
@software{gpt-neo,
  author       = {Black, Sid and
                  Leo, Gao and
                  Wang, Phil and
                  Leahy, Connor and
                  Biderman, Stella},
  title        = {{GPT-Neo: Large Scale Autoregressive Language 
                   Modeling with Mesh-Tensorflow}},
  month        = mar,
  year         = 2021,
  note         = {{If you use this software, please cite it using 
                   these metadata.}},
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.5297715},
  url          = {https://doi.org/10.5281/zenodo.5297715}
}
```