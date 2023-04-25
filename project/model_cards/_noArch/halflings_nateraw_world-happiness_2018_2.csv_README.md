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
  - name: nateraw_world-happiness_2018_2.csv
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
            value: 0.4946480691432953
          - type: loss
            name: Model loss
            value: 0.4008486866950989

---

# regression model trained on "nateraw/world-happiness"
🤖 [Load and use this model](https://mlconsole.com/model/hf/halflings/nateraw_world-happiness_2018_2.csv) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

