---
tags:
- espnet
- audio
- audio-to-audio
- vocoder
language: 
- multilingual
datasets:
- libritts
- csj
- css10
- aishell3
- jvs
- jsss
- jsut
license: cc-by-4.0
inference: false
---

## Vocoder model - FastDiff

**No support given.**

### Details

```
num_iters_per_epoch: 250
max_epoch: 1000
batch_size: 64
vocoder_conf:
    audio_channels: 1
    inner_channels: 32
    cond_channels: 80
    upsample_ratios:
    - 5
    - 5
    - 4
    - 3
```
