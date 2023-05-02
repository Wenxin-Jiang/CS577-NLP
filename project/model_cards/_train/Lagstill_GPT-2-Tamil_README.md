---
license: bigscience-bloom-rail-1.0

widget :
- text: "அகத்தின் அழகு"
  example_title: "அகத்தின் அழகு"
- text : "கடுகு சிறுத்தாலும்"
  example_title: "கடுகு சிறுத்தாலும்"
- text : "யானைக்கும் அடி"
  example_title : "யானைக்கும் அடி"
---
# GPT2-Tamil

## Model description
GPT2-Tamil is a GPT-2 transformer model fine Tuned on a  large corpus of Tamil data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way with an automatic process to generate inputs and labels from those texts. More precisely, it was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence, shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the predictions for the token i only uses the inputs from 1 to i but not the future tokens.

This way, the model learns an inner representation of the Tamil language that can then be used to extract features useful for downstream tasks.
## Intended uses & limitations

You can use the raw model for text generation or fine-tune it to a downstream task. See the
[model hub](https://huggingface.co/models?filter=gpt2) to look for fine-tuned versions on a task that interests you.

## Usage
You can use this model for Tamil text generation:
```python
>>> from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
>>> tokenizer = GPT2Tokenizer.from_pretrained("Lagstill/GPT-2-Tamil")
>>> model = TFGPT2LMHeadModel.from_pretrained("Lagstill/GPT-2-Tamil")
>>> text = "அகத்தின் அழகு"
>>> encoded_text = tokenizer.encode(text, return_tensors='tf')
>>> beam_output = model.generate(
    encoded_text,
    max_length=100,
    num_beams=5,
    temperature=0.7,
    no_repeat_ngram_size=2,
    num_return_sequences=5
    )
>>> print(tokenizer.decode(beam_output[0], skip_special_tokens=True))
```
---
