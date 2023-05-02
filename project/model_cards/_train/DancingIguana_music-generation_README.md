---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: music-generation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# music-generation

This model a trained from scratch version of [distilgpt2](https://huggingface.co/distilgpt2) on a dataset where the text represents musical notes. The [dataset](https://www.kaggle.com/datasets/soumikrakshit/classical-music-midi) consists of one stream of notes from MIDI files (the stream with most notes), where all of the melodies were transposed either to C major or A minor. Also, the BPM of the song is ignored, the duration of each note is based on its quarter length.

Each element in the melody is represented by a series of letters and numbers with the following structure.
* For a note: ns[pitch of the note as a string]s[duration]
  * Examples: nsC4s0p25, nsF7s1p0, 
* For a rest: rs[duration]:
  * Examples: rs0p5, rs1q6
* For a chord: cs[number of notes in chord]s[pitches of chords separated by "s"]s[duration]
  * Examples: cs2sE7sF7s1q3, cs2sG3sGw3s0p25
  
The following special symbols are replaced in the strings by the following:
* . = p
* / = q
* # = 
* - = t

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
