---
language: 
- en

tags:
- text-classification
- fake-news
- pytorch
datasets:
- Fake News https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
metrics:
- Accuracy, AUC
---

## Model description:
[Distilbert](https://arxiv.org/abs/1910.01108) is created with knowledge distillation during the pre-training phase which reduces the size of a BERT model by 40%, while retaining 97% of its language understanding. It's smaller, faster than Bert and any other Bert-based model.

[Distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) finetuned on the fake news dataset with below Hyperparameters
```
 learning rate 5e-5, 
 batch size 32,
 num_train_epochs=2,
```
Full code available @ [DistilBert-FakeNews](https://github.com/anasserhussien/DistilBert-FakeNews)

Dataset available  @  [Fake News dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

