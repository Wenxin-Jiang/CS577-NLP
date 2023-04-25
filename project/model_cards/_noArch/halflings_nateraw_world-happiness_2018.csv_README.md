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
  - name: nateraw_world-happiness_2018.csv
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
            value: 0.925627589225769
          - type: loss
            name: Model loss
            value: 1.1342997550964355

---

# nateraw/world-happiness/2018.csv (#0)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/halflings/nateraw_world-happiness_2018.csv).
