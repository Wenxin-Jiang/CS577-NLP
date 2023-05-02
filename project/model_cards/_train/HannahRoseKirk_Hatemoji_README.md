---
license: cc-by-4.0
language: 
- en
tags:
- text-classification
- pytorch
- hate-speech-detection
datasets:
- HatemojiBuild
- HatemojiCheck
metrics:
- Accuracy, F1 Score
---

# Hatemoji Model

## Model description

This model is a fine-tuned version of the [DeBERTa base model](https://huggingface.co/microsoft/deberta-base). This model is cased. The model was trained on iterative rounds of adversarial data generation with human-and-model-in-the-loop. In each round, annotators are tasked with tricking the model-in-the-loop with emoji-containing statements that it will misclassify. Between each round, the model is retrained. This is the final model from the iterative process, referred to as R8-T in our paper. The intended task is to classify an emoji-containing statement as either non-hateful (LABEL 0.0) or hateful (LABEL 1.0). 
- **Github Repository:** https://github.com/HannahKirk/Hatemoji
- **HuggingFace Datasets:** [HatemojiBuild](https://huggingface.co/datasets/HannahRoseKirk/HatemojiBuild) & [HatemojiCheck](https://huggingface.co/datasets/HannahRoseKirk/HatemojiCheck)
- **Paper:** https://arxiv.org/abs/2108.05921
- **Point of Contact:** hannah.kirk@oii.ox.ac.uk

## Intended uses & limitations
The intended use of the model is to classify English-language, emoji-containing, short-form text documents as a binary task: non-hateful vs hateful. The model has demonstrated strengths compared to commercial and academic models on classifying emoji-based hate, but is also a strong classifier of text-only hate. Because the model was trained on synthetic, adversarially-generated data, it may have some weaknesses when it comes to empirical emoji-based hate 'in-the-wild'. 

You can interact with this model on [Dynabench](https://dynabench.org/tasks/hs), and find its limitations. We hope to continue improving the model on new adversarial data to better iron out its remaining weaknesses!

## How to use
The model can be used with pipeline:
```python
from transformers import pipeline
classifier = pipeline("text-classification",model='HannahRoseKirk/Hatemoji', return_all_scores=True)
prediction = classifier("I 💜💙💚 emoji 😍", )
print(prediction)
"""
Output
[[{'label': 'LABEL_0', 'score': 0.9999157190322876}, {'label': 'LABEL_1', 'score': 8.425049600191414e-05}]]
"""
```

### Training data
The model was trained on:
* The three rounds of emoji-containing, adversarially-generated texts from [HatemojiBuild](https://huggingface.co/datasets/HannahRoseKirk/HatemojiBuild)
* The four rounds of text-only, adversarially-generated texts from Vidgen et al., (2021). _Learning from the worst: Dynamically generated datasets to improve online hate detection_. Available on [Github](https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset) and explained in their [paper](https://arxiv.org/abs/2012.15761).
* A collection of widely available and publicly accessible datasets from [https://hatespeechdata.com/](hatespeechdata.com)

## Train procedure
The model was trained using HuggingFace's [run glue script](https://github.com/huggingface/transformers/blob/main/examples/pytorch/text-classification/run_glue.py), using the following parameters:
```
python3 transformers/examples/pytorch/text-classification/run_glue.py \
--model_name_or_path microsoft/deberta-base \
--validation_file path_to_data/dev.csv \
--train_file path_to_data/train.csv \
--do_train --do_eval --max_seq_length 512 --learning_rate 2e-5 \
--num_train_epochs 3 --evaluation_strategy epoch \
--load_best_model_at_end --output_dir path_to_outdir/deberta123/ \
--seed 123 \
--cache_dir /.cache/huggingface/transformers/ \
--overwrite_output_dir > ./log_deb 2> ./err_deb
```

We experimented with upsampling the train split of each round to improve performance with increments of [1, 5, 10, 100], with the optimum upsampling taken
forward to all subsequent rounds. The optimal upsampling ratios for R1-R4 (text rounds from Vidgen et al.,) are carried forward. This model is trained on upsampling ratios of `{'R0':1, 'R1':5, 'R2':100, 'R3':1, 'R4':1 , 'R5':100, 'R6':1, 'R7':5}`.

## Variable and metrics
We wished to train a model which could effectively encode information about emoji-based hate, without worsening performance on text-only hate. Thus, we evaluate the model on:
* [HatemojiCheck](https://huggingface.co/datasets/HannahRoseKirk/HatemojiCheck), an evaluation checklist with 7 functionalities of emoji-based hate and contrast sets
* [HateCheck](https://huggingface.co/datasets/Paul/hatecheck), an evaluation checklist contains 29 functional tests for hate speech and contrast sets.
* The held-out tests sets from [HatemojiBuild](https://huggingface.co/datasets/HannahRoseKirk/HatemojiBuild) the three round of adversarially-generated data collection with emoji-containing examples (R5-7). Available on Huuggingface
* The held-out test sets from the four rounds of adversarially-generated data collection with text-only examples (R1-4, from [Vidgen et al.](https://github.com/bvidgen/Dynamically-Generated-Hate-Speech-Dataset))

For the round-specific test sets, we used a weighted F1-score across them to choose the final model in each round. For more details, see our [paper](https://arxiv.org/abs/2108.05921)

## Evaluation results
We compare our model to:
* **P-IA**: the identity attack attribute from Perspective API
* **P-TX**: the toxicity attribute from Perspective API
* **B-D**: A BERT model trained on the [Davidson et al. (2017)](https://github.com/t-davidson/hate-speech-and-offensive-language) dataset
* **B-F**: A BERT model trained on the [Founta et al. (2018)](https://github.com/ENCASEH2020/hatespeech-twitter) dataset

|          | **Emoji Test Sets** |            |                |            | **Text Test Sets** |            |               |            | **All Rounds** |            |
| :------- | :-----------------: | :--------: | :------------: | :--------: | :----------------: | :--------: | :-----------: | :--------: | :------------: | :--------: |
|          | **R5-R7**           |            | **HmojiCheck** |            | **R1-R4**          |            | **HateCheck** |            | **R1-R7**      |            |
|          | **Acc**             | **F1**     | **Acc**        | **F1**     | **Acc**            | **F1**     | **Acc**       | **F1**     | **Acc**        | **F1**     |
| **P-IA** | 0\.508              | 0\.394     | 0\.689         | 0\.754     | 0\.679             | 0\.720     | 0\.765        | 0\.839     | 0\.658         | 0\.689     |
| **P-TX** | 0\.523              | 0\.448     | 0\.650         | 0\.711     | 0\.602             | 0\.659     | 0\.720        | 0\.813     | 0\.592         | 0\.639     |
| **B-D**  | 0\.489              | 0\.270     | 0\.578         | 0\.636     | 0\.589             | 0\.607     | 0\.632        | 0\.738     | 0\.591         | 0\.586     |
| **B-F**  | 0\.496              | 0\.322     | 0\.552         | 0\.605     | 0\.562             | 0\.562     | 0\.602        | 0\.694     | 0\.557         | 0\.532     |
| **Hatemoji** | **0\.744**          | **0\.755** | **0\.871**     | **0\.904** | **0\.827**         | **0\.844** | **0\.966**    | **0\.975** | **0\.814**     | **0\.829** |

For full discussion of the model results, see our [paper](https://arxiv.org/abs/2108.05921).

A recent [paper](https://arxiv.org/pdf/2202.11176.pdf) by Lees et al., (2022) _A New Generation of Perspective API:Efficient Multilingual Character-level Transformers_ beats this model on the HatemojiCheck benchmark. 