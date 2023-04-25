---
license: cc-by-nc-4.0
library_name: fairseq
task: text-to-speech
tags:
- fairseq
- audio
- text-to-speech
language: en
datasets:
- mtedx
- covost2
- europarl_st
- voxpopuli
widget:
- example_title: Common Voice sample 1
  src: https://huggingface.co/facebook/xm_transformer_600m-es_en-multi_domain/resolve/main/common_voice_es_19966634.flac
---
## unit_hifigan_mhubert_vp_en_es_fr_it3_400k_layer11_km1000_lj_dur

Speech-to-speech translation model from fairseq S2UT ([paper](https://arxiv.org/abs/2204.02967)/[code](https://github.com/facebookresearch/fairseq/blob/main/examples/speech_to_speech/docs/enhanced_direct_s2st_discrete_units.md)):
- Spanish-English
- Trained on mTEDx, CoVoST 2, Europarl-ST and VoxPopuli

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

#models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
#     "facebook/xm_transformer_s2ut_800m-es-en-st-asr-bt_h1_2022",
#     arg_overrides={"config_yaml": "config.yaml", "task": "speech_to_text"},
#     cache_dir=cache_dir,
# )
# model = models[0].cpu()
# cfg["task"].cpu = True
# generator = task.build_generator([model], cfg)


# # requires 16000Hz mono channel audio
# audio, _ = torchaudio.load("/Users/lpw/git/api-inference-community/docker_images/fairseq/tests/samples/sample2.flac")

# sample = S2THubInterface.get_model_input(task, audio)
# unit = S2THubInterface.get_prediction(task, model, generator, sample)

# speech synthesis           
library_name = "fairseq"
cache_dir = (
    cache_dir or (Path.home() / ".cache" / library_name).as_posix()
)
cache_dir = snapshot_download(
    f"facebook/unit_hifigan_mhubert_vp_en_es_fr_it3_400k_layer11_km1000_lj_dur", cache_dir=cache_dir, library_name=library_name
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