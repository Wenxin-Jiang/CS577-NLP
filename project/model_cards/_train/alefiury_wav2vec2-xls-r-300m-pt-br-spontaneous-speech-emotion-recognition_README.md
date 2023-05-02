---
language: pt
datasets:
- coraa_ser
- emovo
- ravdess
- baved
metrics:
- f1
tags:
- audio
- speech
- wav2vec2
- pt
- portuguese-speech-corpus
- italian-speech-corpus
- english-speech-corpus
- arabic-speech-corpus
- spontaneous
- speech
- PyTorch
license: apache-2.0
model_index:
  name: wav2vec2-xls-r-300m-pt-br-spontaneous-speech-emotion-recognition
results:
    metrics:
       - name: Test Macro F1-Score
         type: f1
         value: 81.87%
---

# Wav2vec 2.0 XLS-R For Spontaneous Speech Emotion Recognition

This is the model that got first place in the SER track of the Automatic Speech Recognition for spontaneous and prepared speech & Speech Emotion Recognition in Portuguese (SE&R 2022) Workshop.

The following datasets were used in the training:

- [CORAA SER v1.0](https://github.com/rmarcacini/ser-coraa-pt-br/): a dataset composed of spontaneous portuguese speech and approximately 40 minutes of audio segments labeled in three classes: neutral, non-neutral female, and non-neutral male.

- [EMOVO Corpus](https://aclanthology.org/L14-1478/): a database of emotional speech for the Italian language, built from the voices of up to 6 actors who played 14 sentences simulating 6 emotional states (disgust, fear, anger, joy, surprise, sadness) plus the neutral state.

- [RAVDESS](https://zenodo.org/record/1188976#.YO6yI-gzaUk): a dataset that provides 1440 samples of recordings from actors performing on 8 different emotions in English, which are: angry, calm, disgust, fearful, happy, neutral, sad and surprised.

- [BAVED](https://github.com/40uf411/Basic-Arabic-Vocal-Emotions-Dataset): a collection of audio recordings of Arabic words spoken with varying degrees of emotion. The dataset contains seven words: like, unlike, this, file, good, neutral, and bad, which are spoken at three emotional levels: low emotion (tired or feeling down), neutral emotion (the way the speaker speaks daily), and high emotion (positive or negative emotions such as happiness, joy, sadness, anger).

The test set used is a part of the CORAA SER v1.0 that has been set aside for this purpose.

It achieves the following results on the test set:
- Accuracy: 0.9090
- Macro Precision: 0.8171
- Macro Recall: 0.8397
- Macro F1-Score: 0.8187

## Datasets Details

The following image shows the overall distribution of the datasets:

![distribution](https://docs.google.com/spreadsheets/d/e/2PACX-1vTUvuMLRnoFv3MBkStOcMQE5GuiqqyrvpyEtIiwoQEg8uA6dWvfZM-faHORLFNmPYJUzDbO6TZ2a9Zb/pubchart?oid=446282973&format=image)

The following image shows the number of instances by label:

![numberInstances](https://docs.google.com/spreadsheets/d/e/2PACX-1vS7PUbW6J3Hnof1D2l492KW0sbF4BzWCeaiGQm53w-9EZck_Y14feE48HtcBvmjjZKsTJWP1RZpdh_v/pubchart?oid=1904097403&format=image)


## Repository

The repository that implements the model to be trained and tested is avaible [here](https://github.com/alefiury/SE-R-2022-SER-Track).