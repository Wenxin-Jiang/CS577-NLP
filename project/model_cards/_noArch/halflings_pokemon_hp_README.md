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
  - julien-c/kaggle-rounakbanik-pokemon
model-index:
  - name: pokemon_hp
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: julien-c/kaggle-rounakbanik-pokemon
          name: julien-c/kaggle-rounakbanik-pokemon
        metrics:
          - type: mae
            name: Mean absolute error
            value: 4.479848861694336
          - type: loss
            name: Model loss
            value: 51.252288818359375

---

# pokemon.csv (1) (#1)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/halflings/pokemon_hp).
