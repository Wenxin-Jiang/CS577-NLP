# HateSpeechDetection
---
pipeline_tag: text-classification
---

The model is used for classifying a text as Hatespeech or Normal. The model is trained using data from Twitter, specifically Kenyan related tweets. To maximize on the limited dataset, text augmentation was done.

The dataset is available here: https://github.com/sgich/HateSpeechDetection

Using a pre-trained "bert-base-uncased" transformer model, adding a dropout layer, a linear output layer and adding 10 common emojis that may be related to either Hate or Normal Speech. Then the model was tuned on a dataset of Kenyan/Kenyan-related scraped tweets with the purpose of performing text classification of "Normal Speech" or "Hate Speech" based on the text. This model was the result of realizing that majority of similar models did not cater for the African context where the target groups are not based on race and/or religious affiliation but mostly tribal differences which has proved fatal in the past.

The model can be improved greatly by using a large and representative dataset and optimization of the model to a better degree.



