---
language: multilingual
license: cc-by-4.0
tags:
- language-identification
- speechbrain
- wav2vec2
- pytorch
- embeddings
- Language
- Identification
- audio-classification
- wav2vec2.0
- XLS-R-300M
- VoxLingua107
datasets:
- voxlingua107
metrics:
- Accuracy
---

# VoxLingua107 Wav2Vec Spoken Language Identification Model
## Model description
This is a spoken language identification model trained on the VoxLingua107 dataset using SpeechBrain.

The model is trained using weights of pretrained [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) model, Wav2Vec2.0 architecture and negative log likelihood loss.

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
from speechbrain.pretrained.interfaces import foreign_class


language_id = foreign_class(source="TalTechNLP/voxlingua107-xls-r-300m-wav2vec", pymodule_file="encoder_wav2vec_classifier.py", classname="EncoderWav2vecClassifier", hparams_file='inference_wav2vec.yaml', savedir="tmp")

# Download Thai language sample from Omniglot and convert to suitable form
wav_file = "https://omniglot.com/soundfiles/udhr/udhr_th.mp3"
out_prob, score, index, text_lab = language_id.classify_file(wav_file)

print("probability:", out_prob)
print("label:", text_lab)
print("score:", score)
print("index:", index)
    probability: tensor([[[-2.2849e+01, -2.4349e+01, -2.3686e+01, -2.3632e+01, -2.0218e+01,
            -2.7241e+01, -2.6715e+01, -2.2301e+01, -2.6076e+01, -2.1716e+01,
            -1.9923e+01, -2.7303e+01, -2.1211e+01, -2.2998e+01, -2.4436e+01,
            -2.6437e+01, -2.2686e+01, -2.4244e+01, -2.0416e+01, -2.8329e+01,
            -1.7788e+01, -2.4829e+01, -2.4186e+01, -2.7036e+01, -2.5993e+01,
            -1.9677e+01, -2.2746e+01, -2.9192e+01, -2.4941e+01, -2.7135e+01,
            -2.6653e+01, -2.2791e+01, -2.4599e+01, -2.1066e+01, -2.4855e+01,
            -2.1874e+01, -2.2914e+01, -2.4174e+01, -2.0902e+01, -2.3197e+01,
            -2.6108e+01, -2.3941e+01, -2.3103e+01, -2.2363e+01, -2.8969e+01,
            -2.5302e+01, -2.4862e+01, -2.2392e+01, -2.4042e+01, -2.1221e+01,
            -2.3656e+01, -2.1286e+01, -1.9209e+01, -2.3254e+01, -2.8291e+01,
            -5.9105e+00, -2.4525e+01, -2.4937e+01, -2.8349e+01, -2.4420e+01,
            -2.7439e+01, -2.6329e+01, -2.3317e+01, -2.3842e+01, -2.2114e+01,
            -2.3637e+01, -1.7217e+01, -1.8342e+01, -2.4332e+01, -2.6090e+01,
            -2.5452e+01, -2.3854e+01, -2.6082e+01, -2.4992e+01, -2.0618e+01,
            -2.9351e+01, -2.4153e+01, -2.3156e+01, -2.6893e+01, -2.5314e+01,
            -2.8374e+01, -2.4009e+01, -2.3604e+01, -2.4063e+01, -2.3538e+01,
            -2.4953e+01, -2.5607e+01, -2.3960e+01, -2.6471e+01, -2.3348e+01,
            -2.1681e+01, -2.7610e+01, -2.5023e+01, -2.3585e+01, -2.7146e-03,
            -2.0338e+01, -1.8737e+01, -2.5158e+01, -2.7491e+01, -2.3623e+01,
            -2.5718e+01, -2.3465e+01, -1.8305e+01, -2.1064e+01, -2.9880e+01,
            -2.2809e+01, -1.9856e+01]]])
    # The identified language ISO code is given in score[0][0]
    label: [['th']]
    score: tensor([[-0.0027]])
    index: tensor([[94]])

# The scores in the out_prob tensor can be interpreted as log-likelihoods that
# the given utterance belongs to the given language (i.e., the larger the better)
# The linear-scale likelihood can be retrieved using the following:

print(score.exp())
  tensor([0.9973])
  
# Alternatively, use the utterance embedding extractor:
signal, fs = torchaudio.load(wav_file)
embeddings =  language_id.encode_batch(signal)
print(embeddings.shape)
    torch.Size([2, 1, 2048])
```
#### Limitations and bias
Since the model is trained on VoxLingua107, it has many limitations and biases, some of which are:

 - Probably it's accuracy on smaller languages is quite limited
 - Probably it works worse on female speech than male speech (because YouTube data includes much more male speech)
 - Based on experiments, it performs satisfactory on accented speech
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

| Version               | Error Rate (%) |
|-----------------------|:------:|
| 2022-04-14     |   5.6  |

Error rate is calculated on VoxLingua107 development dataset.


### BibTeX entry and citation info

```bibtex
@inproceedings{valk2021slt,
  title={{VoxLingua107}: a Dataset for Spoken Language Recognition},
  author={J{\"o}rgen Valk and Tanel Alum{\"a}e},
  booktitle={Proc. IEEE SLT Workshop},
  year={2021},
}
```