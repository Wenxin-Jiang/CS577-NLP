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
  - house_price_prediction
model-index:
  - name: house_price_prediction_ser
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: house_price_prediction
          name: house_price_prediction
        metrics:
          - type: mae
            name: Mean absolute error
            value: 5.011783599853516
          - type: loss
            name: Model loss
            value: 43.01755905151367

---

# regression model trained on "house_price_prediction"
🤖 [Load and use this model](https://mlconsole.com/model/hf/halflings/house_price_prediction_ser) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

