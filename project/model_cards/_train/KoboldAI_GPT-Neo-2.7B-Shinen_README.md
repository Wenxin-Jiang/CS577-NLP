---
language: en
license: mit
---
# GPT-Neo 2.7B - Shinen
## Model Description
GPT-Neo 2.7B-Shinen is a finetune created using EleutherAI's GPT-Neo 2.7B model. Compared to GPT-Neo-2.7-Horni, this model is much heavier on the sexual content.

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
>>> generator = pipeline('text-generation', model='KoboldAI/GPT-Neo-2.7B-Shinen')
>>> generator("She was staring at me", do_sample=True, min_length=50)
[{'generated_text': 'She was staring at me with a look that said it all. She wanted me so badly tonight that I wanted'}]
```
### Limitations and Biases
GPT-Neo was trained as an autoregressive language model. This means that its core functionality is taking a string of text and predicting the next token. While language models are widely used for tasks other than this, there are a lot of unknowns with this work.
GPT-Neo-Shinen was trained on a dataset known to contain profanity, lewd, and otherwise abrasive language. GPT-Neo-Shinen *WILL* produce socially unacceptable text without warning.
GPT-Neo-Shinen will respond to particular prompts and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results.
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