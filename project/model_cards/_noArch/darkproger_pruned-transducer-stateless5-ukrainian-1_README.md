---
language: 
  - uk
tags:
- automatic-speech-recognition
- audio
license: cc-by-nc-sa-4.0
datasets:
- https://github.com/egorsmkv/speech-recognition-uk
- mozilla-foundation/common_voice_6_1
metrics:
- wer
model-index:
- name: Ukrainian pruned_transducer_stateless5 v1.0.0
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice uk
      type: mozilla-foundation/common_voice_6_1
      split: test
      args: uk
    metrics:
       - name: Validation WER
         type: wer
         value: 13.37
---

`pruned_transducer_stateless5` with Conformer encoder for Ukrainian: https://github.com/proger/icefall/tree/uk

[Data Filtering](https://github.com/proger/uk)

[Tensorboard run](https://tensorboard.dev/experiment/8WizOEvHR8CqmQAOsr4ALg/)

```
./pruned_transducer_stateless5/train.py \
  --world-size 2 \
  --num-epochs 30 \
  --start-epoch 1 \
  --full-libri 1 \
  --exp-dir pruned_transducer_stateless5/exp-uk-shuf \
  --max-duration 500 \
  --use-fp16 1 \
  --num-encoder-layers 18 \
  --dim-feedforward 1024 \
  --nhead 4 \
  --encoder-dim 256 \
  --decoder-dim 512 \
  --joiner-dim 512 \
  --bpe-model uk/data/lang_bpe_250/bpe.model
```

```
./pruned_transducer_stateless5/decode.py \
  --epoch 27 \
  --avg 15 \
  --use-averaged-model True \
  --exp-dir pruned_transducer_stateless5/exp-uk-shuf \
  --decoding-method fast_beam_search \
  --num-encoder-layers 18 \
  --dim-feedforward 1024 \
  --nhead 4 \
  --encoder-dim 256 \
  --decoder-dim 512 \
  --joiner-dim 512 \
  --bpe-model uk/data/lang_bpe_250/bpe.model \
  --lang-dir uk/data/lang_bpe_250
```