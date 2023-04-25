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
  - diabetes_detection
model-index:
  - name: diabetes_detection_scaler
    results:
      - task:
          type: tabular-classification
          name: tabular-classification
        dataset:
          type: diabetes_detection
          name: diabetes_detection
        metrics:
          - type: accuracy
            name: Accuracy
            value: 0.7864583730697632
          - type: loss
            name: Model loss
            value: 0.510176420211792

---

# classification model trained on "diabetes_detection"
🤖 [Load and use this model](https://mlconsole.com/model/hf/halflings/diabetes_detection_scaler) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

