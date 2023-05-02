---
language: en
widget:
- text: $answer$ ; $mcoptions$ ; $question$ = What is the color of a cloudy sky?
license: apache-2.0
---

# macaw-answer-11b

## Model description

Macaw (<b>M</b>ulti-<b>a</b>ngle <b>c</b>(q)uestion <b>a</b>ns<b>w</b>ering) is a ready-to-use model capable of 
general question answering, 
showing robustness outside the domains it was trained on. It has been trained in "multi-angle" fashion, 
which means it can handle a flexible set of input and output "slots" 
(question, answer, multiple-choice options, context, and explanation) .

Macaw was built on top of [T5](https://github.com/google-research/text-to-text-transfer-transformer) and comes in 
three sizes: [macaw-11b](https://huggingface.co/allenai/macaw-11b), [macaw-3b](https://huggingface.co/allenai/macaw-3b), 
and [macaw-large](https://huggingface.co/allenai/macaw-large), as well as an answer-focused version featured on 
various leaderboards [macaw-answer-11b](https://huggingface.co/allenai/macaw-answer-11b).

See https://github.com/allenai/macaw for more details.