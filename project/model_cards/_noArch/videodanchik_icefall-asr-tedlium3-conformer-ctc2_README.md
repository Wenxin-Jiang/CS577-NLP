---
datasets: 
  - Tedlium3
language: 
  - en
license: cc-by-nc-nd-3.0
metrics: 
  - 
    name: "dev"
    type: wer
    value: 5.60
  - 
    name: "test"
    type: wer
    value: 5.33
tags: 
  - k2
  - icefall
  - automatic-speech-recognition
---

# Tedlium3

This is an ASR ctc attention encoder-decoder recipe for the Tedlium3 corpus.
The encoder is the re-worked conformer model.
Language models are downloaded from https://kaldi-asr.org/models/m5

## Performance Record

### conformer_ctc2

| Decodeing method         | dev WER    | test WER |
|--------------------------|------------|---------|
| ctc-decoding             |  6.45   | 5.96  |
| 1best                    |  5.92   | 5.51  |
| whole-lattice-rescoring  |  5.96   | 5.47  |
| attention-decoder        |  5.60   | 5.33  |

See the [recipe](https://github.com/k2-fsa/icefall/tree/master/egs/tedlium3/ASR/conformer_ctc2) for details.
