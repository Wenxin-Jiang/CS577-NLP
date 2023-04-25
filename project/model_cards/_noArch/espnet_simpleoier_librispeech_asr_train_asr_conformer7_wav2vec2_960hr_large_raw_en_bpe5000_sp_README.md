---
tags:
- espnet
- audio
- automatic-speech-recognition
language: en
datasets:
- librispeech
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `espnet/simpleoier_librispeech_asr_train_asr_conformer7_wav2vec2_960hr_large_raw_en_bpe5000_sp`

This model was trained by simpleoier using librispeech recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout b0ff60946ada6753af79423a2e6063984bec2926
pip install -e .
cd egs2/librispeech/asr1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/simpleoier_librispeech_asr_train_asr_conformer7_wav2vec2_960hr_large_raw_en_bpe5000_sp
```



## ASR config

<details><summary>expand</summary>

```

```

</details>



### Citing ESPnet

```BibTex
@inproceedings{watanabe2018espnet,
  author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson Yalta and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
  title={{ESPnet}: End-to-End Speech Processing Toolkit},
  year={2018},
  booktitle={Proceedings of Interspeech},
  pages={2207--2211},
  doi={10.21437/Interspeech.2018-1456},
  url={http://dx.doi.org/10.21437/Interspeech.2018-1456}
}




```

or arXiv:

```bibtex
@misc{watanabe2018espnet,
  title={ESPnet: End-to-End Speech Processing Toolkit}, 
  author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson Yalta and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
  year={2018},
  eprint={1804.00015},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```
