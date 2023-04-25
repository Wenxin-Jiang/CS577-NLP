---
license: cc-by-sa-4.0
language: "de"
thumbnail:
tags:
- automatic-speech-recognition
- CTC
- Attention
- pytorch
- speechbrain
metrics:
- wer
---

# German ASR

This model is trained on the Mozilla Common Voice 6.1, the Spoken Wikipedia Corpus and the m-ailabs corpus.

  - https://nats.gitlab.io/swc/
  - https://commonvoice.mozilla.org/de/datasets
  - https://www.caito.de/2019/01/03/the-m-ailabs-speech-dataset/

We do not provide a language model.

You can find the training codes [here](https://github.com/rub-ksv/asr-crdnn-german).
# Performance

This model has a WER of 7.24%.
(You can find an updated version of this model here: https://huggingface.co/jfreiwa/asr-crdnn-german-umlaute)

# Model application

## Install SpeechBrain
First of all, please install SpeechBrain with the following command:
```
pip install speechbrain
```
Please notice that we encourage you to read the tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

## Using the model
```
from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="jfreiwa/asr-crdnn-german", savedir="pretrained_models/asr-crdnn-german")
asr_model.transcribe_file("jfreiwa/asr-crdnn-german/example-de.wav")

```

## Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.


# Limitations
We do not provide any warranty on the performance achieved by this model when used on other datasets.

# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/

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

# **Citing our paper**
Please, cite our paper, when you use this model in your research.
```bibtex
@inproceedings{freiwald2022,
  author={J. Freiwald and P. Pracht and S. Gergen and D. Kolossa},
  title={Open-Source End-To-End Learning for Privacy-Preserving German {ASR}},
  year=2022,
  booktitle={DAGA 2022}
}
```

# Acknowledgements
This work was funded by the German Federal Ministry of Education and Research (BMBF)
within the “Innovations for Tomorrow’s Production, Services, and
Work” Program (02L19C200), a project that is implemented by
the Project Management Agency Karlsruhe (PTKA). The authors
are responsible for the content of this publication.