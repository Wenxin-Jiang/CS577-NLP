---
language: en
tags:
- text-classification
- pytorch
- roberta
- emotions
- multi-class-classification
- multi-label-classification
datasets:
- go_emotions
license: mit
widget:
- text: "I am not having a great day."
---

Model trained from [roberta-base](https://huggingface.co/roberta-base) on the [go_emotions](https://huggingface.co/datasets/go_emotions) dataset for multi-label classification.

[go_emotions](https://huggingface.co/datasets/go_emotions) is based on Reddit data and has 28 labels. It is a multi-label dataset where one or multiple labels may apply for any given input text, hence this model is a multi-label classification model with 28 'probability' float outputs for any given input text. Typically a threshold of 0.5 is applied to the probabilities for the prediction for each label.

The model was trained using `AutoModelForSequenceClassification.from_pretrained` with `problem_type="multi_label_classification"` for 3 epochs with a learning rate of 2e-5 and weight decay of 0.01.

Evaluation (of the 28 dim output via a threshold of 0.5 to binarize each) using the dataset test split gives:
- Micro F1 0.585
- ROC AUC 0.751
- Accuracy 0.474

But the metrics would be more meaningful when measured per label given the multi-label nature.

Additionally some labels (E.g. `gratitude`) when considered independently perform very strongly with F1 around 0.9, whilst others (E.g. `relief`) perform very poorly. This is a challenging dataset. Labels such as `relief` do have much fewer examples in the training data (less than 100 out of the 40k+), but there is also some ambiguity and/or labelling errors visible in the training data of `go_emotions` that is suspected to constrain the performance.