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
  - julien-c/kaggle-rounakbanik-pokemon
model-index:
  - name: pokemon_is_legendary
    results:
      - task:
          type: tabular-classification
          name: tabular-classification
        dataset:
          type: julien-c/kaggle-rounakbanik-pokemon
          name: pokemon.csv
        metrics:
          - type: accuracy
            name: Accuracy
            value: 1
          - type: loss
            name: Model loss
            value: 0.314619243144989

---

# pokemon.csv (#0)
Trained on [ML Console](https://mlconsole.com).

[Load the model on ML Console](https://mlconsole.com/model/hf/halflings/pokemon_is_legendary).
