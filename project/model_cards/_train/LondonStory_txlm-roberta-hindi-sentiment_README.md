---
tags:
- txlm-roberta-hindi-sentiment
language: 
- hi
license: mit
---

# T-XLM-RoBERTa-Hindi-Sentiment 

`T-XLM-RoBERTa-Hindi-Sentiment` model is a fine-tuned version of the [Twitter-XLM-RoBERTa-base](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base) model from Cardiff-NLP.


## Description of the model and the training data

`txlm-roberta-hindi-sentiment` is a Hindi language sentiment classifier model (in Devanagari script) which is trained on a publicly available Hindi language dataset. See the GitHub source of the dataset [HERE](https://github.com/sid573/Hindi_Sentiment_Analysis). 

The training, testing and validation datasets consist of 6807, 1634 and 635 numbers of labelled Hindi language examples respectively. 

The trained model shows a weighted average macro F1-score of 0.89 (please see the confusion matrix in the Google Colab notebook below). 


## Code

The Google Colab notebook, where the model is fine-tuned by employing native PyTorch modules can be found on LondonStory's GitHub page [HERE](https://github.com/LondonStory/Supervised-NLP-models/blob/main/T-XLM-RoBERTa-base-finetuning-with-pytorch.ipynb). 







