---
license: unknown
inference: false
tags:
  - mlconsole
  - tabular-classification
library_name: mlconsole
metrics:
  - accuracy
  - loss
datasets:
  - train.csv
model-index:
  - name: titanic-survival-with-ml-console
    results:
      - task:
          type: tabular-classification
          name: tabular-classification
        dataset:
          type: train.csv
          name: train.csv
        metrics:
          - type: accuracy
            name: Accuracy
            value: 0.7882882952690125
          - type: loss
            name: Model loss
            value: 0.5075606107711792

---

# train.csv (#2)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/victor/titanic-survival-with-ml-console).
