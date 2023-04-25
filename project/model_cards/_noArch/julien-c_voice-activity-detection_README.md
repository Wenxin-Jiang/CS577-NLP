---
tags:
- pyannote
- audio
- voice-activity-detection
datasets:
- dihard
license: mit
inference: false
---

## Example pyannote-audio Voice Activity Detection model 

### `pyannote.audio.models.segmentation.PyanNet`

♻️ Imported from https://github.com/pyannote/pyannote-audio-hub

This model was trained by @hbredin.


### Demo: How to use in pyannote-audio

```python
from pyannote.audio.core.inference import Inference

model = Inference('julien-c/voice-activity-detection', device='cuda')
model({
	"audio": "TheBigBangTheory.wav"
})
```

### Citing pyannote-audio

```BibTex
@inproceedings{Bredin2020,
  Title = {{pyannote.audio: neural building blocks for speaker diarization}},
  Author = {{Bredin}, Herv{\'e} and {Yin}, Ruiqing and {Coria}, Juan Manuel and {Gelly}, Gregory and {Korshunov}, Pavel and {Lavechin}, Marvin and {Fustes}, Diego and {Titeux}, Hadrien and {Bouaziz}, Wassim and {Gill}, Marie-Philippe},
  Booktitle = {ICASSP 2020, IEEE International Conference on Acoustics, Speech, and Signal Processing},
  Address = {Barcelona, Spain},
  Month = {May},
  Year = {2020},
}
```

or

```bibtex
@inproceedings{Lavechin2020,
    author = {Marvin Lavechin and Marie-Philippe Gill and Ruben Bousbib and Herv\'{e} Bredin and Leibny Paola Garcia-Perera},
    title = {{End-to-end Domain-Adversarial Voice Activity Detection}},
    year = {2020},
    url = {https://arxiv.org/abs/1910.10655},
}
```

