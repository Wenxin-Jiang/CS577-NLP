---
language: es
license: mit

widget:
- text: "y porqué es lo que hay que hacer con los menas y con los adultos también!!!! NO a los inmigrantes ilegales!!!!"
---

### Description
This model is a fine-tuned version of [BETO (spanish bert)](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) that has been trained on the *Datathon Against Racism* dataset (2022)

We performed several experiments that will be described in the upcoming paper "Estimating Ground Truth in a Low-labelled Data Regime:A Study of Racism Detection in Spanish" (NEATClasS 2022)
We applied 6 different methods ground-truth estimations, and for each one we performed 4 epochs of fine-tuning. The result is made of 24 models:

| method	| epoch 1	| epoch 3	| epoch 3	| epoch 4	|
|---	|---	|---	|---	|---	|
| raw-label	| [raw-label-epoch-1](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-1)	| [raw-label-epoch-2](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-2)	| [raw-label-epoch-3](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-3)	| [raw-label-epoch-4](https://huggingface.co/MartinoMensio/racism-models-raw-label-epoch-4)	|
| m-vote-strict	| [m-vote-strict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-1)	| [m-vote-strict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-2)	| [m-vote-strict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-3)	| [m-vote-strict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-m-vote-strict-epoch-4)	|
| m-vote-nonstrict	| [m-vote-nonstrict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-1)	| [m-vote-nonstrict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-2)	| [m-vote-nonstrict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-3)	| [m-vote-nonstrict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-m-vote-nonstrict-epoch-4)	|
| regression-w-m-vote	| [regression-w-m-vote-epoch-1](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-1)	| [regression-w-m-vote-epoch-2](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-2)	| [regression-w-m-vote-epoch-3](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-3)	| [regression-w-m-vote-epoch-4](https://huggingface.co/MartinoMensio/racism-models-regression-w-m-vote-epoch-4)	|
| w-m-vote-strict	| [w-m-vote-strict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-1)	| [w-m-vote-strict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-2)	| [w-m-vote-strict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-3)	| [w-m-vote-strict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-strict-epoch-4)	|
| w-m-vote-nonstrict	| [w-m-vote-nonstrict-epoch-1](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-1)	| [w-m-vote-nonstrict-epoch-2](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-2)	| [w-m-vote-nonstrict-epoch-3](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-3)	| [w-m-vote-nonstrict-epoch-4](https://huggingface.co/MartinoMensio/racism-models-w-m-vote-nonstrict-epoch-4)	|


This model is `regression-w-m-vote-epoch-3`

### Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers.pipelines import TextClassificationPipeline

class TextRegressionPipeline(TextClassificationPipeline):
    """
    Class based on the TextClassificationPipeline from transformers.
    The difference is that instead of being based on a classifier, it is based on a regressor.
    You can specify the regression threshold when you call the pipeline or when you instantiate the pipeline.
    """
    def __init__(self, **kwargs):
        """
        Builds a new Pipeline based on regression.
        regression_threshold: Optional(float). If None, the pipeline will simply output the score. If set to a specific value, the output will be both the score and the label.
        """
        self.regression_threshold = kwargs.pop("regression_threshold", None)
        super().__init__(**kwargs)
    def __call__(self, *args, **kwargs):
        """
        You can also specify the regression threshold when you call the pipeline.
        regression_threshold: Optional(float). If None, the pipeline will simply output the score. If set to a specific value, the output will be both the score and the label.
        """
        self.regression_threshold_call = kwargs.pop("regression_threshold", None)
        result = super().__call__(*args, **kwargs)
        return result
    def postprocess(self, model_outputs, function_to_apply=None, return_all_scores=False):
        outputs = model_outputs["logits"][0]
        outputs = outputs.numpy()
        scores = outputs
        score = scores[0]
        regression_threshold = self.regression_threshold
        # override the specific threshold if it is specified in the call
        if self.regression_threshold_call:
            regression_threshold = self.regression_threshold_call
        if regression_threshold:
            return {"label": 'racist' if score > regression_threshold else 'non-racist', "score": score}
        else:
            return {"score": score}



model_name = 'regression-w-m-vote-epoch-3'
tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")
full_model_path = f'MartinoMensio/racism-models-{model_name}'
model = AutoModelForSequenceClassification.from_pretrained(full_model_path)

pipe = TextRegressionPipeline(model=model, tokenizer=tokenizer)

texts = [
    'y porqué es lo que hay que hacer con los menas y con los adultos también!!!! NO a los inmigrantes ilegales!!!!',
    'Es que los judíos controlan el mundo'
]
# just get the score of regression
print(pipe(texts))
# [{'score': 0.7393736}, {'score': 0.44301373}]

# or also specify a threshold to cut racist/non-racist
print(pipe(texts, regression_threshold=0.9))
# [{'label': 'non-racist', 'score': 0.7393736}, {'label': 'non-racist', 'score': 0.44301373}]
```

For more details, see https://github.com/preyero/neatclass22
