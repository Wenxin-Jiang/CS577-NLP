---
language:
  - en
tags:
- translation
- speech
- audio
- automatic-speech-recognition
datasets:
- whisper
metrics:
- WER
license: mit
---
This model was forked from the original [OpenAI whisper model](https://github.com/openai/whisper).

# Whisper

## Model
Whisper is a multi-lingual speech-to-text model.
It takes in raw audio recordings from many languages and outputs transcriptions in the language of origin or translated to english.
The model first converts speech to spectrograms, then uses an auto-regressive transformer to decode the speech to text.
Here is an overview of the architecture:

![model_architecure](https://github.com/jerpint/whisper/raw/main/approach.png)

For more information on the technical implementations, consult the [paper](https://cdn.openai.com/papers/whisper.pdf).
## Training Data

The model was trained on 680 000 hours of audio and associated transcripts trained from the internet.
The majority of the audio is in english (~65%) while the remainder is in other languages.
A total of 98 different languages were used in the dataset.

![image](https://user-images.githubusercontent.com/18450628/204110014-e2684385-d790-4dd7-8ce1-47168efb2726.png)


## Model Variations

OpenAI has released 9 different versions of the model, trained either on english-only audio or on multilingual data.

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

## Limitations and bias

In the [paper](https://cdn.openai.com/papers/whisper.pdf), they find a direct corelation between performance on a given language and the amount of data available in the dataset.
As such, languages that are under-represented in the scraped dataset perform less well in whisper.
Because english is much more prevalent than other languages, the model will likely perform better in english.
This is shown in the following figure, where a lower word error rate (WER) indicates a better performance:

![model_performance](https://github.com/jerpint/whisper/raw/main/language-breakdown.svg)
