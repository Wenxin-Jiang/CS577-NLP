---
license: mit
---

Base model: [roberta-large](https://huggingface.co/roberta-large)

Fine tuned for persuadee donation detection on the [Persuasion For Good Dataset](https://gitlab.com/ucdavisnlp/persuasionforgood) (Wang et al., 2019):

Given a complete dialogue from Persuasion For Good, the task is to predict the binary label:
 - 0: the persuadee does not intend to donate
 - 1: the persuadee intends to donate

Only persuadee utterances are input to the model for this task - persuader utterances are discarded. Each training example is the concatenation of all persuadee utterances in a single dialogue, each separated by the `</s>` token.

For example:

**Input**: `<s>How are you?</s>Can you tell me more about the charity?</s>...</s>Sure, I'll donate a dollar.</s>...</s>`

**Label**: 1

**Input**: `<s>How are you?</s>Can you tell me more about the charity?</s>...</s>I am not interested.</s>...</s>`

**Label**: 0

The following Dialogues were excluded:
 - 146 dialogues where a donation of 0 was made at the end of the task but a non-zero amount was pledged by the persuadee in the dialogue, per the following regular expression: `(?:\$(?:0\.)?[1-9]|[1-9][.0-9]*?(?: ?\$| dollars?| cents?))`
 
Data Info:
 - **Training set**: 587 dialogues, using actual end-task donations as labels
 - **Validation set**: 141 dialogues, using manual donation intention labels from Persuasion For Good 'AnnSet'
 - **Test set**: 143 dialogues, using manual donation intention labels from Persuasion For Good 'AnnSet'

Training Info:
 - **Loss**: CrossEntropy with class weights: 1.5447 (class 0) and 0.7393 (class 1). These weights were derived from the training split.
 - **Early Stopping**: The checkpoint with the highest validation macro f1 was selected. This occurred at step 35 (see training metrics for more detail).

Testing Info:
 - **Test Macro F1**: 0.893
 - **Test Accuracy**: 0.902