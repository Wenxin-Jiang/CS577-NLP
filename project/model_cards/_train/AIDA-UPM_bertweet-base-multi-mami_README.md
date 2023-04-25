---
pipeline_tag: text-classification
tags:
- text-classification
- misogyny
language: en
license: apache-2.0
widget:
- text: "Women wear yoga pants because men don't stare at their personality"
  example_title: "Misogyny detection"
---

# bertweet-base-multi-mami
This is a Bertweet model: It maps sentences & paragraphs to a 768 dimensional dense vector space and classifies them into 5 multi labels.

# Multilabels
    label2id={
        "misogynous": 0,
        "shaming": 1,
        "stereotype": 2,
        "objectification": 3,
        "violence": 4,
    },
