---
tags:
- asteroid
- audio
- FasNet-TAC
- audio-to-audio
- multichannel
- beamforming
datasets:
- TACDataset
- sep_noisy
license: cc-by-sa-4.0
---

## Asteroid model `Samuele Cornell/FasNetTAC_TACDataset_separatenoisy`
Imported from [Zenodo](https://zenodo.org/record/4557489)

### Description:
This model was trained by popcornell using the TAC/TAC recipe in Asteroid. It was trained on the separate_noisy task of the TACDataset dataset.

### Training config:
```yaml
data:
    dev_json: ./data/validation.json
    sample_rate: 16000
    segment: None
    test_json: ./data/test.json
    train_json: ./data/train.json
net:
    chunk_size: 50
    context_ms: 16
    enc_dim: 64
    feature_dim: 64
    hidden_dim: 128
    hop_size: 25
    n_layers: 4
    n_src: 2
    window_ms: 4
optim:
    lr: 0.001
    weight_decay: 1e-06
training:
    accumulate_batches: 1
    batch_size: 8
    early_stop: True
    epochs: 200
    gradient_clipping: 5
    half_lr: True
    num_workers: 8
    patience: 30
    save_top_k: 10
```

### Results:
```yaml
si_sdr: 10.871864315894744
si_sdr_imp: 11.322284052560262
```

### License notice:
This work "FasNetTAC_TACDataset_separatenoisy" is a derivative of LibriSpeech ASR corpus by Vassil Panayotov, used under CC BY 4.0; of End-to-end Microphone Permutation and Number Invariant Multi-channel Speech Separation by Yi Luo, Zhuo Chen, Nima Mesgarani, Takuya Yoshioka, used under CC BY 4.0. "FasNetTAC_TACDataset_separatenoisy" is licensed under Attribution-ShareAlike 3.0 Unported by popcornell.

