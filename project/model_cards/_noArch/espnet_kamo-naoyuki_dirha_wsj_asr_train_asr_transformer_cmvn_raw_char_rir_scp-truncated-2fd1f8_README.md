---
tags:
- espnet
- audio
- automatic-speech-recognition
language: en
datasets:
- dirha_wsj
license: cc-by-4.0
---
## Example ESPnet2 ASR model 
### `kamo-naoyuki/dirha_wsj_asr_train_asr_transformer_cmvn_raw_char_rir_scpdatadirha_irwav.scp_noise_db_range10_17_noise_scpdatadirha_noisewav.scp_speech_volume_normalize1.0_num_workers2_rir_apply_prob1._sp_valid.acc.ave`
♻️ Imported from https://zenodo.org/record/4415021/

This model was trained by kamo-naoyuki using dirha_wsj/asr1 recipe in [espnet](https://github.com/espnet/espnet/).
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