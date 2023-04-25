---
license: cc-by-nc-4.0
library_name: fairseq
task: audio-to-audio
tags:
- fairseq
- audio
- audio-to-audio
- speech-to-speech-translation

datasets:
- MuST-C

---
## xm_transformer_s2ut_en-hk

Speech-to-speech translation model with single-pass decoder (S2UT) from fairseq:
- English-Hokkien
- Trained with supervised data in TED domain, and weakly supervised data in TED and Audiobook domain. See [here]( https://research.facebook.com/publications/hokkien-direct-speech-to-speech-translation) 
for training details
- Speech synthesis with [facebook/unit_hifigan_HK_layer12.km2500_frame_TAT-TTS](https://huggingface.co/facebook/unit_hifigan_HK_layer12.km2500_frame_TAT-TTS)
- [Project Page](https://github.com/facebookresearch/fairseq/tree/ust/examples/hokkien)

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

models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
    "facebook/xm_transformer_s2ut_en-hk",
    arg_overrides={"config_yaml": "config.yaml", "task": "speech_to_text"},
    cache_dir=cache_dir,
)
#model = models[0].cpu()
#cfg["task"].cpu = True
generator = task.build_generator([model], cfg)


# requires 16000Hz mono channel audio
audio, _ = torchaudio.load("/path/to/an/audio/file")

sample = S2THubInterface.get_model_input(task, audio)
unit = S2THubInterface.get_prediction(task, model, generator, sample)

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