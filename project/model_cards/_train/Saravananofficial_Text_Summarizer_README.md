---
license: apache-2.0
---
# Text-Summarizer
## About

An Abstractive text summarizer trained using lstm based sequence to sequence model with attention mechanisim. The attention model is used for generating each word of the summary conditioned on the input sentence.

- Used CNN_DailyMail dataset.
- Code + Deployment : https://www.youtube.com/watch?v=LFZBA99NOpU
[![IMAGE ALT TEXT HERE](https://i.ytimg.com/vi/LFZBA99NOpU/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCQacvrk4iyXIEhzufcyLKd9ZWHlQ)](https://www.youtube.com/watch?v=LFZBA99NOpU)

### Training Model Overview

loss graph

![Output](./train_log.jpeg "loss graph")

encoder-decoder overview
![Output1](./model_plot.jpeg "model overview")

## Conclusion

- 🫶  The machine learning model to convert a text document to abstract is done successfully.
- 🫶  Created a Flask app using an api call from this repository & deployed the app in heroku app.

## Deployment:

- 🫶  https://text-summariser-v1.herokuapp.com/
