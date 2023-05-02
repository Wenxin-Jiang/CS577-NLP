---
license: mit
widget:
- text: "The man turned on the faucet <mask> water flows out."
- text: "The woman received her pension <mask> she retired."
---
# roberta-temporal-predictor
A RoBERTa-base model that is fine-tuned on the [The New York Times Annotated Corpus](https://catalog.ldc.upenn.edu/LDC2008T19)
to predict temporal precedence of two events. This is used as the ``temporality prediction'' component
in our ROCK framework for reasoning about commonsense causality. See our [paper](https://arxiv.org/abs/2202.00436) for more details.

# Usage

You can directly use this model for filling-mask tasks, as shown in the example widget.
However, for better temporal inference, it is recommended to symmetrize the outputs as
$$
P(E_1 \prec E_2) = \frac{1}{2} (f(E_1,E_2) + f(E_2,E_1))
$$
where ``f(E_1,E_2)`` denotes the predicted probability for ``E_1`` to occur preceding ``E_2``.
For simplicity, we implement the following TempPredictor class that incorporate this symmetrization automatically.
Below is an example usage for the ``TempPredictor`` class:
```python
from transformers import (RobertaForMaskedLM, RobertaTokenizer)
from src.temp_predictor import TempPredictor

TORCH_DEV = "cuda:0" # change as needed

tp_roberta_ft = src.TempPredictor(
    model=RobertaForMaskedLM.from_pretrained("CogComp/roberta-temporal-predictor"),
    tokenizer=RobertaTokenizer.from_pretrained("CogComp/roberta-temporal-predictor"),
    device=TORCH_DEV
)

E1 = "The man turned on the faucet."
E2 = "Water flows out."
t12 = tp_roberta_ft(E1, E2, top_k=5)
print(f"P('{E1}' before '{E2}'): {t12}")
```

# BibTeX entry and citation info

```bib
@misc{zhang2022causal,
      title={Causal Inference Principles for Reasoning about Commonsense Causality}, 
      author={Jiayao Zhang and Hongming Zhang and Dan Roth and Weijie J. Su},
      year={2022},
      eprint={2202.00436},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```