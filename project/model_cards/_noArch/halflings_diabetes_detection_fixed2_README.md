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
  - name: diabetes_detection_fixed2
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
            value: 0.78125
          - type: loss
            name: Model loss
            value: 0.523585319519043

---

# classification model trained on "diabetes_detection"
🤖 [Load and use this model](https://mlconsole.com/model/hf/halflings/diabetes_detection_fixed2) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

