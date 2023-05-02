---
language: eng
tags:
- bert
license: apache-2.0

widget:
- text: "The hotel is very nicely located"
  example_title: "Example 1"
- text: "The reception staff were extremely helpful and very welcoming"
  example_title: "Example 2"
- text: "There is no balcony in the rooms on the mountain side"
  example_title: "Example 3"
- text: "A bit pricey"
  example_title: "Example 4"
---

# English Hotel Review Sentiment Classification
A model trained on English Hotel Reviews from Switzerland. The base model is the [bert-base-uncased](https://huggingface.co/bert-base-uncased). The last hidden layer of the base model was extracted and a classification layer was added. The entire model was then trained for 5 epochs on our dataset.