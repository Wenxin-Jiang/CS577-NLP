---
language: "en"
thumbnail:
tags:
- speech-translation
- CTC
- Attention
- Transformer
- pytorch
- speechbrain
- automatic-speech-recognition
metrics:
- BLEU
---

# Conformer Encoder/Decoder for Speech Translation

This model was trained with [SpeechBrain](https://speechbrain.github.io), and is based on the Fisher Callhome recipie. 
The performance of the model is the following:

| Release | CoVoSTv2 JA->EN Test BLEU | Custom Dataset Validation BLEU | Custom Dataset Test BLEU | GPUs |
|:-------------:|:--------------:|:--------------:|:--------------:|:--------:|
| 01-13-21 | 9.73 | 8.38 | 12.01 | 1xRTX 3090 |


This model was trained on subtitled audio downloaded from YouTube, and was not fine-tuned on the CoVoSTv2 training set.
When calculating the BLEU score for CoVoSTv2, the utterances were first preprocessed by the same pipeline that preprocessed the original data for the model, which includes removing all punctuation outside of apostrophes, and removing capitalization, similar to the data preprocessing done for the Fisher Callhome dataset in the speechbrain recipe.
## Pipeline description

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

## Install SpeechBrain

First of all, install SpeechBrain with the following command:

```
pip install speechbrain
```

### Transcribing your own audio files (Spoken Japanese, to written English)

```python
from speechbrain.pretrained import EncoderDecoderASR
st_model = EncoderDecoderASR.from_hparams(source="bob80333/speechbrain_ja2en_st_63M_yt600h")
st_model.transcribe_file("your_file_here.wav")
```
### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Limitations:
The model is likely to get caught in repetitions.  The model is not very good at translation, which is reflected by its low BLEU scores.
The outputs of this model are unlikely to be correct, do not rely on it for any serious purpose.
This model was trained on data from Youtube, and has inherited whatever biases can be found in Youtube audio/subtitles.
The creator of this model doesn't actually know Japanese.