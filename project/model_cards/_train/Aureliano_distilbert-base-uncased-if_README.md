---
language: en
license: apache-2.0
datasets:
- bookcorpus
- wikipedia

---

# DistilBERT base model (uncased) for Interactive Fiction

[`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) finetuned on a dataset of Interactive
Fiction commands.

Details on the datasets can be found [here](https://github.com/aporporato/jericho-corpora).

The resulting model scored an accuracy of 0.976253 on the WordNet task test set.

## How to use the discriminator in `transformers`

```python
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer

discriminator = TFAutoModelForSequenceClassification.from_pretrained("Aureliano/distilbert-base-uncased-if")
tokenizer = AutoTokenizer.from_pretrained("Aureliano/distilbert-base-uncased-if")

text = "get lamp"
encoded_input = tokenizer(text, return_tensors='tf')
output = discriminator(encoded_input)
prediction = tf.nn.softmax(output["logits"][0], -1)
label = discriminator.config.id2label[tf.math.argmax(prediction).numpy()]
print(text, ":", label)  # take.v.04 -> "get into one's hands, take physically"

```

## How to use the discriminator in `transformers` on a custom dataset

(Heavily based on: https://github.com/huggingface/notebooks/blob/master/examples/text_classification-tf.ipynb)

```python
import math
import numpy as np

import tensorflow as tf
from datasets import load_metric, Dataset, DatasetDict
from transformers import TFAutoModel, TFAutoModelForSequenceClassification, AutoTokenizer, DataCollatorWithPadding, create_optimizer
from transformers.keras_callbacks import KerasMetricCallback

# This example shows how this model can be used:
#  you should finetune the model of your specific corpus if commands, bigger than this
dict_train = {
    "idx": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20"],
    "sentence": ["e", "get pen", "drop book", "x paper", "i", "south", "get paper", "drop the pen", "x book",
                 "inventory", "n", "get the book", "drop paper", "look at Pen", "inv", "g", "s", "get sandwich",
                 "drop sandwich", "x sandwich", "agin"],
    "label": ["travel.v.01", "take.v.04", "drop.v.01", "examine.v.02", "inventory.v.01", "travel.v.01", "take.v.04",
              "drop.v.01", "examine.v.02", "inventory.v.01", "travel.v.01", "take.v.04", "drop.v.01", "examine.v.02",
              "inventory.v.01", "repeat.v.01", "travel.v.01", "take.v.04", "drop.v.01", "examine.v.02", "repeat.v.01"]
}
dict_val = {
    "idx": ["0", "1", "2", "3", "4", "5"],
    "sentence": ["w", "get shield", "drop sword", "x spikes", "i", "repeat"],
    "label": ["travel.v.01", "take.v.04", "drop.v.01", "examine.v.02", "inventory.v.01", "repeat.v.01"]
}

raw_train_dataset = Dataset.from_dict(dict_train)
raw_val_dataset = Dataset.from_dict(dict_val)
raw_dataset = DatasetDict()
raw_dataset["train"] = raw_train_dataset
raw_dataset["val"] = raw_val_dataset
raw_dataset = raw_dataset.class_encode_column("label")
print(raw_dataset)
print(raw_dataset["train"].features)
print(raw_dataset["val"].features)
print(raw_dataset["train"][1])
label2id = {}
id2label = {}
for i, l in enumerate(raw_dataset["train"].features["label"].names):
    label2id[l] = i
    id2label[i] = l

discriminator = TFAutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased",
                                                                     label2id=label2id,
                                                                     id2label=id2label)
discriminator.distilbert = TFAutoModel.from_pretrained("Aureliano/distilbert-base-uncased-if")
tokenizer = AutoTokenizer.from_pretrained("Aureliano/distilbert-base-uncased-if")

tokenize_function = lambda example: tokenizer(example["sentence"], truncation=True)

pre_tokenizer_columns = set(raw_dataset["train"].features)
encoded_dataset = raw_dataset.map(tokenize_function, batched=True)
tokenizer_columns = list(set(encoded_dataset["train"].features) - pre_tokenizer_columns)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer, return_tensors="tf")

batch_size = len(encoded_dataset["train"])
tf_train_dataset = encoded_dataset["train"].to_tf_dataset(
    columns=tokenizer_columns,
    label_cols=["labels"],
    shuffle=True,
    batch_size=batch_size,
    collate_fn=data_collator
)
tf_validation_dataset = encoded_dataset["val"].to_tf_dataset(
    columns=tokenizer_columns,
    label_cols=["labels"],
    shuffle=False,
    batch_size=batch_size,
    collate_fn=data_collator
)

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
num_epochs = 20
batches_per_epoch = math.ceil(len(encoded_dataset["train"]) / batch_size)
total_train_steps = int(batches_per_epoch * num_epochs)

optimizer, schedule = create_optimizer(
    init_lr=2e-5, num_warmup_steps=total_train_steps // 5, num_train_steps=total_train_steps
)

metric = load_metric("accuracy")


def compute_metrics(eval_predictions):
    logits, labels = eval_predictions
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


metric_callback = KerasMetricCallback(metric_fn=compute_metrics, eval_dataset=tf_validation_dataset)
callbacks = [metric_callback]

discriminator.compile(optimizer=optimizer, loss=loss, metrics=["sparse_categorical_accuracy"])
discriminator.fit(
    tf_train_dataset,
    epochs=num_epochs,
    validation_data=tf_validation_dataset,
    callbacks=callbacks
)

print("Evaluate on test data")
results = discriminator.evaluate(tf_validation_dataset)
print("test loss, test acc:", results)

text = "i"
encoded_input = tokenizer(text, return_tensors='tf')
output = discriminator(encoded_input)
prediction = tf.nn.softmax(output["logits"][0], -1)
label = id2label[tf.math.argmax(prediction).numpy()]
print("\n", text, ":", label,
      "\n")  # ideally 'inventory.v.01' (-> "make or include in an itemized record or report"), but probably only with a better finetuning dataset

text = "get lamp"
encoded_input = tokenizer(text, return_tensors='tf')
output = discriminator(encoded_input)
prediction = tf.nn.softmax(output["logits"][0], -1)
label = id2label[tf.math.argmax(prediction).numpy()]
print("\n", text, ":", label,
      "\n")  # ideally 'take.v.04' (-> "get into one's hands, take physically"), but probably only with a better finetuning dataset

text = "w"
encoded_input = tokenizer(text, return_tensors='tf')
output = discriminator(encoded_input)
prediction = tf.nn.softmax(output["logits"][0], -1)
label = id2label[tf.math.argmax(prediction).numpy()]
print("\n", text, ":", label,
      "\n")  # ideally 'travel.v.01' (-> "change location; move, travel, or proceed, also metaphorically"), but probably only with a better finetuning dataset

```

## How to use in a Rasa pipeline

The model can integrated in a Rasa pipeline through
a [`LanguageModelFeaturizer`](https://rasa.com/docs/rasa/components#languagemodelfeaturizer)

```yaml
recipe: default.v1
language: en

pipeline:
  # See https://rasa.com/docs/rasa/tuning-your-model for more information.
    ...
    - name: "WhitespaceTokenizer"
    ...
    - name: LanguageModelFeaturizer
      model_name: "distilbert"
      model_weights: "Aureliano/distilbert-base-uncased-if"
    ...
```