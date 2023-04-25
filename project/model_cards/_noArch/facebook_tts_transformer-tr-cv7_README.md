---
library_name: fairseq
task: text-to-speech
tags:
- fairseq
- audio
- text-to-speech
language: tr
datasets:
- common_voice
widget:
- text: "Merhaba, bu bir deneme çalışmasıdır."
  example_title: "Hello, this is a test run."
---
# tts_transformer-tr-cv7

[Transformer](https://arxiv.org/abs/1809.08895) text-to-speech model from fairseq S^2 ([paper](https://arxiv.org/abs/2109.06912)/[code](https://github.com/pytorch/fairseq/tree/main/examples/speech_synthesis)):
- Turkish
- Single-speaker male voice
- Trained on [Common Voice v7](https://commonvoice.mozilla.org/en/datasets)

## Usage

```python
from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
import IPython.display as ipd


models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
    "facebook/tts_transformer-tr-cv7",
    arg_overrides={"vocoder": "hifigan", "fp16": False}
)
model = models[0]
TTSHubInterface.update_cfg_with_data_cfg(cfg, task.data_cfg)
generator = task.build_generator(model, cfg)

text = "Merhaba, bu bir deneme çalışmasıdır."

sample = TTSHubInterface.get_model_input(task, text)
wav, rate = TTSHubInterface.get_prediction(task, model, generator, sample)

ipd.Audio(wav, rate=rate)
```

See also [fairseq S^2 example](https://github.com/pytorch/fairseq/blob/main/examples/speech_synthesis/docs/common_voice_example.md).

## Citation

```bibtex
@inproceedings{wang-etal-2021-fairseq,
    title = "fairseq S{\^{}}2: A Scalable and Integrable Speech Synthesis Toolkit",
    author = "Wang, Changhan  and
      Hsu, Wei-Ning  and
      Adi, Yossi  and
      Polyak, Adam  and
      Lee, Ann  and
      Chen, Peng-Jen  and
      Gu, Jiatao  and
      Pino, Juan",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-demo.17",
    doi = "10.18653/v1/2021.emnlp-demo.17",
    pages = "143--152",
}
```
