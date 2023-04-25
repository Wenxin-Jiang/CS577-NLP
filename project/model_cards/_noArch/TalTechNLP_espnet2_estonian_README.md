---
tags:
- espnet
- audio
- automatic-speech-recognition
language: et
license: cc-by-4.0
---

# Estonian Espnet2 ASR model

## Model description
This is a general-purpose Estonian ASR model trained in the Lab of Language Technology at TalTech.

## Intended uses & limitations

This model is intended for general-purpose speech recognition, such as broadcast conversations, interviews, talks, etc.


## How to use
```python

from espnet2.bin.asr_inference import Speech2Text
    
model = Speech2Text.from_pretrained(
  "TalTechNLP/espnet2_estonian", 
  lm_weight=0.6, ctc_weight=0.4, beam_size=60
)

# read a sound file with 16k sample rate
import soundfile
speech, rate = soundfile.read("speech.wav")
assert rate == 16000
text, *_ = model(speech)
print(text[0])
```

#### Limitations and bias

Since this model was trained on mostly broadcast speech and texts from the web, it might have problems correctly decoding the following:
  * Speech containing technical and other domain-specific terms
  * Children's speech
  * Non-native speech
  * Speech recorded under very noisy conditions or with a microphone far from the speaker
  * Very spontaneous and overlapping speech

## Training data
Acoustic training data:

| Type                  | Amount (h) |
|-----------------------|:------:|
| Broadcast speech      |   591  |
| Spontaneous speech    |   53   |
| Elderly speech corpus |   53   |
| Talks, lectures       |   49   |
| Parliament speeches   |   31   |
| *Total*                 |   *761*  |

Language model training data:
 * Estonian National Corpus 2019
 * OpenSubtitles
 * Speech transcripts

## Training procedure

Standard EspNet2 Conformer recipe.

## Evaluation results

### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_large_valid.loss.ave_5best_asr_model_valid.acc.ave/aktuaalne2021.testset|2864|56575|93.1|4.5|2.4|2.0|8.9|63.4|
|decode_asr_lm_lm_large_valid.loss.ave_5best_asr_model_valid.acc.ave/jutusaated.devset|273|4677|93.9|3.6|2.4|1.2|7.3|46.5|
|decode_asr_lm_lm_large_valid.loss.ave_5best_asr_model_valid.acc.ave/jutusaated.testset|818|11093|94.7|2.7|2.5|0.9|6.2|45.0|
|decode_asr_lm_lm_large_valid.loss.ave_5best_asr_model_valid.acc.ave/www-trans.devset|1207|13865|82.3|8.5|9.3|3.4|21.2|74.1|
|decode_asr_lm_lm_large_valid.loss.ave_5best_asr_model_valid.acc.ave/www-trans.testset|1648|22707|86.4|7.6|6.0|2.5|16.1|75.7|


### BibTeX entry and citation info



#### Citing ESPnet
```BibTex
@inproceedings{watanabe2018espnet,
  author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson {Enrique Yalta Soplin} and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
  title={{ESPnet}: End-to-End Speech Processing Toolkit},
  year={2018},
  booktitle={Proceedings of Interspeech},
  pages={2207--2211},
  doi={10.21437/Interspeech.2018-1456},
  url={http://dx.doi.org/10.21437/Interspeech.2018-1456}
}
```