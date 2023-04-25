---
library_name: fairseq
task: audio-to-audio
tags:
- fairseq
- audio
- audio-to-audio
- speech-to-speech-translation
language: en-zh
datasets:
- must_c
- covost2
widget:
- example_title: Common Voice sample 1
  src: https://huggingface.co/facebook/xm_transformer_600m-en_es-multi_domain/resolve/main/common_voice_en_18295850.mp3
---
# xm_transformer_600m-en_zh-multi_domain

[W2V2-Transformer](https://aclanthology.org/2021.acl-long.68/) speech-to-text translation model from fairseq S2T ([paper](https://arxiv.org/abs/2010.05171)/[code](https://github.com/pytorch/fairseq/tree/main/examples/speech_to_text)):
- English-Chinese
- Trained on MuST-C, CoVoST 2, Multilingual LibriSpeech, Common Voice v7 and CCMatrix
- Speech synthesis with [facebook/tts_transformer-zh-cv7_css10](https://huggingface.co/facebook/tts_transformer-zh-cv7_css10)

## Usage
```python
from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.speech_to_text.hub_interface import S2THubInterface
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
import IPython.display as ipd
import torchaudio


models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
    "facebook/xm_transformer_600m-en_zh-multi_domain",
    arg_overrides={"config_yaml": "config.yaml"},
)
model = models[0]
generator = task.build_generator(model, cfg)


# requires 16000Hz mono channel audio
audio, _ = torchaudio.load("/path/to/an/audio/file")

sample = S2THubInterface.get_model_input(task, audio)
text = S2THubInterface.get_prediction(task, model, generator, sample)

# speech synthesis
tts_models, tts_cfg, tts_task = load_model_ensemble_and_task_from_hf_hub(
  f"facebook/tts_transformer-zh-cv7_css10",
  arg_overrides={"vocoder": "griffin_lim", "fp16": False},
)
tts_model = tts_models[0]
TTSHubInterface.update_cfg_with_data_cfg(tts_cfg, tts_task.data_cfg)
tts_generator = tts_task.build_generator([tts_model], tts_cfg)

tts_sample = TTSHubInterface.get_model_input(tts_task, text)
wav, sr = TTSHubInterface.get_prediction(
    tts_task, tts_model, tts_generator, tts_sample
)

ipd.Audio(wav, rate=rate)
```

## Citation
```bibtex
@inproceedings{li-etal-2021-multilingual,
    title = "Multilingual Speech Translation from Efficient Finetuning of Pretrained Models",
    author = "Li, Xian  and
      Wang, Changhan  and
      Tang, Yun  and
      Tran, Chau  and
      Tang, Yuqing  and
      Pino, Juan  and
      Baevski, Alexei  and
      Conneau, Alexis  and
      Auli, Michael",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.68",
    doi = "10.18653/v1/2021.acl-long.68",
    pages = "827--838",
}

@inproceedings{wang-etal-2020-fairseq,
    title = "Fairseq {S}2{T}: Fast Speech-to-Text Modeling with Fairseq",
    author = "Wang, Changhan  and
      Tang, Yun  and
      Ma, Xutai  and
      Wu, Anne  and
      Okhonko, Dmytro  and
      Pino, Juan",
    booktitle = "Proceedings of the 1st Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2020",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.aacl-demo.6",
    pages = "33--39",
}
```
