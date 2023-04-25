---
license: apache-2.0
tags:
  - mlconsole
  - tabular-regression
library_name: mlconsole
inference: false
datasets:
- julien-c/kaggle-rounakbanik-pokemon
metrics:
  - mae
  - loss
model-index:
  - name: pokemon-predict-hp
    results:
      - task:
          type: tabular-regression
          name: tabular-regression
        dataset:
          type: julien-c/kaggle-rounakbanik-pokemon
          name: pokemon.csv
        metrics:
          - type: mae
            name: Mean absolute error
            value: 15.908513069152832
          - type: loss
            name: Model loss
            value: 647.6045532226562

---

# pokemon.csv (#0)
Trained on [ML Console](https://mlconsole.com) on the [julien-c/kaggle-rounakbanik-pokemon](https://huggingface.co/datasets/julien-c/kaggle-rounakbanik-pokemon).

[Load the model on ML Console](https://mlconsole.com/model/hf/julien-c/pokemon-predict-hp).


### Screenshots of training

![](screenshots/training-curve.png)

![](screenshots/predict.png)

