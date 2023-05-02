---
license: mit
language:
- en
widget:
- text: >-
    A nervous passenger is about to book a flight ticket, and he asks the
    airlines' ticket seller, 'I hope your planes are safe. Do they have a good
    track record for safety?' The airline agent replies, 'Sir, I can guarantee
    you, we've never had a plane that has crashed more than once.'
  example_title: A joke
- text: >-
    Let me, however, hasten to assure that I am the same Gandhi as I was in
    1920. I have not changed in any fundamental respect. I attach the same
    importance to nonviolence that I did then. If at all, my emphasis on it has
    grown stronger. There is no real contradiction between the present
    resolution and my previous writings and utterances.
  example_title: Not a joke
tags:
- roberta
---

### What is this?
This model has been developed to detect "narrative-style" jokes, stories and anecdotes (i.e. they are narrated as a story) spoken during speeches or conversations etc. It works best when jokes/anecdotes are at least 40 words or longer. It is based on Facebook's [RoBerta-MUPPET](https://huggingface.co/facebook/muppet-roberta-base). 

The training dataset was a private collection of around 2000 jokes. This model has not been trained or tested on one-liners, puns or Reddit-style language-manipulation jokes such as knock-knock, Q&A jokes etc.

See the example in the inference widget or How to use section for what constitues a narrative-style joke.

For a slightly more accurate model (0.4% more) that is 65% slower at inference, see the [Deberta-v3 model](https://huggingface.co/Reggie/DeBERTa-v3-base-joke_detector). For a much more inaccurate model (2.4% less) that is way faster at inference, see the [distilbert model](https://huggingface.co/Reggie/distilbert-joke_detector).

### Install these first
You'll need to pip install transformers & maybe sentencepiece

### How to use
```python
from transformers import pipeline
import torch
device = 0 if torch.cuda.is_available() else -1
model_name = 'Reggie/muppet-roberta-base-joke_detector'
max_seq_len = 510

pipe = pipeline(model=model_name, device=device, truncation=True, max_length=max_seq_len)
is_it_a_joke = """A nervous passenger is about to book a flight ticket, and he asks the airlines' ticket seller, "I hope your planes are safe. Do they have a good track record for safety?" The airline agent replies, "Sir, I can guarantee you, we've never had a plane that has crashed more than once." """
result = pipe(is_it_a_joke) # [{'label': 'LABEL_1', 'score': 0.7313136458396912}]
print('This is a joke') if result[0]['label'] == 'LABEL_1' else print('This is not a joke')

# Or if you don't want to use pipelines
from transformers import pipeline
import torch
device = 0 if torch.cuda.is_available() else -1
model_name = 'Reggie/muppet-roberta-base-joke_detector'
max_seq_len = 510

tokenizer = AutoTokenizer.from_pretrained(model_name, model_max_length=510)
model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
input = tokenizer(is_it_a_joke, '', truncation=True, return_tensors="pt")
output = model(input["input_ids"].to(device))
prediction = torch.softmax(output["logits"][0], -1).tolist()
pred_out = 1 if prediction[0] < prediction[1] else 0
print('This is a joke') if pred_out == 1 else print('This is not a joke')
```