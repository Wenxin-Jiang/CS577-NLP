---
language:
  - id
  - ms
license: apache-2.0
tags:
  - g2p
  - text2text-generation
inference: false
---

# ID G2P LSTM

ID G2P LSTM is a grapheme-to-phoneme model based on the [LSTM](https://doi.org/10.1162/neco.1997.9.8.1735) architecture. This model was trained from scratch on a modified [Malay/Indonesian lexicon](https://huggingface.co/datasets/bookbot/id_word2phoneme).

This model was trained using the [Keras](https://keras.io/) framework. All training was done on Google Colaboratory. We adapted the [LSTM training script](https://keras.io/examples/nlp/lstm_seq2seq/) provided by the official Keras Code Example.

## Model

| Model         | #params | Arch. | Training/Validation data |
| ------------- | ------- | ----- | ------------------------ |
| `id-g2p-lstm` | 596K    | LSTM  | Malay/Indonesian Lexicon |

![](./model.png)

## Training Procedure

<details>
  <summary>Model Config</summary>

    latent_dim: 256
    num_encoder_tokens: 28
    num_decoder_tokens: 32
    max_encoder_seq_length: 24
    max_decoder_seq_length: 25

</details>

<details>
  <summary>Training Setting</summary>

    batch_size: 64
    optimizer: "rmsprop"
    loss: "categorical_crossentropy"
    learning_rate: 0.001
    epochs: 100

</details>

## How to Use

<details>
  <summary>Tokenizers</summary>

    g2id = {
        ' ': 27,
        "'": 0,
        '-': 1,
        'a': 2,
        'b': 3,
        'c': 4,
        'd': 5,
        'e': 6,
        'f': 7,
        'g': 8,
        'h': 9,
        'i': 10,
        'j': 11,
        'k': 12,
        'l': 13,
        'm': 14,
        'n': 15,
        'o': 16,
        'p': 17,
        'q': 18,
        'r': 19,
        's': 20,
        't': 21,
        'u': 22,
        'v': 23,
        'w': 24,
        'y': 25,
        'z': 26
    }

    p2id = {
        '\t': 0,
        '\n': 1,
        ' ': 31,
        '-': 2,
        'a': 3,
        'b': 4,
        'd': 5,
        'e': 6,
        'f': 7,
        'g': 8,
        'h': 9,
        'i': 10,
        'j': 11,
        'k': 12,
        'l': 13,
        'm': 14,
        'n': 15,
        'o': 16,
        'p': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'z': 24,
        'ŋ': 25,
        'ə': 26,
        'ɲ': 27,
        'ʃ': 28,
        'ʒ': 29,
        'ʔ': 30
    }

</details>

```py
import keras
import numpy as np
from huggingface_hub import from_pretrained_keras

latent_dim = 256
bos_token, eos_token, pad_token = "\t", "\n", " "
num_encoder_tokens, num_decoder_tokens = 28, 32
max_encoder_seq_length, max_decoder_seq_length = 24, 25

model = from_pretrained_keras("bookbot/id-g2p-lstm")

encoder_inputs = model.input[0]
encoder_outputs, state_h_enc, state_c_enc = model.layers[2].output
encoder_states = [state_h_enc, state_c_enc]
encoder_model = keras.Model(encoder_inputs, encoder_states)

decoder_inputs = model.input[1]

decoder_state_input_h = keras.Input(shape=(latent_dim,), name="input_3")
decoder_state_input_c = keras.Input(shape=(latent_dim,), name="input_4")
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_lstm = model.layers[3]
decoder_outputs, state_h_dec, state_c_dec = decoder_lstm(
    decoder_inputs, initial_state=decoder_states_inputs
)
decoder_states = [state_h_dec, state_c_dec]
decoder_dense = model.layers[4]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = keras.Model(
    [decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states
)

def inference(sequence):
    id2p = {v: k for k, v in p2id.items()}

    input_seq = np.zeros(
        (1, max_encoder_seq_length, num_encoder_tokens), dtype="float32"
    )

    for t, char in enumerate(sequence):
        input_seq[0, t, g2id[char]] = 1.0
    input_seq[0, t + 1 :, g2id[pad_token]] = 1.0

    states_value = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, p2id[bos_token]] = 1.0

    stop_condition = False
    decoded_sentence = ""
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = id2p[sampled_token_index]
        decoded_sentence += sampled_char

        if sampled_char == eos_token or len(decoded_sentence) > max_decoder_seq_length:
            stop_condition = True

        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.0

        states_value = [h, c]
    return decoded_sentence.replace(eos_token, "")

inference("mengembangkannya")
```

## Authors

ID G2P LSTM was trained and evaluated by [Ananto Joyoadikusumo](https://anantoj.github.io/), [Steven Limcorn](https://stevenlimcorn.github.io/), [Wilson Wongso](https://w11wo.github.io/). All computation and development are done on Google Colaboratory.

## Framework versions

- Keras 2.8.0
- TensorFlow 2.8.0
