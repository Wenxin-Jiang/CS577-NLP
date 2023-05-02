---
license: apache-2.0
language: en
library: transformers
other: distilroberta
datasets:
- Short Question Answer Assessment Dataset 
---

# DistilRoBERTa base model for Short Question Answer Assessment

## Model description

The pre-trained model is a distilled version of the [RoBERTa-base model](https://huggingface.co/roberta-base). It follows the same training procedure as [DistilBERT](https://huggingface.co/distilbert-base-uncased).
The code for the distillation process can be found [here](https://github.com/huggingface/transformers/tree/master/examples/distillation).
This model is case-sensitive: it makes a difference between english and English.

The model has 6 layers, 768 dimension and 12 heads, totalizing 82M parameters (compared to 125M parameters for RoBERTa-base).
On average DistilRoBERTa is twice as fast as Roberta-base.

We encourage to check [RoBERTa-base model](https://huggingface.co/roberta-base) to know more about usage, limitations and potential biases.



This is a classification model that solves Short Question Answer Assessment task, finetuned [pretrained DistilRoBERTa model](https://huggingface.co/distilroberta-base) on 
[Question Answer Assessment dataset](#)

## Intended uses & limitations

This can only be used for the kind of questions and answers provided by that are similar to the ones in the dataset of [Banjade et al.](https://aclanthology.org/W16-0520.pdf).


### How to use

You can use this model directly with a :

```python
>>> from transformers import pipeline
>>> classifier = pipeline("text-classification", model="Giyaseddin/distilroberta-base-finetuned-short-answer-assessment", return_all_scores=True)
>>> context = "To rescue a child who has fallen down a well, rescue workers fasten him to a rope, the other end of which is then reeled in by a machine. The rope pulls the child straight upward at steady speed."
>>> question = "How does the amount of tension in the rope compare to the downward force of gravity acting on the child?"
>>> ref_answer = "Since the child is being raised straight upward at a constant speed, the net force on the child is zero and all the forces balance. That means that the tension in the rope balances the downward force of gravity."
>>> student_answer = "The tension force is higher than the force of gravity."
>>> 
>>> body = " [SEP] ".join([context, question, ref_answer, student_answer])
>>> raw_results = classifier([body])
>>> raw_results
[[{'label': 'LABEL_0', 'score': 0.0004029414849355817},
  {'label': 'LABEL_1', 'score': 0.0005476847873069346},
  {'label': 'LABEL_2', 'score': 0.998059093952179},
  {'label': 'LABEL_3', 'score': 0.0009902542224153876}]]
>>> _LABELS_ID2NAME = {0: "correct", 1: "correct_but_incomplete", 2: "contradictory", 3: "incorrect"}
>>> results = []
>>> for result in raw_results:
    	for score in result:
        	results.append([
            	{_LABELS_ID2NAME[int(score["label"][-1:])]: "%.2f" % score["score"]}
        	])

>>> results
[[{'correct': '0.00'}],
 [{'correct_but_incomplete': '0.00'}],
 [{'contradictory': '1.00'}],
 [{'incorrect': '0.00'}]]
```

### Limitations and bias

Even if the training data used for this model could be characterized as fairly neutral, this model can have biased
predictions. It also inherits some of
[the bias of its teacher model](https://huggingface.co/bert-base-uncased#limitations-and-bias).

This bias will also affect all fine-tuned versions of this model.

Also one of the limiations of this model is the length, longer sequences would lead to wrong predictions, due to the pre-processing phase (after concatentating the input sequences, the important student answer might be pruned!)

## Pre-training data

## Training data

The RoBERTa model was pretrained on the reunion of five datasets:
- [BookCorpus](https://yknzhu.wixsite.com/mbweb), a dataset consisting of 11,038 unpublished books;
- [English Wikipedia](https://en.wikipedia.org/wiki/English_Wikipedia) (excluding lists, tables and headers) ;
- [CC-News](https://commoncrawl.org/2016/10/news-dataset-available/), a dataset containing 63 millions English news
  articles crawled between September 2016 and February 2019.
- [OpenWebText](https://github.com/jcpeterson/openwebtext), an opensource recreation of the WebText dataset used to
  train GPT-2,
- [Stories](https://arxiv.org/abs/1806.02847) a dataset containing a subset of CommonCrawl data filtered to match the
  story-like style of Winograd schemas.

Together theses datasets weight 160GB of text.

## Fine-tuning data

The annotated dataset consists of 900 students’ short constructed answers and their correctness in the given context. Four qualitative levels of correctness are defined, correct, correct-but-incomplete, contradictory and Incorrect.


## Training procedure

### Preprocessing

In the preprocessing phase, the following parts are concatenated: _question context_, _question_, _reference_answer_, and _student_answer_ using the separator `[SEP]`.
This makes the full text as:

```
[CLS] Context Sentence [SEP] Question Sentence [SEP] Reference Answer Sentence [SEP] Student Answer Sentence [CLS]
```

The data are splitted according to the following ratio:
- Training set 80%.
- Test set 20%.

Lables are mapped as: `{0: "correct", 1: "correct_but_incomplete", 2: "contradictory", 3: "incorrect"}`

### Fine-tuning

The model was finetuned on GeForce GTX 960M for 20 minuts. The parameters are:

|      Parameter      | Value | 
|:-------------------:|:-----:|
|    Learning rate    | 5e-5  | 
|    Weight decay     | 0.01  | 
| Training batch size |   8   | 
|       Epochs        |   4   | 

Here is the scores during the training:


|   Epoch    | Training Loss | 	 Validation Loss | 	 Accuracy |   	 F1   |  Precision |  Recall  |
|:----------:|:-------------:|:-----------------:|:----------:|:---------:|:----------:|:--------:|
|     1      |   No log      |     	0.773334     | 	0.713706  |  0.711398 |  0.746059  | 0.713706 |
|     2      |   1.069200    |     	0.404932     | 	0.885279  |  0.884592 |  0.886699  | 0.885279 |
|     3      |   0.473700    |     	0.247099     | 	0.931980  |  0.931675 |  0.933794  | 0.931980 |
|     3      |   0.228000    |     	0.205577     | 	0.954315  |  0.954210 |  0.955258  | 0.954315 |

## Evaluation results

When fine-tuned on downstream task of Question Answer Assessment 4 class classification, this model achieved the following results:
(scores are rounded to 2 floating points)


|						   |  precision |  recall | f1-score | support |
|:------------------------:|:----------:|:-------:|:--------:|:-------:|
|  		  _correct_		   |   0.933    |  0.992  |   0.962  |   366   |
| _correct_but_incomplete_ |   0.976    |  0.934  |   0.954  |   257   |
|  	   _contradictory_	   |   0.938    |  0.929  |   0.933  |   113   |
|  		 _incorrect_	   |   0.975    |  0.932  |   0.953  |   249   |
|   	 accuracy		   |     -      |    -    |   0.954  |   985   |
|  		macro avg		   |   0.955    |  0.947  |   0.950  |   985   |
| 	  weighted avg		   |   0.955    |  0.954  |   0.954  |   985   |

Confusion matrix:


|	 Actual \ Predicted	   | _correct_ | _correct_but_incomplete_ | _contradictory_ | _incorrect_ |
|:------------------------:|:---------:|:------------------------:|:---------------:|:-----------:|
|  		  _correct_		   |	363	   |	 		3			  |	 	   0		|	  0 	  |
| _correct_but_incomplete_ |	14	   |	 	    240			  |	 	   0		|	  3 	  |
|  	   _contradictory_	   |	5	   |	 		0			  |	 	   105		|	  3 	  |
|  		 _incorrect_	   |	7	   |	 		3			  |	 	   7		|	  232 	  |



The AUC score is: 'micro'= **0.9695** and 'macro': **0.9650**
