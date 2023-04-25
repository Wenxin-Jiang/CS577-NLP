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
  - nateraw/world-happiness
model-index:
  - name: nateraw_world-happiness_2018_2.csv
    results:
      - task:
          type: tabular-classification
          name: tabular-classification
        dataset:
          type: nateraw/world-happiness
          name: nateraw/world-happiness
        metrics:
          - type: accuracy
            name: Accuracy
            value: 0.025641025975346565
          - type: loss
            name: Model loss
            value: 1.8496686220169067

---

# classification model trained on "nateraw/world-happiness"
🤖 [Load and use this model](https://mlconsole.com/model/hf/FaroukFaiz/nateraw_world-happiness_2018_2.csv) in one click.
🧑‍💻 [Train your own model](https://mlconsole.com) on ML Console.

