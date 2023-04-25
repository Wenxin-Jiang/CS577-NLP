---
tags: 
- pyannote
- pyannote-audio
- pyannote-audio-pipeline
- audio
- voice
- speech
- speaker
- speaker-diarization
- speaker-change-detection
- voice-activity-detection
- overlapped-speech-detection
datasets:
- ami
- dihard
- voxconverse
- aishell
- repere
- voxceleb
license: mit
---

# 🎹 Speaker diarization

Relies on pyannote.audio 2.0: see [installation instructions](https://github.com/pyannote/pyannote-audio/tree/develop#installation).


## TL;DR

```python
# load the pipeline from Hugginface Hub
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2022.07")

# apply the pipeline to an audio file
diarization = pipeline("audio.wav")

# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)
```

## Advanced usage

In case the number of speakers is known in advance, one can use the `num_speakers` option:

```python
diarization = pipeline("audio.wav", num_speakers=2)
```

One can also provide lower and/or upper bounds on the number of speakers using `min_speakers` and `max_speakers` options:

```python
diarization = pipeline("audio.wav", min_speakers=2, max_speakers=5)
```

If you feel adventurous, you can try and play with the various pipeline hyper-parameters.  
For instance, one can use a more aggressive voice activity detection by increasing the value of `segmentation_onset` threshold:

```python
hparams = pipeline.parameters(instantiated=True)
hparams["segmentation_onset"] += 0.1
pipeline.instantiate(hparams)
```

## Benchmark 

### Real-time factor

Real-time factor is around 5% using one Nvidia Tesla V100 SXM2 GPU (for the neural inference part) and one Intel Cascade Lake 6248 CPU (for the clustering part).

In other words, it takes approximately 3 minutes to process a one hour conversation.

### Accuracy

This pipeline is benchmarked on a growing collection of datasets.  

Processing is fully automatic:

* no manual voice activity detection (as is sometimes the case in the literature)
* no manual number of speakers (though it is possible to provide it to the pipeline)
* no fine-tuning of the internal models nor tuning of the pipeline hyper-parameters to each dataset

... with the least forgiving diarization error rate (DER) setup (named *"Full"* in [this paper](https://doi.org/10.1016/j.csl.2021.101254)):

* no forgiveness collar
* evaluation of overlapped speech


| Benchmark                                                                                                                          | [DER%](. "Diarization error rate") | [FA%](. "False alarm rate") | [Miss%](. "Missed detection rate") | [Conf%](. "Speaker confusion rate") | Expected output                                                                            | File-level evaluation                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | --------------------------- | ---------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| [AISHELL-4](http://www.openslr.org/111/)                                                                                           | 14.61                              | 3.31                        | 4.35                               | 6.95                                | [RTTM](reproducible_research/AISHELL.SpeakerDiarization.Full.test.rttm)                    | [eval](reproducible_research/AISHELL.SpeakerDiarization.Full.test.eval)                    |
| [AMI *Mix-Headset*](https://groups.inf.ed.ac.uk/ami/corpus/) [*only_words*](https://github.com/BUTSpeechFIT/AMI-diarization-setup) | 18.21                              | 3.28                        | 11.07                              | 3.87                                | [RTTM](reproducible_research/2022.07/AMI.SpeakerDiarization.only_words.test.rttm)          | [eval](reproducible_research/2022.07/AMI.SpeakerDiarization.only_words.test.eval)          |
| [AMI *Array1-01*](https://groups.inf.ed.ac.uk/ami/corpus/) [*only_words*](https://github.com/BUTSpeechFIT/AMI-diarization-setup)   | 29.00                              | 2.71                        | 21.61                              | 4.68                                | [RTTM](reproducible_research/2022.07/AMI-SDM.SpeakerDiarization.only_words.test.rttm)      | [eval](reproducible_research/2022.07/AMI-SDM.SpeakerDiarization.only_words.test.eval)      |
| [CALLHOME](https://catalog.ldc.upenn.edu/LDC2001S97) [*Part2*](https://github.com/BUTSpeechFIT/CALLHOME_sublists/issues/1)         | 30.24                              | 3.71                        | 16.86                              | 9.66                                | [RTTM](reproducible_research/2022.07/CALLHOME.SpeakerDiarization.CALLHOME.test.rttm)       | [eval](reproducible_research/2022.07/CALLHOME.SpeakerDiarization.CALLHOME.test.eval)       |
| [DIHARD 3 *Full*](https://arxiv.org/abs/2012.01477)                                                                                | 20.99                              | 4.25                        | 10.74                              | 6.00                                | [RTTM](reproducible_research/2022.07/DIHARD.SpeakerDiarization.Full.test.rttm)             | [eval](reproducible_research/2022.07/DIHARD.SpeakerDiarization.Full.test.eval)             |
| [REPERE *Phase 2*](https://islrn.org/resources/360-758-359-485-0/)                                                                 | 12.62                              | 1.55                        | 3.30                               | 7.76                                | [RTTM](reproducible_research/2022.07/REPERE.SpeakerDiarization.Full.test.rttm)             | [eval](reproducible_research/2022.07/REPERE.SpeakerDiarization.Full.test.eval)             |
| [VoxConverse *v0.0.2*](https://github.com/joonson/voxconverse)                                                                     | 12.76                              | 3.45                        | 3.85                               | 5.46                                | [RTTM](reproducible_research/2022.07/VoxConverse.SpeakerDiarization.VoxConverse.test.rttm) | [eval](reproducible_research/2022.07/VoxConverse.SpeakerDiarization.VoxConverse.test.eval) |


## Support

For commercial enquiries and scientific consulting, please contact [me](mailto:herve@niderb.fr).  
For [technical questions](https://github.com/pyannote/pyannote-audio/discussions) and [bug reports](https://github.com/pyannote/pyannote-audio/issues), please check [pyannote.audio](https://github.com/pyannote/pyannote-audio) Github repository.


## Citations

```bibtex
@inproceedings{Bredin2021,
  Title = {{End-to-end speaker segmentation for overlap-aware resegmentation}},
  Author = {{Bredin}, Herv{\'e} and {Laurent}, Antoine},
  Booktitle = {Proc. Interspeech 2021},
  Address = {Brno, Czech Republic},
  Month = {August},
  Year = {2021},
}
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
