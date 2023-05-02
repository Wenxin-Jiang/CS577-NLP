---
license: apache-2.0
language: fi
metrics:
- wer
- cer
tags:
- automatic-speech-recognition
- fi
- finnish
- generated_from_trainer
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_9_0
model-index:
- name: wav2vec2-base-fi-voxpopuli-v2-finetuned
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 9
      type: mozilla-foundation/common_voice_9_0
      args: fi
    metrics:
    - name: Test WER
      type: wer
      value: 5.93
    - name: Test CER
      type: cer
      value: 1.40
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: FLEURS ASR
      type: google/fleurs
      args: fi_fi
    metrics:
    - name: Test WER
      type: wer
      value: 13.99
    - name: Test CER
      type: cer
      value: 6.07
---

# Wav2Vec2-base-fi-voxpopuli-v2 for Finnish ASR

This acoustic model is a fine-tuned version of [facebook/wav2vec2-base-fi-voxpopuli-v2](https://huggingface.co/facebook/wav2vec2-base-fi-voxpopuli-v2) for Finnish ASR. The model has been fine-tuned with 276.7 hours of Finnish transcribed speech data. Wav2Vec2 was introduced in
[this paper](https://arxiv.org/abs/2006.11477) and first released at [this page](https://github.com/pytorch/fairseq/tree/main/examples/wav2vec#wav2vec-20).

This repository also includes Finnish KenLM language model used in the decoding phase with the acoustic model.

## Model description

[Wav2vec2-base-fi-voxpopuli-v2](https://huggingface.co/facebook/wav2vec2-base-fi-voxpopuli-v2) is Facebook AI's pretrained model for Finnish speech. It is pretrained on 14.2k hours of unlabeled Finnish speech from [VoxPopuli V2 dataset](https://github.com/facebookresearch/voxpopuli/) with the wav2vec 2.0 objective.

This model is fine-tuned version of the pretrained model for Finnish ASR.

## Intended uses & limitations

You can use this model for Finnish ASR (speech-to-text) task. 

### How to use

Check the [run-finnish-asr-models.ipynb](https://huggingface.co/Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned/blob/main/run-finnish-asr-models.ipynb) notebook in this repository for an detailed example on how to use this model.

### Limitations and bias

This model was fine-tuned with audio samples which maximum length was 20 seconds so this model most likely works the best for quite short audios of similar length. However, you can try this model with a lot longer audios too and see how it works. If you encounter out of memory errors with very long audio files you can use the audio chunking method introduced in [this blog post](https://huggingface.co/blog/asr-chunking).

A vast majority of the data used for fine-tuning was from the Finnish Parliament dataset so this model may not generalize so well to very different domains like common daily spoken Finnish with dialects etc. In addition, audios of the datasets tend to be adult male dominated so this model may not work as well for speeches of children and women, for example.

The Finnish KenLM language model used in the decoding phase has been trained with text data from the audio transcriptions and from a subset of Finnish Wikipedia. Thus, the decoder's language model may not generalize to very different language, for example to spoken daily language with dialects (because especially the Wikipedia contains mostly formal Finnish language). It may be beneficial to train your own KenLM language model for your domain language and use that in the decoding.

## Training data

This model was fine-tuned with 276.7 hours of Finnish transcribed speech data from following datasets:

| Dataset                                                                                                                           | Hours    | % of total hours |
|:------------------------------------------------------------------------------------------------------------------------------    |:--------:|:----------------:|
| [Common Voice 9.0 Finnish train + evaluation + other splits](https://huggingface.co/datasets/mozilla-foundation/common_voice_9_0) | 10.80 h  | 3.90 %           |
| [Finnish parliament session 2](https://b2share.eudat.eu/records/4df422d631544ce682d6af1d4714b2d4)                                 | 0.24 h   | 0.09 %           |
| [VoxPopuli Finnish](https://github.com/facebookresearch/voxpopuli)                                                                | 21.97 h  | 7.94 %           |
| [CSS10 Finnish](https://github.com/kyubyong/css10)                                                                                | 10.32 h  | 3.73 %           |
| [Aalto Finnish Parliament ASR Corpus](http://urn.fi/urn:nbn:fi:lb-2021051903)                                                     | 228.00 h | 82.40 %          |
| [Finnish Broadcast Corpus](http://urn.fi/urn:nbn:fi:lb-2016042502)                                                                | 5.37 h   | 1.94 %           |

Datasets were filtered to include maximum length of 20 seconds long audio samples.

## Training procedure

This model was trained on a Tesla V100 GPU, sponsored by Hugging Face & OVHcloud.

Training script was provided by Hugging Face and it is available [here](https://github.com/huggingface/transformers/blob/main/examples/research_projects/robust-speech-event/run_speech_recognition_ctc_bnb.py). We only modified its data loading for our custom datasets.

For the KenLM language model training, we followed the [blog post tutorial](https://huggingface.co/blog/wav2vec2-with-ngram) provided by Hugging Face. Training data for the 5-gram KenLM were text transcriptions of the audio training data and 100k random samples of cleaned [Finnish Wikipedia](https://huggingface.co/datasets/wikipedia) (August 2021) dataset.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-04
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: [8-bit Adam](https://github.com/facebookresearch/bitsandbytes) with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

The pretrained `facebook/wav2vec2-base-fi-voxpopuli-v2` model was initialized with following hyperparameters:
- attention_dropout: 0.094
- hidden_dropout: 0.047
- feat_proj_dropout: 0.04
- mask_time_prob: 0.082
- layerdrop: 0.041
- activation_dropout: 0.055
- ctc_loss_reduction: "mean"

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.575         | 0.33  | 500   | 0.7454          | 0.7048 |
| 0.5838        | 0.66  | 1000  | 0.2377          | 0.2608 |
| 0.5692        | 1.0   | 1500  | 0.2014          | 0.2244 |
| 0.5112        | 1.33  | 2000  | 0.1885          | 0.2013 |
| 0.4857        | 1.66  | 2500  | 0.1881          | 0.2120 |
| 0.4821        | 1.99  | 3000  | 0.1603          | 0.1894 |
| 0.4531        | 2.32  | 3500  | 0.1594          | 0.1865 |
| 0.4411        | 2.65  | 4000  | 0.1641          | 0.1874 |
| 0.4437        | 2.99  | 4500  | 0.1545          | 0.1874 |
| 0.4191        | 3.32  | 5000  | 0.1565          | 0.1770 |
| 0.4158        | 3.65  | 5500  | 0.1696          | 0.1867 |
| 0.4032        | 3.98  | 6000  | 0.1561          | 0.1746 |
| 0.4003        | 4.31  | 6500  | 0.1432          | 0.1749 |
| 0.4059        | 4.64  | 7000  | 0.1390          | 0.1690 |
| 0.4019        | 4.98  | 7500  | 0.1291          | 0.1646 |
| 0.3811        | 5.31  | 8000  | 0.1485          | 0.1755 |
| 0.3955        | 5.64  | 8500  | 0.1351          | 0.1659 |
| 0.3562        | 5.97  | 9000  | 0.1328          | 0.1614 |
| 0.3646        | 6.3   | 9500  | 0.1329          | 0.1584 |
| 0.351         | 6.64  | 10000 | 0.1342          | 0.1554 |
| 0.3408        | 6.97  | 10500 | 0.1422          | 0.1509 |
| 0.3562        | 7.3   | 11000 | 0.1309          | 0.1528 |
| 0.3335        | 7.63  | 11500 | 0.1305          | 0.1506 |
| 0.3491        | 7.96  | 12000 | 0.1365          | 0.1560 |
| 0.3538        | 8.29  | 12500 | 0.1293          | 0.1512 |
| 0.3338        | 8.63  | 13000 | 0.1328          | 0.1511 |
| 0.3509        | 8.96  | 13500 | 0.1304          | 0.1520 |
| 0.3431        | 9.29  | 14000 | 0.1360          | 0.1517 |
| 0.3309        | 9.62  | 14500 | 0.1328          | 0.1514 |
| 0.3252        | 9.95  | 15000 | 0.1316          | 0.1498 |


### Framework versions

- Transformers 4.19.1
- Pytorch 1.11.0+cu102
- Datasets 2.2.1
- Tokenizers 0.11.0

## Evaluation results

Evaluation was done with the [Common Voice 7.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0), [Common Voice 9.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_9_0) and with the [FLEURS ASR Finnish test split](https://huggingface.co/datasets/google/fleurs).

This model's training data includes the training splits of Common Voice 9.0 but most of our previous models include the Common Voice 7.0 so we ran tests for both Common Voice versions. Note: Common Voice doesn't seem to fully preserve the test split as fixed between the dataset versions so it is possible that some of the training examples of Common Voice 9.0 are in the test split of the Common Voice 7.0 and vice versa. Thus, Common Voice test result comparisons are not fully accurate between the models trained with different Common Voice versions but the comparison should still be meaningful enough.

### Common Voice 7.0 testing

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned --dataset mozilla-foundation/common_voice_7_0 --config fi --split test
```

This model (the first row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

|                                                       | Model parameters | WER (with LM) | WER (without LM) | CER (with LM) | CER (without LM) |
|-------------------------------------------------------|------------------|---------------|------------------|---------------|------------------|
|Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned    | 95 million       |5.85           |13.52             |1.35           |2.44              |
|Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish | 300 million      |4.13           |**9.66**          |0.90           |1.66              |
|Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm              | 300 million      |8.16           |17.92             |1.97           |3.36              |
|Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm                | 1000 million     |5.65           |13.11             |1.20           |2.23              |
|Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2             | 1000 million     |**4.09**       |9.73              |**0.88**       |**1.65**          |

### Common Voice 9.0 testing

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned --dataset mozilla-foundation/common_voice_9_0 --config fi --split test
```

This model (the first row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

|                                                       | Model parameters | WER (with LM) | WER (without LM) | CER (with LM) | CER (without LM) |
|-------------------------------------------------------|------------------|---------------|------------------|---------------|------------------|
|Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned    | 95 million       |5.93           |14.08             |1.40           |2.59              |
|Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish | 300 million      |4.13           |9.83              |0.92           |1.71              |
|Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm              | 300 million      |7.42           |16.45             |1.79           |3.07              |
|Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm                | 1000 million     |5.35           |13.00             |1.14           |2.20              |
|Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2             | 1000 million     |**3.72**       |**8.96**          |**0.80**       |**1.52**          |

### FLEURS ASR testing

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned --dataset google/fleurs --config fi_fi --split test
```

This model (the first row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

|                                                       | Model parameters | WER (with LM) | WER (without LM) | CER (with LM) | CER (without LM) |
|-------------------------------------------------------|------------------|---------------|------------------|---------------|------------------|
|Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned    | 95 million       |13.99          |17.16             |6.07           |6.61              |
|Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish | 300 million      |12.44          |**14.63**         |5.77           |6.22              |
|Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm              | 300 million      |17.72          |23.30             |6.78           |7.67              |
|Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm                | 1000 million     |20.34          |16.67             |6.97           |6.35              |
|Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2             | 1000 million     |**12.11**      |14.89             |**5.65**       |**6.06**          |


## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗