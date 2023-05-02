---
license: cc-by-sa-3.0
language:
- ja
tag:
- emotion-analysis
datasets:
- wrime
widget:
- text: "車のタイヤがパンクしてた。。いたずらの可能性が高いんだって。。"
---

# WRIME-fine-tuned BERT base Japanese

This model is a [Japanese BERT<sub>BASE</sub>](https://huggingface.co/cl-tohoku/bert-base-japanese-v2) fine-tuned on the [WRIME](https://github.com/ids-cv/wrime) dataset. It was trained as part of the paper ["Emotion Analysis of Writers and Readers of Japanese Tweets on Vaccinations"](https://aclanthology.org/2022.wassa-1.10/). Fine-tuning code is available at this [repo](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination).

# Intended uses and limitations

This model can be used to predict intensities scores for eight emotions for writers and readers. Please refer to the `Fine-tuning data` section for the list of emotions.

Because of the regression fine-tuning task, it is possible for the model to infer scores outside of the range of the scores of the fine-tuning data (`score < 0` or `score > 4`).

# Model Architecture, Tokenization, and Pretraining

The Japanese BERT<sub>BASE</sub> fine-tuned was `cl-tohoku/bert-base-japanese-v2`. Please refer to their [model card](https://huggingface.co/cl-tohoku/bert-base-japanese-v2) for details regarding the model architecture, tokenization, pretraining data, and pretraining procedure.

# Fine-tuning data

The model is fine-tuned on [WRIME](https://github.com/ids-cv/wrime), a dataset of Japanese Tweets annotated with writer and reader emotion intensities. We use version 1 of the dataset. Each Tweet is accompanied by a set of writer emotion intensities (from the author of the Tweet) and three sets of reader emotions (from three annotators). The emotions follow Plutchhik's emotions, namely:

* joy
* sadness
* anticipation
* surprise
* anger
* fear
* disgust
* trust

These emotion intensities follow a four-point scale:

| emotion intensity | emotion presence|
|---|---|
| 0 | no |
| 1 | weak |
| 2 | medium |
| 3 | strong |

# Fine-tuning

The BERT is fine-tuned to directly regress the emotion intensities of the writer and the averaged emotions of the readers from each Tweet, meaning there are 16 outputs (8 emotions per writer/reader).

The fine-tuning was inspired by common BERT fine-tuning procedures. The BERT was fine-tuned on WRIME for 3 epochs using the AdamW optimizer with a learning rate of 2e-5, β<sub>1</sub>=0.9, β<sub>2</sub>=0.999, weight decay of 0.01, linear decay, a warmup ratio of 0.01, and a batch size of 32. Training was conducted with an NVIDIA Tesla K80 and finished in 3 hours.

# Evaluation results

Below are the MSEs of the BERT on the test split of WRIME.

| Annotator | Joy | Sadness | Anticipation | Surprise | Anger | Fear | Disgust | Trust | Overall |
|---|---|---|---|---|---|---|---|---|---| 
| Writer | 0.658 | 0.688 | 0.746 | 0.542 | 0.486 | 0.462 | 0.664 | 0.400 | 0.581 |
| Reader | 0.192 | 0.178 | 0.211 | 0.139 | 0.032 | 0.147 | 0.123 | 0.029 | 0.131 |
| Both | 0.425 | 0.433 | 0.479 | 0.341 | 0.259 | 0.304 | 0.394 | 0.214 | 0.356 |