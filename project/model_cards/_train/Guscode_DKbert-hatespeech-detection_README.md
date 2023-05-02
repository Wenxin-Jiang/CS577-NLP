---
language:

- da

tags:
- Hatespeech
- Danish
- BERT
license: mit
datasets:
- DKHate - OffensEval2020
Classes:
- Hateful
- Not Hateful
---


# DKbert-hatespeech-classification

Use this model to detect hatespeech in Danish. For details, guide and command line tool see [DK hate github](https://github.com/Guscode/DKbert-hatespeech-detection)

## Training data

Training data is from OffensEval2020 which can be found [here]( https://figshare.com/articles/dataset/Danish_Hate_Speech_Abusive_Language_data/12220805)

## Performance

The model achieves a macro F1-score of 0.78 

Precision hateful: 0.77

Recall hateful: 0.49

See more on [DK hate github](https://github.com/Guscode/DKbert-hatespeech-detection)

## Training procedure

- [BOTXO Nordic Bert](https://huggingface.co/DJSammy/bert-base-danish-uncased_BotXO,ai)
- Learning rate: 1e-5,
- Batch size: 16
- Max sequence length: 128

## Project information

This model was made in collaboration between [Johan Horsmans](https://github.com/JohanHorsmans) and [Gustav Aarup Lauridsen](https://github.com/Guscode) for their Cultural Data Science Exam.


