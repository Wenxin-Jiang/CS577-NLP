 ---
inference: false
language: id
---

# IndoConvBERT Base Model

IndoConvBERT is a ConvBERT model pretrained on Indo4B.

## Pretraining details

We follow a different training procedure: instead of using a two-phase approach, that pre-trains the model for 90% with 128 sequence length and 10% with 512 sequence length, we pre-train the model with 512 sequence length for 1M steps on a v3-8 TPU.

The current version of the model is trained on Indo4B and small Twitter dump.

## Acknowledgement

Big thanks to TFRC (TensorFlow Research Cloud) for providing free TPU.
