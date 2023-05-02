---
language: 
  - en
tags:
- text2text-generation
- pytorch
license: "gpl-3.0"
datasets:
- samsum
widget:
- text: "Ruben has forgotten what the homework was. Alex tells him to ask the teacher."
  example_title: "I forgot my homework"
- text: "Mac is lost at the zoo. Frank says he is at the gorilla exhibit. Charlie is going to see the minks."
  example_title: "Very sunny"
- text: "Mac has started to date Dennis's mother. Dennis is going to beat him up."
  example_title: "Not very sunny"
---

# Maeve - SAMSum

Maeve is a language model that is similar to BART in structure but trained specially using a CAT (Conditionally Adversarial Transformer).

This allows the model to learn to create long-form text from short entries with high degrees of control and coherence that are impossible to achieve with traditional transformers.

This specific model has been trained on the SAMSum dataset, and can invert summaries into full-length news articles. Feel free to try examples on the right!
