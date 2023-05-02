---
license: mit
tags:
- generated_from_trainer
datasets:
- source_data_nlp
widget:
- text: "Confocal images of Bmm-GFP (green) in 3rd instar larval fat bodies of different genotypes. DAPI (blue) stains nuclei. Scale bar represents 25 µm. (A) Knocking down CSN2 or overexpressing RDH/CG2064 in animals with DGAT1 overexpression (ppl>DGAT1) decreases the level and lipid droplet localization of Bmm-GFP."
- text: "The GFP intensity along the line across a lipid droplet in (A) was measured by ImageJ.The lipid droplet localization of Bmm-GFP, represented by two peaks, is clearly visible in fat cells from ppl > DGAT1 larvae , but it is lost in fat cells from ppl > DGAT1 larvae with CSN2 RNAi or overexpression of RDH/CG2064. More than 30 lipid droplets of each genotype were measured. One typical image curve is shown for each genotype."
- text: "XPT of siRNA treated DC3. 2R cells after 48 hours of knockdown. Treated cells were fed with the indicated amounts of C8L peptid conjugated to iron oxide beads via a disulfide bond. The cells were then exposed to RF33. 70-Luc Reporter CD8 T cells overnight. Error bars show SD of >3 replicate wells. * p<0.05 for siRNA vs control I-Ab using two-way ANOVA. Representative plot of 3 independent experiments."
metrics:
- precision
- recall
- f1
- name: sd-ner-v2
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: source_data_nlp
      type: source_data_nlp
      args: NER
    metrics:
    - name: Precision
      type: precision
      value: 0.8030010681183889
    - name: Recall
      type: recall
      value: 0.837754771918473
    - name: F1
      type: f1
      value: 0.8200098518700961
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sd-ner-v2

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the source_data_nlp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1551
- Accuracy Score: 0.9513
- Precision: 0.8030
- Recall: 0.8378
- F1: 0.8200

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 256
- seed: 42
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy Score | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:---------:|:------:|:------:|
| 0.1082        | 1.0   | 785  | 0.1550          | 0.9493         | 0.7826    | 0.8402 | 0.8104 |
| 0.073         | 2.0   | 1570 | 0.1551          | 0.9513         | 0.8030    | 0.8378 | 0.8200 |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0a0+bfe5ad2
- Datasets 1.17.0
- Tokenizers 0.12.1
