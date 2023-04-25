---
license: mit
language:
- ja
tags:
- music
- audio
- audio-to-audio
- SFI
datasets:
- MUSDB18-HQ
metrics:
- SDR
---

# Sampling-frequency-independent (SFI) Conv-TasNet trained with the MUSDB18-HQ dataset for music source separation
This model was proposed in [our IEEE/ACM Trans. ASLP paper](https://doi.org/10.1109/TASLP.2022.3203907) and works well with untrained sampling frequencies by using sampling-frequency-independent convolutional layers with the time domain filter design.
The latent analog filter is a multiphase gammatone filter.
It was trained by Tomohiko Nakamura using [the codebase](https://github.com/TomohikoNakamura/sfi_convtasnet)).
This model was trained with 32 kHz-sampled data but works well with untrained sampling frequencies (e.g., 8, 16 kHz).

# License
MIT

# Citation
Please cite the following paper.
```
@article{KSaito2022IEEEACMTASLP,
 author={Saito, Koichi and Nakamura, Tomohiko and Yatabe, Kohei and Saruwatari, Hiroshi},
 journal = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
 title = {Sampling-frequency-independent convolutional layer and its application to audio source separation},
 year=2022,
 month=sep,
 volume=30,
 pages={2928--2943},
 doi={10.1109/TASLP.2022.3203907},
}
```

# Contents
- Four trained models (seed=40,42,44,47)
- Evaluation results (json files obtained with the museval library)
