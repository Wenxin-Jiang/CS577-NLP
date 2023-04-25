---
library_name: keras
license: apache-2.0
tags:
- seq2seq
- translation
language:
- en
- fr
---

## Keras Implementation of Character-level recurrent sequence-to-sequence model 

This repo contains the model and the notebook [to this Keras example on Character-level recurrent sequence-to-sequence model](https://keras.io/examples/nlp/lstm_seq2seq/).

Full credits to : [fchollet](https://twitter.com/fchollet)

Model reproduced by : [Sumedh](https://huggingface.co/sumedh)

## Intended uses & limitations

This model implements a basic character-level recurrent sequence-to-sequence network for translating short English sentences into short French sentences, character-by-character. Note that it is fairly unusual to do character-level machine translation, as word-level models are more common in this domain. It works best on text of length <= 15 characters.

## Training and evaluation data
English to French translation data from
https://www.manythings.org/anki/

## Training procedure
- We start with input sequences from a domain (e.g. English sentences) and corresponding target sequences from another domain (e.g. French sentences).
- An encoder LSTM turns input sequences to 2 state vectors (we keep the last LSTM state and discard the outputs).
- A decoder LSTM is trained to turn the target sequences into the same sequence but offset by one timestep in the future, a training process called "teacher forcing" in this context. It uses as initial state the state vectors from the encoder. Effectively, the decoder learns to generate targets[t+1...] given targets[...t], conditioned on the input sequence.
- In inference mode, when we want to decode unknown input sequences, we: - Encode the input sequence into state vectors - Start with a target sequence of size 1 (just the start-of-sequence character) - Feed the state vectors and 1-char target sequence to the decoder to produce predictions for the next character - Sample the next character using these predictions (we simply use argmax). - Append the sampled character to the target sequence - Repeat until we generate the end-of-sequence character or we hit the character limit.

### Training hyperparameters

The following hyperparameters were used during training:

| name | learning_rate | decay | rho | momentum | epsilon | centered | training_precision |
|----|-------------|-----|---|--------|-------|--------|------------------|
|RMSprop|0.0010000000474974513|0.0|0.8999999761581421|0.0|1e-07|False|float32|

```python
batch_size = 64  # Batch size for training.
epochs = 100  # Number of epochs to train for.
latent_dim = 256  # Latent dimensionality of the encoding space.
num_samples = 10000  # Number of samples to train on.
```

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>