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
  - name: titanic_mlconsole
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
            value: 0.792792797088623
          - type: loss
            name: Model loss
            value: 0.5146282911300659

---

# train.csv (#0)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/osanseviero/titanic_mlconsole).
