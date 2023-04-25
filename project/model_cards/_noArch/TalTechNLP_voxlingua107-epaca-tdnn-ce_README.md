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

# VoxLingua107 ECAPA-TDNN Spoken Language Identification Model (CE)

## Model description

This is a spoken language recognition model trained on the VoxLingua107 dataset using SpeechBrain.
The model uses the ECAPA-TDNN architecture that has previously been used for speaker recognition. However, it uses
more fully connected hidden layers after the embedding layer, and cross-entropy loss was used for training. 
We observed that this improved the performance of extracted utterance embeddings for downstream tasks.

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
language_id = EncoderClassifier.from_hparams(source="TalTechNLP/voxlingua107-epaca-tdnn-ce", savedir="tmp")
# Download Thai language sample from Omniglot and cvert to suitable form
signal = language_id.load_audio("https://omniglot.com/soundfiles/udhr/udhr_th.mp3")
prediction =  language_id.classify_batch(signal)
print(prediction)
  (tensor([[-2.8646e+01, -3.0346e+01, -2.0748e+01, -2.9562e+01, -2.2187e+01,
         -3.2668e+01, -3.6677e+01, -3.3573e+01, -3.2545e+01, -2.4365e+01,
         -2.4688e+01, -3.1171e+01, -2.7743e+01, -2.9918e+01, -2.4770e+01,
         -3.2250e+01, -2.4727e+01, -2.6087e+01, -2.1870e+01, -3.2821e+01,
         -2.2128e+01, -2.2822e+01, -3.0888e+01, -3.3564e+01, -2.9906e+01,
         -2.2392e+01, -2.5573e+01, -2.6443e+01, -3.2429e+01, -3.2652e+01,
         -3.0030e+01, -2.4607e+01, -2.2967e+01, -2.4396e+01, -2.8578e+01,
         -2.5153e+01, -2.8475e+01, -2.6409e+01, -2.5230e+01, -2.7957e+01,
         -2.6298e+01, -2.3609e+01, -2.5863e+01, -2.8225e+01, -2.7225e+01,
         -3.0486e+01, -2.1185e+01, -2.7938e+01, -3.3155e+01, -1.9076e+01,
         -2.9181e+01, -2.2160e+01, -1.8352e+01, -2.5866e+01, -3.3636e+01,
         -4.2016e+00, -3.1581e+01, -3.1894e+01, -2.7834e+01, -2.5429e+01,
         -3.2235e+01, -3.2280e+01, -2.8786e+01, -2.3366e+01, -2.6047e+01,
         -2.2075e+01, -2.3770e+01, -2.2518e+01, -2.8101e+01, -2.5745e+01,
         -2.6441e+01, -2.9822e+01, -2.7109e+01, -3.0225e+01, -2.4566e+01,
         -2.9268e+01, -2.7651e+01, -3.4221e+01, -2.9026e+01, -2.6009e+01,
         -3.1968e+01, -3.1747e+01, -2.8156e+01, -2.9025e+01, -2.7756e+01,
         -2.8052e+01, -2.9341e+01, -2.8806e+01, -2.1636e+01, -2.3992e+01,
         -2.3794e+01, -3.3743e+01, -2.8332e+01, -2.7465e+01, -1.5085e-02,
         -2.9094e+01, -2.1444e+01, -2.9780e+01, -3.6046e+01, -3.7401e+01,
         -3.0888e+01, -3.3172e+01, -1.8931e+01, -2.2679e+01, -3.0225e+01,
         -2.4995e+01, -2.1028e+01]]), tensor([-0.0151]), tensor([94]), ['th'])
# The scores in the prediction[0] tensor can be interpreted as log-likelihoods that
# the given utterance belongs to the given language (i.e., the larger the better)
# The linear-scale likelihood can be retrieved using the following:
print(prediction[1].exp())
  tensor([0.9850])
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

Error rate: 6.7% on the VoxLingua107 development dataset


### BibTeX entry and citation info

```bibtex
@inproceedings{valk2021slt,
  title={{VoxLingua107}: a Dataset for Spoken Language Recognition},
  author={J{\"o}rgen Valk and Tanel Alum{\"a}e},
  booktitle={Proc. IEEE SLT Workshop},
  year={2021},
}
```
