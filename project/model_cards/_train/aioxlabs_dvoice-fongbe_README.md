---
language: "fon"
thumbnail:
pipeline_tag: automatic-speech-recognition
tags:
- CTC
- pytorch
- speechbrain
- Transformer
license: "apache-2.0"
datasets:
- commonvoice
metrics:
- wer
- cer
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# wav2vec 2.0 with CTC/Attention trained on DVoice Fongbe (No LM)
This repository provides all the necessary tools to perform automatic speech
recognition from an end-to-end system pretrained on a [ALFFA](https://github.com/besacier/ALFFA_PUBLIC) Fongbe dataset within
SpeechBrain. For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io).

| DVoice Release | Val. CER | Val. WER | Test CER | Test WER |
|:-------------:|:---------------------------:| -----:| -----:| -----:|
| v2.0 | 4.16 | 9.19 | 3.98 | 9.00 |

# Pipeline description
This ASR system is composed of 2 different but linked blocks:
- Tokenizer (unigram) that transforms words into subword units and trained with
the train transcriptions.
- Acoustic model (wav2vec2.0 + CTC). A pretrained wav2vec 2.0 model ([facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53)) is combined with two DNN layers and finetuned on the Darija dataset.
The obtained final acoustic representation is given to the CTC greedy decoder.
The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

# Install SpeechBrain
First of all, please install tranformers and SpeechBrain with the following command:
```
pip install speechbrain transformers
```
Please notice that we encourage you to read the SpeechBrain tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

# Transcribing your own audio files (in Fongbe)
```python
from speechbrain.pretrained import EncoderASR
asr_model = EncoderASR.from_hparams(source="aioxlabs/dvoice-fongbe", savedir="pretrained_models/asr-wav2vec2-dvoice-fon")
asr_model.transcribe_file('./the_path_to_your_audio_file')
```

# Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

# Training
To train the model from scratch, please see our GitHub tutorial [here](https://github.com/AIOXLABS/DVoice).

# Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

# About DVoice
DVoice is a community initiative that aims to provide Africa low resources languages with data and models to facilitate their use of voice technologies. The lack of data on these languages makes it necessary to collect data using methods that are specific to each one. Two different approaches are currently used: the DVoice platforms ([https://dvoice.ma](https://dvoice.ma) and [https://dvoice.sn](https://dvoice.sn)), which are based on Mozilla Common Voice, for collecting authentic recordings from the community, and transfer learning techniques for automatically labeling recordings that are retrived from social medias. The DVoice platform currently manages 7 languages including Darija (Moroccan Arabic dialect) whose dataset appears on this version, Wolof, Mandingo, Serere, Pular, Diola and Soninke.

For this project, AIOX Labs the SI2M Laboratory are joining forces to build the future of technologies together.

# About AIOX Labs
Based in Rabat, London and Paris, AIOX-Labs mobilizes artificial intelligence technologies to meet the business needs and data projects of companies.

- He is at the service of the growth of groups, the optimization of processes or the improvement of the customer experience.
- AIOX-Labs is multi-sector, from fintech to industry, including retail and consumer goods.
- Business ready data products with a solid algorithmic base and adaptability for the specific needs of each client.
- A complementary team made up of doctors in AI and business experts with a solid scientific base and international publications.

Website: [https://www.aiox-labs.com/](https://www.aiox-labs.com/)

# SI2M Laboratory
The Information Systems, Intelligent Systems and Mathematical Modeling Research Laboratory (SI2M) is an academic research laboratory of the National Institute of Statistics and Applied Economics (INSEA). The research areas of the laboratories are Information Systems, Intelligent Systems, Artificial Intelligence, Decision Support, Network and System Security, Mathematical Modelling.

Website: [SI2M Laboratory](https://insea.ac.ma/index.php/pole-recherche/equipe-de-recherche/150-laboratoire-de-recherche-en-systemes-d-information-systemes-intelligents-et-modelisation-mathematique)

# About SpeechBrain
SpeechBrain is an open-source and all-in-one speech toolkit. It is designed to be simple, extremely flexible, and user-friendly. Competitive or state-of-the-art performance is obtained in various domains.
Website: https://speechbrain.github.io/
GitHub: https://github.com/speechbrain/speechbrain


# Referencing SpeechBrain
```
@misc{SB2021,
    author = {Ravanelli, Mirco and Parcollet, Titouan and Rouhe, Aku and Plantinga, Peter and Rastorgueva, Elena and Lugosch, Loren and Dawalatabad, Nauman and Ju-Chieh, Chou and Heba, Abdel and Grondin, Francois and Aris, William and Liao, Chien-Feng and Cornell, Samuele and Yeh, Sung-Lin and Na, Hwidong and Gao, Yan and Fu, Szu-Wei and Subakan, Cem and De Mori, Renato and Bengio, Yoshua },
    title = {SpeechBrain},
    year = {2021},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\\\\url{https://github.com/speechbrain/speechbrain}},
  }
```
# Acknowledgements
This research was supported through computational resources of HPC-MARWAN (www.marwan.ma/hpc) provided by CNRST, Rabat, Morocco. We deeply thank this institution.