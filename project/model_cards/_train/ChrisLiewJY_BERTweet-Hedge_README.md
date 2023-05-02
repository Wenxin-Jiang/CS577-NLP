---
license: mit
language: 
  - en
tags:
- uncertainty-detection
- social-media
- text-classification
widget:
- text: "It seems like Bitcoin prices are heading into bearish territory."
  example_title: "Hedge Detection (Positive - Label 1)"
- text: "Bitcoin prices have fallen by 42% in the last 30 days."
  example_title: "Hedge Detection (Negative - Label 0)"
---

### Overview
Fine tuned VinAI's BERTweet base model on the Wiki Weasel 2.0 Corpus from the [Szeged Uncertainty Corpus](https://rgai.inf.u-szeged.hu/node/160) for hedge (linguistic uncertainty) detection in social media texts. Model was trained and optimised using Ray Tune's implementation of Deep Mind's Population Based Training with the arithmetic mean of Accuracy & F1 as its evaluation metric.

### Labels
* LABEL_1 = Positive (Hedge is detected within text)
* LABEL_0 = Negative (No Hedges detected within text)

### <a name="models2"></a> Model Performance
Model | Accuracy | F1-Score | Accuracy & F1-Score
---|---|---|---
`BERTweet-Hedge` | 0.9680 | 0.8765 | 0.9222
