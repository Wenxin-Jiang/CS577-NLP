---
license: apache-2.0
language: "en"
thumbnail:
tags:
- G2P
- Grapheme-to-Phoneme
- speechbrain
- text2text-generation
datasets:
- Librispeech
metrics:
- Phone-Error-Rate
widget:
- text: "English is tough. It can be understood through thorough thought though."
---
# SoundChoice: Grapheme-to-Phoneme Models with Semantic Disambiguation

This repository provides all the necessary tools to perform English grapheme-to-phoneme conversion with a pretrained SoundChoice G2P model using SpeechBrain. It is trained on LibriG2P training data derived from [LibriSpeech Alignments](https://zenodo.org/record/2619474#.YuCdaC8r1ZF) and [Google Wikipedia](https://github.com/google/WikipediaHomographData)


## Install SpeechBrain

First of all, please install SpeechBrain with the following command (local installation):

```bash
pip install speechbrain
pip install transformers
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

## Perform G2P Conversion

Please follow the example below to perform grapheme-to-phoneme conversion with a high-level wrapper.

```python
from speechbrain.pretrained import GraphemeToPhoneme
g2p = GraphemeToPhoneme.from_hparams("speechbrain/soundchoice-g2p")
text = "To be or not to be, that is the question"
phonemes = g2p(text)
```

Given below is the expected output
```python
>>> phonemes
['T', 'UW', ' ', 'B', 'IY', ' ', 'AO', 'R', ' ', 'N', 'AA', 'T', ' ', 'T', 'UW', ' ', 'B', 'IY', ' ', 'DH', 'AE', 'T', ' ', 'IH', 'Z', ' ', 'DH', 'AH', ' ', 'K', 'W', 'EH', 'S', 'CH', 'AH', 'N']
```

To perform G2P conversion on a batch of text, pass
an array of strings to the interface:

```python
items = [
    "All's Well That Ends Well",
    "The Merchant of Venice",
    "The Two Gentlemen of Verona",
    "The Comedy of Errors"
]
transcriptions = g2p(items)
```

Given below is the expected output:

```python
>>> transcriptions
[['AO', 'L', 'Z', ' ', 'W', 'EH', 'L', ' ', 'DH', 'AE', 'T', ' ', 'EH', 'N', 'D', 'Z', ' ', 'W', 'EH', 'L'], ['DH', 'AH', ' ', 'M', 'ER', 'CH', 'AH', 'N', 'T', ' ', 'AH', 'V', ' ', 'V', 'EH', 'N', 'AH', 'S'], ['DH', 'AH', ' ', 'T', 'UW', ' ', 'JH', 'EH', 'N', 'T', 'AH', 'L', 'M', 'IH', 'N', ' ', 'AH', 'V', ' ', 'V', 'ER', 'OW', 'N', 'AH'], ['DH', 'AH', ' ', 'K', 'AA', 'M', 'AH', 'D', 'IY', ' ', 'AH', 'V', ' ', 'EH', 'R', 'ER', 'Z']]
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

### Training
The model was trained with SpeechBrain (aa018540).
To train it from scratch follows these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```
cd speechbrain
pip install -r requirements.txt
pip install -e .
```

3. Run Training:
```
cd recipes/LibriSpeech/G2P
python train.py hparams/hparams_g2p_rnn.yaml --data_folder=your_data_folder
```

Adjust hyperparameters as needed by passing additional arguments.

# **Citing SpeechBrain**
Please, cite SpeechBrain if you use it for your research or business.

```bibtex
@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}
```

Also please cite the SoundChoice G2P paper on which this pretrained model is based:

```bibtex
@misc{ploujnikov2022soundchoice,
      title={SoundChoice: Grapheme-to-Phoneme Models with Semantic Disambiguation}, 
      author={Artem Ploujnikov and Mirco Ravanelli},
      year={2022},
      eprint={2207.13703},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}
```

# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/