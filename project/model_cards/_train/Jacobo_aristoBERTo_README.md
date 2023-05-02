---
tags:
language:
- grc
model-index:
- name: aristoBERTo
  results: []
widget:
- text: "Πλάτων ὁ Περικτιόνης [MASK] γένος ἀνέφερεν εἰς Σόλωνα."
- text: "ὁ Κριτίας ἀπέβλεψε [MASK] τὴν θύραν."
- text: "πρῶτοι δὲ καὶ οὐνόματα ἱρὰ ἔγνωσαν καὶ [MASK] ἱροὺς ἔλεξαν."

---


# aristoBERTo

aristoBERTo is a transformer model for ancient Greek, a low resource  language. We initialized the pre-training with weights from [GreekBERT](https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1), a Greek version of BERT which was trained on a large corpus of modern Greek (~ 30 GB of texts). We continued the pre-training with an ancient Greek corpus of about 900 MB, which was scrapped from the web and post-processed. Duplicate texts and editorial punctuation were removed. 

Applied to the processing of ancient Greek, aristoBERTo outperforms xlm-roberta-base and mdeberta in most downstream tasks like the labeling of POS, MORPH, DEP and LEMMA. 

aristoBERTo is provided by the [Diogenet project](https://diogenet.ucsd.edu) of the University of California, San Diego. 
 

## Intended uses

This model was created for fine-tuning with spaCy and the ancient Greek Universal Dependency datasets as well as a NER corpus produced by the [Diogenet project](https://diogenet.ucsd.edu). As a fill-mask model, AristoBERTo can also be used in the restoration of damaged Greek papyri, inscriptions, and manuscripts. 


It achieves the following results on the evaluation set:
- Loss: 1.6323

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step    | Validation Loss |
|:-------------:|:-----:|:-------:|:---------------:|
| 1.377         | 20.0  | 3414220 | 1.6314          |


### Framework versions

- Transformers 4.14.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.16.1
- Tokenizers 0.10.3
