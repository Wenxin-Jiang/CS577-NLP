---
language: multilingual
thumbnail:
tags:
- audio-classification
- speechbrain
- embeddings
- Language
- Identification
- pytorch
- ECAPA-TDNN
- TDNN
- VoxLingua107
license: "apache-2.0"
datasets:
- VoxLingua107
metrics:
- Accuracy
widget:
- example_title: English Sample
  src: https://cdn-media.huggingface.co/speech_samples/LibriSpeech_61-70968-0000.flac
---

# VoxLingua107 ECAPA-TDNN Spoken Language Identification Model

## Model description

This is a spoken language recognition model trained on the VoxLingua107 dataset using SpeechBrain.
The model uses the ECAPA-TDNN architecture that has previously been used for speaker recognition.

The model can classify a speech utterance according to the language spoken.
It covers 107 different languages (
Abkhazian, 
Afrikaans, 
Amharic, 
Arabic, 
Assamese, 
Azerbaijani, 
Bashkir, 
Belarusian, 
Bulgarian, 
Bengali, 
Tibetan, 
Breton, 
Bosnian, 
Catalan, 
Cebuano, 
Czech, 
Welsh, 
Danish, 
German, 
Greek, 
English, 
Esperanto, 
Spanish, 
Estonian, 
Basque, 
Persian, 
Finnish, 
Faroese, 
French, 
Galician, 
Guarani, 
Gujarati, 
Manx, 
Hausa, 
Hawaiian, 
Hindi, 
Croatian, 
Haitian, 
Hungarian, 
Armenian, 
Interlingua, 
Indonesian, 
Icelandic, 
Italian, 
Hebrew, 
Japanese, 
Javanese, 
Georgian, 
Kazakh, 
Central Khmer, 
Kannada, 
Korean, 
Latin, 
Luxembourgish, 
Lingala, 
Lao, 
Lithuanian, 
Latvian, 
Malagasy, 
Maori, 
Macedonian, 
Malayalam, 
Mongolian, 
Marathi, 
Malay, 
Maltese, 
Burmese, 
Nepali, 
Dutch, 
Norwegian Nynorsk, 
Norwegian, 
Occitan, 
Panjabi, 
Polish, 
Pushto, 
Portuguese, 
Romanian, 
Russian, 
Sanskrit, 
Scots, 
Sindhi, 
Sinhala, 
Slovak, 
Slovenian, 
Shona, 
Somali, 
Albanian, 
Serbian, 
Sundanese, 
Swedish, 
Swahili, 
Tamil, 
Telugu, 
Tajik, 
Thai, 
Turkmen, 
Tagalog, 
Turkish, 
Tatar, 
Ukrainian, 
Urdu, 
Uzbek, 
Vietnamese, 
Waray, 
Yiddish, 
Yoruba, 
Mandarin Chinese).

## Intended uses & limitations

The model has two uses:

  - use 'as is' for spoken language recognition
  - use as an utterance-level feature (embedding) extractor, for creating a dedicated language ID model on your own data
  
The model is trained on automatically collected YouTube data. For more 
information about the dataset, see [here](http://bark.phon.ioc.ee/voxlingua107/).


#### How to use

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
language_id = EncoderClassifier.from_hparams(source="TalTechNLP/voxlingua107-epaca-tdnn", savedir="tmp")
# Download Thai language sample from Omniglot and cvert to suitable form
signal = language_id.load_audio("https://omniglot.com/soundfiles/udhr/udhr_th.mp3")
prediction =  language_id.classify_batch(signal)
print(prediction)
  (tensor([[0.3210, 0.3751, 0.3680, 0.3939, 0.4026, 0.3644, 0.3689, 0.3597, 0.3508,
           0.3666, 0.3895, 0.3978, 0.3848, 0.3957, 0.3949, 0.3586, 0.4360, 0.3997,
           0.4106, 0.3886, 0.4177, 0.3870, 0.3764, 0.3763, 0.3672, 0.4000, 0.4256,
           0.4091, 0.3563, 0.3695, 0.3320, 0.3838, 0.3850, 0.3867, 0.3878, 0.3944,
           0.3924, 0.4063, 0.3803, 0.3830, 0.2996, 0.4187, 0.3976, 0.3651, 0.3950,
           0.3744, 0.4295, 0.3807, 0.3613, 0.4710, 0.3530, 0.4156, 0.3651, 0.3777,
           0.3813, 0.6063, 0.3708, 0.3886, 0.3766, 0.4023, 0.3785, 0.3612, 0.4193,
           0.3720, 0.4406, 0.3243, 0.3866, 0.3866, 0.4104, 0.4294, 0.4175, 0.3364,
           0.3595, 0.3443, 0.3565, 0.3776, 0.3985, 0.3778, 0.2382, 0.4115, 0.4017,
           0.4070, 0.3266, 0.3648, 0.3888, 0.3907, 0.3755, 0.3631, 0.4460, 0.3464,
           0.3898, 0.3661, 0.3883, 0.3772, 0.9289, 0.3687, 0.4298, 0.4211, 0.3838,
           0.3521, 0.3515, 0.3465, 0.4772, 0.4043, 0.3844, 0.3973, 0.4343]]), tensor([0.9289]), tensor([94]), ['th'])
# The scores in the prediction[0] tensor can be interpreted as cosine scores between
# the languages and the given utterance (i.e., the larger the better)
# The identified language ISO code is given in prediction[3]
print(prediction[3])
  ['th']
  
# Alternatively, use the utterance embedding extractor:
emb =  language_id.encode_batch(signal)
print(emb.shape)
  torch.Size([1, 1, 256])
```

#### Limitations and bias

Since the model is trained on VoxLingua107, it has many limitations and biases, some of which are:

 - Probably it's accuracy on smaller languages  is quite limited
 - Probably it works worse on female speech than male speech (because YouTube data includes much more male speech)
 - Based on subjective experiments, it doesn't work well on speech with a foreign accent
 - Probably it doesn't work well on children's speech and on persons with speech disorders


## Training data

The model is trained on [VoxLingua107](http://bark.phon.ioc.ee/voxlingua107/).

VoxLingua107 is a speech dataset for training spoken language identification models. 
The dataset consists of short speech segments automatically extracted from YouTube videos and labeled according the language of the video title and description, with some post-processing steps to filter out false positives.

VoxLingua107 contains data for 107 languages. The total amount of speech in the training set is 6628 hours. 
The average amount of data per language is 62 hours. However, the real amount per language varies a lot. There is also a seperate development set containing 1609 speech segments from 33 languages, validated by at least two volunteers to really contain the given language.

## Training procedure

We used [SpeechBrain](https://github.com/speechbrain/speechbrain) to train the model.
Training recipe will be published soon.

## Evaluation results

Error rate: 7% on the development dataset


### BibTeX entry and citation info

```bibtex
@inproceedings{valk2021slt,
  title={{VoxLingua107}: a Dataset for Spoken Language Recognition},
  author={J{\"o}rgen Valk and Tanel Alum{\"a}e},
  booktitle={Proc. IEEE SLT Workshop},
  year={2021},
}
```
