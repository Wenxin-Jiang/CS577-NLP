---
license: unknown
inference: false
tags:
  - mlconsole
  - tabular-regression
library_name: mlconsole
metrics:
  - mae
  - loss
datasets:
  - nateraw/world-happiness
model-index:
  - name: nateraw_world-happiness_2019.csv
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: nateraw/world-happiness
          name: nateraw/world-happiness
        metrics:
          - type: mae
            name: Mean absolute error
            value: 0.9219764471054077
          - type: loss
            name: Model loss
            value: 1.3516408205032349

---

# nateraw/world-happiness/2019.csv (1) (#3)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/halflings/nateraw_world-happiness_2019.csv).
