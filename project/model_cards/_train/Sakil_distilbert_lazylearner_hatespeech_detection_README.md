---
license: apache-2.0
language: en
tags:
- hate
- speech

widget:
- text: "RT @ShenikaRoberts: The shit you hear about me might be true or it might be faker than the bitch who told it to ya &#5736"

---

# Dataset Collection:
* The hatespeech dataset is collected from different open sources like Kaggle ,social media like Twitter.
* The dataset has the two classes hatespeech and non hatespeech.
* The class distribution is equal
* Different strategies have been followed during the data gathering phase.
* The dataset is collected from relevant sources.

# distilbert-base-uncased model is fine-tuned for Hate Speech Detection
* The model is fine-tuned on the dataset.
* This model can be used to create the labels for academic purposes or for industrial purposes.
* This model can be used for the inference purpose as well.

# Data Fields:
 
**label**: 0 - it is a hate speech, 1 - not a hate speech

# Application:
* This model is useful for the detection of hatespeech in the tweets.
* There are numerous situations where we have tweet data but no labels, so this approach can be used to create labels.
* You can fine-tune this model for your particular use cases.

# Model Implementation

# !pip install transformers[sentencepiece]

from transformers import pipeline

model_name="Sakil/distilbert_lazylearner_hatespeech_detection"

classifier = pipeline("text-classification",model=model_name)

classifier("!!! RT @mayasolovely: As a woman you shouldn't complain about cleaning up your house. &amp; as a man you should always take the trash out...")

# Github: [Sakil Ansari](https://github.com/Sakil786/hate_speech_detection_pretrained_model)