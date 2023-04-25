---
language: en
widget:
- text: "It has been determined that the amount of greenhouse gases have decreased by almost half because of the prevalence in the utilization of nuclear power."
---

### Welcome to RoBERTArg!

🤖 **Model description**

This model was trained on ~25k heterogeneous manually annotated sentences (📚 [Stab et al. 2018](https://www.aclweb.org/anthology/D18-1402/)) of controversial topics to classify text into one of two labels: 🏷 **NON-ARGUMENT** (0) and **ARGUMENT** (1).

🗃 **Dataset**

The dataset (📚 Stab et al. 2018) consists of **ARGUMENTS** (\~11k) that either support or oppose a topic if it includes a relevant reason for supporting or opposing the topic, or as a **NON-ARGUMENT** (\~14k) if it does not include reasons. The authors focus on controversial topics, i.e., topics that include "an obvious polarity to the possible outcomes" and compile a final set of eight controversial topics: _abortion, school uniforms, death penalty, marijuana legalization, nuclear energy, cloning, gun control, and minimum wage_.

| TOPIC | ARGUMENT | NON-ARGUMENT |
|----|----|----|
| abortion | 2213 | 2,427 |
| school uniforms | 325 | 1,734 |
| death penalty | 325 | 2,083 |
| marijuana legalization | 325 | 1,262 |
| nuclear energy | 325 | 2,118 |
| cloning | 325 | 1,494 |
| gun control | 325 | 1,889 |
| minimum wage | 325 | 1,346 |

🏃🏼‍♂️**Model training**

**RoBERTArg** was fine-tuned on a RoBERTA (base) pre-trained model from HuggingFace using the HuggingFace trainer with the following hyperparameters:

```
training_args = TrainingArguments(
    num_train_epochs=2,
    learning_rate=2.3102e-06,
    seed=8,
    per_device_train_batch_size=64,
    per_device_eval_batch_size=64,
)
```

📊 **Evaluation**

The model was evaluated on an evaluation set (20%):

| Model | Acc | F1 | R arg | R non | P arg | P non |
|----|----|----|----|----|----|----|
| RoBERTArg | 0.8193 | 0.8021 | 0.8463 | 0.7986 | 0.7623 | 0.8719 |

Showing the **confusion matrix** using again the evaluation set:

| | ARGUMENT | NON-ARGUMENT |
|----|----|----|
| ARGUMENT | 2213 | 558 |
| NON-ARGUMENT | 325 | 1790 |

⚠️ **Intended Uses & Potential Limitations**

The model can only be a starting point to dive into the exciting field of argument mining. But be aware. An argument is a complex structure, with multiple dependencies. Therefore, the model may perform less well on different topics and text types not included in the training set.

Enjoy and stay tuned! 🚀

🐦 Twitter: [@chklamm](http://twitter.com/chklamm)