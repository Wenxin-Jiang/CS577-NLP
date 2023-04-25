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
  - pokemon.csv
model-index:
  - name: pokemon.csv
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: pokemon.csv
          name: pokemon.csv
        metrics:
          - type: mae
            name: Mean absolute error
            value: 3.10766339302063
          - type: loss
            name: Model loss
            value: 18.141359329223633

---

# pokemon.csv (#0)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/halflings/pokemon.csv).
