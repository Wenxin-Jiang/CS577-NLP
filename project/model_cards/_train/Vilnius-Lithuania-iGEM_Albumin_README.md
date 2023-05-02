# Albumin-15s

## Model description

This is a version of [Albert-base-v2](https://huggingface.co/albert-base-v2) for 15's long aptamers comparison to determine which one is more affine to target protein Albumin.

The Albert model was pretrained in the English language, it has many similarities with language or proteins and aptamers which is why we had to fine-tune it to help the model learn embedded positioning for aptamers to be able to distinguish better sequences.

More information can be found in our [github]() and our iGEMs [wiki]().

## Intended uses & limitations

You can use the fine-tuned model for either masked aptamer pair sequence classification, which one is more affine for target protein Albumin, prediction, but it's mostly intended to be fine-tuned again on a different length aptamer or simply expanded datasets.

#### How to use

This model can be used to predict compared affinity with dataset preprocessing function which encodes the specific type of data (Sequence1, Sequence2, Label) where Label indicates binary if Sequence1 is more affine to target protein Albumin.

```python
from transformers import AutoTokenizer, BertModel
mname = "Vilnius-Lithuania-iGEM/Albumin"
model = BertModel.from_pretrained(mname)
```

To predict batches of sequences you have to employ custom functions shown in [git/prediction.ipynb]()

#### Limitations and bias

It seems that fine-tuned Albert model for this kind of task has limition of 90 % accuracy predicting which aptamer is more suitable for a target protein, also Albert-large or immense dataset of 15s aptamer could increase accuracy few %, however extrapolation case is not studied and we cannot confirm this model is state-of-The-art when one of aptamers is SUPER good (has almost maximum entropy to the Albumin).

## Eval results

accuracy :  0.8601

precision:  0.8515

recall   :  0.8725

f1       :  0.8618

roc_auc  :  0.9388

The score was calculated using sklearn.metrics.
