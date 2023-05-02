---
language: es
tags:
- zero-shot-classification
- nli
- pytorch
datasets:
- xnli
pipeline_tag: zero-shot-classification
license: apache-2.0
widget:
- text: "El autor se perfila, a los 50 años de su muerte, como uno de los grandes de su siglo"
  candidate_labels: "cultura, sociedad, economia, salud, deportes"
---
# Zero-shot SELECTRA: A zero-shot classifier based on SELECTRA

*Zero-shot SELECTRA* is a [SELECTRA model](https://huggingface.co/Recognai/selectra_small) fine-tuned on the Spanish portion of the [XNLI dataset](https://huggingface.co/datasets/xnli). You can use it with Hugging Face's [Zero-shot pipeline](https://huggingface.co/transformers/master/main_classes/pipelines.html#transformers.ZeroShotClassificationPipeline) to make [zero-shot classifications](https://joeddav.github.io/blog/2020/05/29/ZSL.html).

In comparison to our previous zero-shot classifier [based on BETO](https://huggingface.co/Recognai/bert-base-spanish-wwm-cased-xnli), zero-shot SELECTRA is **much more lightweight**. As shown in the *Metrics* section, the *small* version (5 times fewer parameters) performs slightly worse, while the *medium* version (3 times fewer parameters) **outperforms** the BETO based zero-shot classifier.

## Usage

```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification", 
                       model="Recognai/zeroshot_selectra_medium")

classifier(
    "El autor se perfila, a los 50 años de su muerte, como uno de los grandes de su siglo",
    candidate_labels=["cultura", "sociedad", "economia", "salud", "deportes"],
    hypothesis_template="Este ejemplo es {}."
)
"""Output
{'sequence': 'El autor se perfila, a los 50 años de su muerte, como uno de los grandes de su siglo',
 'labels': ['sociedad', 'cultura', 'salud', 'economia', 'deportes'],
 'scores': [0.3711881935596466,
  0.25650349259376526,
  0.17355826497077942,
  0.1641489565372467,
  0.03460107371211052]}
"""
```

The `hypothesis_template` parameter is important and should be in Spanish. **In the widget on the right, this parameter is set to its default value: "This example is {}.", so different results are expected.**

## Metrics

| Model | Params | XNLI (acc) | \*MLSUM (acc) |
| --- | --- | --- | --- |
| [zs BETO](https://huggingface.co/Recognai/bert-base-spanish-wwm-cased-xnli) | 110M | 0.799 | 0.530 |
| [zs SELECTRA medium](https://huggingface.co/Recognai/zeroshot_selectra_medium) | 41M | **0.807** | **0.589** |
| zs SELECTRA small | **22M** | 0.795 | 0.446 |

\*evaluated with zero-shot learning (ZSL)

- **XNLI**: The stated accuracy refers to the test portion of the [XNLI dataset](https://huggingface.co/datasets/xnli), after finetuning the model on the training portion.
- **MLSUM**: For this accuracy we take the test set of the [MLSUM dataset](https://huggingface.co/datasets/mlsum) and classify the summaries of 5 selected labels. For details, check out our [evaluation notebook](https://github.com/recognai/selectra/blob/main/zero-shot_classifier/evaluation.ipynb)

## Training

Check out our [training notebook](https://github.com/recognai/selectra/blob/main/zero-shot_classifier/training.ipynb) for all the details.

## Authors

- David Fidalgo ([GitHub](https://github.com/dcfidalgo))
- Daniel Vila ([GitHub](https://github.com/dvsrepo))
- Francisco Aranda ([GitHub](https://github.com/frascuchon))
- Javier Lopez ([GitHub](https://github.com/javispp))