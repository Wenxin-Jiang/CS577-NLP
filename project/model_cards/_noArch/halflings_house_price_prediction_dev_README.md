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
  - name: house_price_prediction_dev
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
            value: 7.064809322357178
          - type: loss
            name: Model loss
            value: 98.9962387084961

---

# regression model trained on "house_price_prediction"
🤖 [Load and use this model](https://mlconsole.com/model/hf/halflings/house_price_prediction_dev) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

