---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: NLP-CIC-WFU_SocialDisNER_fine_tuned_NER_EHR_Spanish_model_Mulitlingual_BERT_v2
  results: []
  
widget:
- text: "Desperté del coma con una inquietud espiritual, que me llevó a mirar al cielo y a encontrar la paz, entrevista a Piki Pfaff https://t.co/JgXnDrXjLN https://t.co/95eVVQOfZo"
- text: "Efectividad y seguridad a largo plazo de la implantación de un stent microbypass trabecular en la cirugía de cataratas: 5 años de resultados https://t.co/tO71HYeCLh https://t.co/mnMGhMNtwx"
- text: "Tuitea con #gotasdesolidaridad y brindemos nuestro apoyo a los pacientes y familiares en el cáncer de mamá @Solan_de_Cabras Uniros a compartirlo @azuchristeamo y @luismi12c https://t.co/TgQizz2kpT"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLP-CIC-WFU_SocialDisNER_fine_tuned_NER_EHR_Spanish_model_Mulitlingual_BERT_v2

This model is a fine-tuned version of [ajtamayoh/NER_EHR_Spanish_model_Mulitlingual_BERT](https://huggingface.co/ajtamayoh/NER_EHR_Spanish_model_Mulitlingual_BERT) on the dataset provided by SocialDisNER shared task, it is available at: https://temu.bsc.es/socialdisner/category/data/.

It achieves the following results on the evaluation set:
- Loss: 0.1483
- Precision: 0.8699
- Recall: 0.8722
- F1: 0.8711
- Accuracy: 0.9771

## Model description

For a complete description of our system, please go to: https://aclanthology.org/2022.smm4h-1.6.pdf

## Training and evaluation data

Dataset provided by SocialDisNER shared task, it is available at: https://temu.bsc.es/socialdisner/category/data/.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 467  | 0.0851          | 0.8415    | 0.8209 | 0.8310 | 0.9720   |
| 0.1011        | 2.0   | 934  | 0.1034          | 0.8681    | 0.8464 | 0.8571 | 0.9744   |
| 0.0537        | 3.0   | 1401 | 0.1094          | 0.8527    | 0.8608 | 0.8568 | 0.9753   |
| 0.0335        | 4.0   | 1868 | 0.1239          | 0.8617    | 0.8603 | 0.8610 | 0.9751   |
| 0.0185        | 5.0   | 2335 | 0.1192          | 0.8689    | 0.8627 | 0.8658 | 0.9756   |
| 0.0112        | 6.0   | 2802 | 0.1426          | 0.8672    | 0.8663 | 0.8667 | 0.9765   |
| 0.0067        | 7.0   | 3269 | 0.1483          | 0.8699    | 0.8722 | 0.8711 | 0.9771   |


### How to cite this work:

Tamayo, A., Gelbukh, A., & Burgos, D. A. (2022, October). Nlp-cic-wfu at socialdisner: Disease mention extraction in spanish tweets using transfer learning and search by propagation. In Proceedings of The Seventh Workshop on Social Media Mining for Health Applications, Workshop & Shared Task (pp. 19-22).

@inproceedings{tamayo2022nlp,
  title={Nlp-cic-wfu at socialdisner: Disease mention extraction in spanish tweets using transfer learning and search by propagation},
  author={Tamayo, Antonio and Gelbukh, Alexander and Burgos, Diego A},
  booktitle={Proceedings of The Seventh Workshop on Social Media Mining for Health Applications, Workshop \& Shared Task},
  pages={19--22},
  year={2022}
}

### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
