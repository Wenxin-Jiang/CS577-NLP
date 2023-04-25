---
license: cc-by-nc-4.0
library_name: fairseq
task: text-to-speech
tags:
- fairseq
- audio
- text-to-speech
language: hk
---
## unit_hifigan_HK_layer12.km2500_frame_TAT-TTS

Hokkien unit HiFiGAN based vocoder from fairseq:
- Trained with [TAT-TTS](https://sites.google.com/speech.ntut.edu.tw/fsw/home/tat-tts-corpus) data with 4 speakers in Taiwanese Hokkien accent. See [here]( https://research.facebook.com/publications/hokkien-direct-speech-to-speech-translation) 
for more training details.

## Usage

```python
import json
import os
from pathlib import Path

import IPython.display as ipd
from fairseq import hub_utils
from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.speech_to_text.hub_interface import S2THubInterface
from fairseq.models.text_to_speech import CodeHiFiGANVocoder
from fairseq.models.text_to_speech.hub_interface import VocoderHubInterface

from huggingface_hub import snapshot_download
import torchaudio

cache_dir = os.getenv("HUGGINGFACE_HUB_CACHE")

# speech synthesis           
library_name = "fairseq"
cache_dir = (
    cache_dir or (Path.home() / ".cache" / library_name).as_posix()
)
cache_dir = snapshot_download(
    f"facebook/unit_hifigan_HK_layer12.km2500_frame_TAT-TTS", cache_dir=cache_dir, library_name=library_name
)

x = hub_utils.from_pretrained(
    cache_dir,
    "model.pt",
    ".",
    archive_map=CodeHiFiGANVocoder.hub_models(),
    config_yaml="config.json",
    fp16=False,
    is_vocoder=True,
)

with open(f"{x['args']['data']}/config.json") as f:
    vocoder_cfg = json.load(f)
assert (
    len(x["args"]["model_path"]) == 1
), "Too many vocoder models in the input"

vocoder = CodeHiFiGANVocoder(x["args"]["model_path"][0], vocoder_cfg)
tts_model = VocoderHubInterface(vocoder_cfg, vocoder)

tts_sample = tts_model.get_model_input(unit)
wav, sr = tts_model.get_prediction(tts_sample)

ipd.Audio(wav, rate=sr)
```