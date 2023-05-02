---
license: apache-2.0
tags:
- question_answering
- qa
- answer_consolidation
widget:
- text: "When will the recession happen? <sep> never <sep> it won't happen"
  example_title: "Example 1"
- text: "When will the recession happen? <sep> it's going on right now <sep> not before next year"
  example_title: "Example 2"
---

# QA Consolidation Model
Model card for the QA Consolidation (step 3) of the Discord Questions framework (EMNLP 2022 - Findings). The model assesses the similarity between two answers (a1, a2) to a question Q. The score obtained is on a scale from 1 (most dissimilar) to 5 (most similar). See example below for formatting.

The model is a RoBERTa-large model, finetuned on the [MOCHA dataset](https://arxiv.org/abs/2010.03636), and a 5-pt version of the [Answer Equivalence](https://arxiv.org/abs/2202.07654v1) dataset. For a (question, answer1, answer2)-tuple, the model outputs a [1-5] answer similarity score, where 5 is most similar.


Example usage of the model:
```py
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import itertools

ae_tokenizer = AutoTokenizer.from_pretrained("Salesforce/qa_consolidation")
ae_model = AutoModelForSequenceClassification.from_pretrained("Salesforce/qa_consolidation").eval()

question = "When will the recession happen?"
answers = ["probably next January", "never", "we're already in a recession", "it won't happen", "it's going on right now", "not before next year", "upcoming January-March"]
dataset = [{"a1": a1, "a2": a2, "input": "%s <sep> %s <sep> %s" % (question, a1, a2)} for a1, a2 in itertools.combinations(answers, 2)]

input_ids = ae_tokenizer.batch_encode_plus([d["input"] for d in dataset], add_special_tokens=False, padding=True, return_tensors="pt")["input_ids"]
scores = ae_model(input_ids=input_ids)["logits"][:, 0].tolist()
for d, score in zip(dataset, scores):
    d["score"] = score

for d in sorted(dataset, key=lambda d: -d["score"]):
    print("[Score: %.3f] %s" % (d["score"], d["input"]))
```


The output then looks like:
```
[Score: 4.980] When will the recession happen? <sep> never <sep> it won't happen
[Score: 3.831] When will the recession happen? <sep> probably next January <sep> upcoming January-March
[Score: 3.366] When will the recession happen? <sep> we're already in a recession <sep> it's going on right now
[Score: 2.302] When will the recession happen? <sep> never <sep> not before next year
[Score: 1.899] When will the recession happen? <sep> probably next January <sep> not before next year
[Score: 1.290] When will the recession happen? <sep> it won't happen <sep> not before next year
[Score: 1.230] When will the recession happen? <sep> we're already in a recession <sep> it won't happen
[Score: 1.187] When will the recession happen? <sep> not before next year <sep> upcoming January-March
[Score: 1.126] When will the recession happen? <sep> it won't happen <sep> it's going on right now
[Score: 1.108] When will the recession happen? <sep> never <sep> we're already in a recession
[Score: 1.099] When will the recession happen? <sep> we're already in a recession <sep> not before next year
[Score: 1.091] When will the recession happen? <sep> probably next January <sep> it's going on right now
[Score: 1.084] When will the recession happen? <sep> never <sep> it's going on right now
[Score: 1.048] When will the recession happen? <sep> probably next January <sep> we're already in a recession
[Score: 1.023] When will the recession happen? <sep> probably next January <sep> it won't happen
[Score: 1.017] When will the recession happen? <sep> probably next January <sep> never
[Score: 1.006] When will the recession happen? <sep> it's going on right now <sep> not before next year
[Score: 0.994] When will the recession happen? <sep> we're already in a recession <sep> upcoming January-March
[Score: 0.917] When will the recession happen? <sep> it's going on right now <sep> upcoming January-March
[Score: 0.903] When will the recession happen? <sep> it won't happen <sep> upcoming January-March
[Score: 0.896] When will the recession happen? <sep> never <sep> upcoming January-March
```


In the paper, we find that a threshold of `T=2.75` achieves the highest F1 score on the validation portions of the two datasets. In the above example, only the first three pairs would be classified as equivalent answers, and all pairs below would be labeled as non-equivalent answers.