---
tags:
- espnet
- audio
- audio-source-separation
- audio-to-audio
language: en
datasets:
- librimix
license: cc-by-4.0
inference: false
---

# ESPnet2 ENH pretrained model

## `anogkongda/librimix_enh_train_raw_valid.si_snr.ave`

♻️ Imported from <https://zenodo.org/record/4480771#.YN70WJozZH4>
This model was trained by anogkongda using librimix recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```python
# coming soon
```

### Citing ESPnet

```BibTex
@inproceedings{watanabe2018espnet,
  author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson {Enrique Yalta Soplin} and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
  title={{ESPnet}: End-to-End Speech Processing Toolkit},
  year={2018},
  booktitle={Proceedings of Interspeech},
  pages={2207--2211},
  doi={10.21437/Interspeech.2018-1456},
  url={http://dx.doi.org/10.21437/Interspeech.2018-1456}
}
@inproceedings{hayashi2020espnet,
  title={{Espnet-TTS}: Unified, reproducible, and integratable open source end-to-end text-to-speech toolkit},
  author={Hayashi, Tomoki and Yamamoto, Ryuichi and Inoue, Katsuki and Yoshimura, Takenori and Watanabe, Shinji and Toda, Tomoki and Takeda, Kazuya and Zhang, Yu and Tan, Xu},
  booktitle={Proceedings of IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={7654--7658},
  year={2020},
  organization={IEEE}
}
```

or arXiv:

```bibtex
@misc{watanabe2018espnet,
      title={ESPnet: End-to-End Speech Processing Toolkit}, 
      author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson Enrique Yalta Soplin and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
      year={2018},
      eprint={1804.00015},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Training config

See full config in [`config.yaml`](./config.yaml)

```yaml
config: conf/tuning/train_conformer_fastspeech2.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_conformer_fastspeech2_raw_phn_jaconv_pyopenjtalk
ngpu: 1
seed: 0
num_workers: 1
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: null
dist_rank: null
local_rank: 0
dist_master_addr: null
dist_master_port: null
dist_launcher: null
multiprocessing_distributed: false
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
```
