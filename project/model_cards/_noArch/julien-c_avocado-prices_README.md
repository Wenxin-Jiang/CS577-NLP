---
license: apache-2.0
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
  - name: avocado-prices
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: nateraw/avocado-prices
          name: avocado.csv
        metrics:
          - type: mae
            name: Mean absolute error
            value: 0.22897861897945404
          - type: loss
            name: Model loss
            value: 0.08849651366472244

---

# regression model trained on "nateraw/avocado-prices"
🤖 [Load and use this model](https://mlconsole.com/model/hf/julien-c/avocado-prices) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

### Screenshots

![predict interface](screenshots/predict.png)