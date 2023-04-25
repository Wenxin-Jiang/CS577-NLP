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
  - unsw_nb15_training-set.csv
model-index:
  - name: predict-intrusion2
    results:
      - task:
          type: tabular-classification
          name: tabular-classification
        dataset:
          type: unsw_nb15_training-set.csv
          name: unsw_nb15_training-set.csv
        metrics:
          - type: accuracy
            name: Accuracy
            value: 0.9487999677658081
          - type: loss
            name: Model loss
            value: 0.36453571915626526

---

# classification model trained on "unsw_nb15_training-set.csv"
🤖 [Load and use this model](https://mlconsole.com/model/hf/zakariaelaouene/predict-intrusion2) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

