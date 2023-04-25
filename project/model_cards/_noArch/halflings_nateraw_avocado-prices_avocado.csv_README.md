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
  - nateraw/avocado-prices
model-index:
  - name: nateraw_avocado-prices_avocado.csv
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: nateraw/avocado-prices
          name: nateraw/avocado-prices
        metrics:
          - type: mae
            name: Mean absolute error
            value: 0.2147810310125351
          - type: loss
            name: Model loss
            value: 0.0813632383942604

---

# regression model trained on "nateraw/avocado-prices"
🤖 [Load and use this model](https://mlconsole.com/model/hf/halflings/nateraw_avocado-prices_avocado.csv) in one click.
🧑‍💻 Train your own model on [ML Console](https://mlconsole.com).

