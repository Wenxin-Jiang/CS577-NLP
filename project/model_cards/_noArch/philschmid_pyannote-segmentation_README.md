---
tags:
- pyannote
- pyannote-audio
- pyannote-audio-model
- audio
- voice
- speech
- speaker
- speaker-segmentation
- voice-activity-detection
- overlapped-speech-detection
- resegmentation
datasets:
- ami
- dihard
- voxconverse
license: mit
inference: false
---

# 🎹 Speaker segmentation

![Example](example.png)

Model from *[End-to-end speaker segmentation for overlap-aware resegmentation](http://arxiv.org/abs/2104.04045)*,  
by Hervé Bredin and Antoine Laurent.

[Online demo](https://huggingface.co/spaces/pyannote/pretrained-pipelines) is available as a Hugging Face Space.

## Support

For commercial enquiries and scientific consulting, please contact [me](mailto:herve@niderb.fr).  
For [technical questions](https://github.com/pyannote/pyannote-audio/discussions) and [bug reports](https://github.com/pyannote/pyannote-audio/issues), please check [pyannote.audio](https://github.com/pyannote/pyannote-audio) Github repository.

## Usage

Relies on pyannote.audio 2.0 currently in development: see [installation instructions](https://github.com/pyannote/pyannote-audio/tree/develop#installation).

### Voice activity detection

```python
from pyannote.audio.pipelines import VoiceActivityDetection
pipeline = VoiceActivityDetection(segmentation="pyannote/segmentation")
HYPER_PARAMETERS = {
  # onset/offset activation thresholds
  "onset": 0.5, "offset": 0.5,
  # remove speech regions shorter than that many seconds.
  "min_duration_on": 0.0,
  # fill non-speech regions shorter than that many seconds.
  "min_duration_off": 0.0
}
pipeline.instantiate(HYPER_PARAMETERS)
vad = pipeline("audio.wav")
# `vad` is a pyannote.core.Annotation instance containing speech regions
```

### Overlapped speech detection

```python
from pyannote.audio.pipelines import OverlappedSpeechDetection
pipeline = OverlappedSpeechDetection(segmentation="pyannote/segmentation")
pipeline.instantiate(HYPER_PARAMETERS)
osd = pipeline("audio.wav")
# `osd` is a pyannote.core.Annotation instance containing overlapped speech regions
```

### Resegmentation

```python
from pyannote.audio.pipelines import Resegmentation
pipeline = Resegmentation(segmentation="pyannote/segmentation", 
                          diarization="baseline")
pipeline.instantiate(HYPER_PARAMETERS)
resegmented_baseline = pipeline({"audio": "audio.wav", "baseline": baseline})
# where `baseline` should be provided as a pyannote.core.Annotation instance
```

### Raw scores

```python
from pyannote.audio import Inference
inference = Inference("pyannote/segmentation")
segmentation = inference("audio.wav")
# `segmentation` is a pyannote.core.SlidingWindowFeature
# instance containing raw segmentation scores like the 
# one pictured above (output)
```

## Reproducible research 

In order to reproduce the results of the paper ["End-to-end speaker segmentation for overlap-aware resegmentation
"](https://arxiv.org/abs/2104.04045), use `pyannote/segmentation@Interspeech2021` with the following hyper-parameters:

| Voice activity detection | `onset` | `offset` | `min_duration_on` | `min_duration_off` |
| ------------------------ | ------- | -------- | ----------------- | ------------------ |
| AMI Mix-Headset          | 0.684   | 0.577    | 0.181             | 0.037              |
| DIHARD3                  | 0.767   | 0.377    | 0.136             | 0.067              |
| VoxConverse              | 0.767   | 0.713    | 0.182             | 0.501              |

| Overlapped speech detection | `onset` | `offset` | `min_duration_on` | `min_duration_off` |
| --------------------------- | ------- | -------- | ----------------- | ------------------ |
| AMI Mix-Headset             | 0.448   | 0.362    | 0.116             | 0.187              |
| DIHARD3                     | 0.430   | 0.320    | 0.091             | 0.144              |
| VoxConverse                 | 0.587   | 0.426    | 0.337             | 0.112              |

| Resegmentation of VBx | `onset` | `offset` | `min_duration_on` | `min_duration_off` |
| --------------------- | ------- | -------- | ----------------- | ------------------ |
| AMI Mix-Headset       | 0.542   | 0.527    | 0.044             | 0.705              |
| DIHARD3               | 0.592   | 0.489    | 0.163             | 0.182              |
| VoxConverse           | 0.537   | 0.724    | 0.410             | 0.563              |

Expected outputs (and VBx baseline) are also provided in the `/reproducible_research` sub-directories.

## Citation

```bibtex
@inproceedings{Bredin2021,
  Title = {{End-to-end speaker segmentation for overlap-aware resegmentation}},
  Author = {{Bredin}, Herv{\'e} and {Laurent}, Antoine},
  Booktitle = {Proc. Interspeech 2021},
  Address = {Brno, Czech Republic},
  Month = {August},
  Year = {2021},
```

```bibtex
@inproceedings{Bredin2020,
  Title = {{pyannote.audio: neural building blocks for speaker diarization}},
  Author = {{Bredin}, Herv{\'e} and {Yin}, Ruiqing and {Coria}, Juan Manuel and {Gelly}, Gregory and {Korshunov}, Pavel and {Lavechin}, Marvin and {Fustes}, Diego and {Titeux}, Hadrien and {Bouaziz}, Wassim and {Gill}, Marie-Philippe},
  Booktitle = {ICASSP 2020, IEEE International Conference on Acoustics, Speech, and Signal Processing},
  Address = {Barcelona, Spain},
  Month = {May},
  Year = {2020},
}
```
