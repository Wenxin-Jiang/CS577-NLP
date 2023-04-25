---
tags:
- espnet
- audio
- text-to-speech
language: zh
datasets:
- csmsc
license: cc-by-4.0
---
## Example ESPnet2 TTS model 
### `kan-bayashi/csmsc_tts_train_tacotron2_raw_phn_pypinyin_g2p_phone_train.loss.best`
♻️ Imported from https://zenodo.org/record/3969118/

This model was trained by kan-bayashi using csmsc/tts1 recipe in [espnet](https://github.com/espnet/espnet/).
### Demo: How to use in ESPnet2
You first need to import the following packages
```bash
pip install torch
pip install espnet_model_zoo
```
Then start using it!
```python
import soundfile
from espnet2.bin.tts_inference import Text2Speech
text2speech = Text2Speech.from_pretrained("espnet/kan-bayashi_csmsc_tts_train_tacotron2_raw_phn_pypinyin_g2p_phone_train.loss.best")

text = "春江潮水连海平，海上明月共潮生"
speech = text2speech(text)["wav"]
soundfile.write("out.wav", speech.numpy(), text2speech.fs, "PCM_16")
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