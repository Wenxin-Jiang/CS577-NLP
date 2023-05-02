---
language:
- es
tags:
- audio  # Example: audio
- automatic-speech-recognition  # Example: 
datasets:
- multilingual_librispeech

metrics:
- eval_wer: 0.073

model-index:
- name: wav2vec2-spanish-multilibrispeech
  results:
  - task: 
      type: automatic-speech-recognition  # Required. Example: automatic-speech-recognition
      name: Speech Recognition  # Optional. Example: Speech Recognition
    dataset:
      type: multilingual_librispeech # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: multilingual_librispeech es # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
      - type: wer
        value: 0.073
        name: eval_wer
      - type: loss
        value: 0.086
        name: eval_loss
---

This is a model for automatic speech recognition in spanish, by using the Spanish portion of [multilingual_librispeech](https://huggingface.co/datasets/multilingual_librispeech) and the [pre-trained wav2vec2 multilingual from Facebook](https://huggingface.co/facebook/wav2vec2-large-xlsr-53)


For training the model, we used the same parameters as they recommend in [the paper](https://arxiv.org/abs/2006.13979). We trained for a total of 15 epochs, obtaining a final wer of 0.073.

An example of how to use this model:

```python
from transformers import Wav2Vec2Tokenizer, AutoModelForCTC

tokenizer = Wav2Vec2Tokenizer.from_pretrained(
            "IIC/wav2vec2-spanish-multilibrispeech"
        )

model = AutoModelForCTC.from_pretrained(
            "IIC/wav2vec2-spanish-multilibrispeech"
        )

```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.