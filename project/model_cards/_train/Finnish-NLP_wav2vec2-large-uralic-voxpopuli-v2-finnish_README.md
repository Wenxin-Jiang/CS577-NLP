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
- name: wav2vec2-large-uralic-voxpopuli-v2-finnish
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
      value: 4.13
    - name: Test CER
      type: cer
      value: 0.92
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
      value: 12.44
    - name: Test CER
      type: cer
      value: 5.77
---

# Wav2vec2-large-uralic-voxpopuli-v2 for Finnish ASR

This acoustic model is a fine-tuned version of [facebook/wav2vec2-large-uralic-voxpopuli-v2](https://huggingface.co/facebook/wav2vec2-large-uralic-voxpopuli-v2) for Finnish ASR. The model has been fine-tuned with 276.7 hours of Finnish transcribed speech data. Wav2Vec2 was introduced in
[this paper](https://arxiv.org/abs/2006.11477) and first released at [this page](https://github.com/pytorch/fairseq/tree/main/examples/wav2vec#wav2vec-20).

This repository also includes Finnish KenLM language model used in the decoding phase with the acoustic model.

## Model description

[Wav2vec2-large-uralic-voxpopuli-v2](https://huggingface.co/facebook/wav2vec2-large-uralic-voxpopuli-v2) is Facebook AI's pretrained model for uralic language family (Finnish, Estonian, Hungarian) speech. It is pretrained on 42.5k hours of unlabeled Finnish, Estonian and Hungarian speech from [VoxPopuli V2 dataset](https://github.com/facebookresearch/voxpopuli/) with the wav2vec 2.0 objective.

This model is fine-tuned version of the pretrained model for Finnish ASR.

## Intended uses & limitations

You can use this model for Finnish ASR (speech-to-text) task. 

### How to use

Check the [run-finnish-asr-models.ipynb](https://huggingface.co/Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish/blob/main/run-finnish-asr-models.ipynb) notebook in this repository for an detailed example on how to use this model.

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: [8-bit Adam](https://github.com/facebookresearch/bitsandbytes) with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

The pretrained `facebook/wav2vec2-large-uralic-voxpopuli-v2` model was initialized with following hyperparameters:
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
| 1.9421        | 0.17  | 500   | 0.8633          | 0.8870 |
| 0.572         | 0.33  | 1000  | 0.1650          | 0.1829 |
| 0.5149        | 0.5   | 1500  | 0.1416          | 0.1711 |
| 0.4884        | 0.66  | 2000  | 0.1265          | 0.1605 |
| 0.4729        | 0.83  | 2500  | 0.1205          | 0.1485 |
| 0.4723        | 1.0   | 3000  | 0.1108          | 0.1403 |
| 0.443         | 1.16  | 3500  | 0.1175          | 0.1439 |
| 0.4378        | 1.33  | 4000  | 0.1083          | 0.1482 |
| 0.4313        | 1.49  | 4500  | 0.1110          | 0.1398 |
| 0.4182        | 1.66  | 5000  | 0.1024          | 0.1418 |
| 0.3884        | 1.83  | 5500  | 0.1032          | 0.1395 |
| 0.4034        | 1.99  | 6000  | 0.0985          | 0.1318 |
| 0.3735        | 2.16  | 6500  | 0.1008          | 0.1355 |
| 0.4174        | 2.32  | 7000  | 0.0970          | 0.1361 |
| 0.3581        | 2.49  | 7500  | 0.0968          | 0.1297 |
| 0.3783        | 2.66  | 8000  | 0.0881          | 0.1284 |
| 0.3827        | 2.82  | 8500  | 0.0921          | 0.1352 |
| 0.3651        | 2.99  | 9000  | 0.0861          | 0.1298 |
| 0.3684        | 3.15  | 9500  | 0.0844          | 0.1270 |
| 0.3784        | 3.32  | 10000 | 0.0870          | 0.1248 |
| 0.356         | 3.48  | 10500 | 0.0828          | 0.1214 |
| 0.3524        | 3.65  | 11000 | 0.0878          | 0.1218 |
| 0.3879        | 3.82  | 11500 | 0.0874          | 0.1216 |
| 0.3521        | 3.98  | 12000 | 0.0860          | 0.1210 |
| 0.3527        | 4.15  | 12500 | 0.0818          | 0.1184 |
| 0.3529        | 4.31  | 13000 | 0.0787          | 0.1185 |
| 0.3114        | 4.48  | 13500 | 0.0852          | 0.1202 |
| 0.3495        | 4.65  | 14000 | 0.0807          | 0.1187 |
| 0.34          | 4.81  | 14500 | 0.0796          | 0.1162 |
| 0.3646        | 4.98  | 15000 | 0.0782          | 0.1149 |
| 0.3004        | 5.14  | 15500 | 0.0799          | 0.1142 |
| 0.3167        | 5.31  | 16000 | 0.0847          | 0.1123 |
| 0.3249        | 5.48  | 16500 | 0.0837          | 0.1171 |
| 0.3202        | 5.64  | 17000 | 0.0749          | 0.1109 |
| 0.3104        | 5.81  | 17500 | 0.0798          | 0.1093 |
| 0.3039        | 5.97  | 18000 | 0.0810          | 0.1132 |
| 0.3157        | 6.14  | 18500 | 0.0847          | 0.1156 |
| 0.3133        | 6.31  | 19000 | 0.0833          | 0.1140 |
| 0.3203        | 6.47  | 19500 | 0.0838          | 0.1113 |
| 0.3178        | 6.64  | 20000 | 0.0907          | 0.1141 |
| 0.3182        | 6.8   | 20500 | 0.0938          | 0.1143 |
| 0.3           | 6.97  | 21000 | 0.0854          | 0.1133 |
| 0.3151        | 7.14  | 21500 | 0.0859          | 0.1109 |
| 0.2963        | 7.3   | 22000 | 0.0832          | 0.1122 |
| 0.3099        | 7.47  | 22500 | 0.0865          | 0.1103 |
| 0.322         | 7.63  | 23000 | 0.0833          | 0.1105 |
| 0.3064        | 7.8   | 23500 | 0.0865          | 0.1078 |
| 0.2964        | 7.97  | 24000 | 0.0859          | 0.1096 |
| 0.2869        | 8.13  | 24500 | 0.0872          | 0.1100 |
| 0.315         | 8.3   | 25000 | 0.0869          | 0.1099 |
| 0.3003        | 8.46  | 25500 | 0.0878          | 0.1105 |
| 0.2947        | 8.63  | 26000 | 0.0884          | 0.1084 |
| 0.297         | 8.8   | 26500 | 0.0891          | 0.1102 |
| 0.3049        | 8.96  | 27000 | 0.0863          | 0.1081 |
| 0.2957        | 9.13  | 27500 | 0.0846          | 0.1083 |
| 0.2908        | 9.29  | 28000 | 0.0848          | 0.1059 |
| 0.2955        | 9.46  | 28500 | 0.0846          | 0.1085 |
| 0.2991        | 9.62  | 29000 | 0.0839          | 0.1081 |
| 0.3112        | 9.79  | 29500 | 0.0832          | 0.1071 |
| 0.29          | 9.96  | 30000 | 0.0828          | 0.1075 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu102
- Datasets 2.2.2
- Tokenizers 0.11.0

## Evaluation results

Evaluation was done with the [Common Voice 7.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0), [Common Voice 9.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_9_0) and with the [FLEURS ASR Finnish test split](https://huggingface.co/datasets/google/fleurs).

This model's training data includes the training splits of Common Voice 9.0 but most of our previous models include the Common Voice 7.0 so we ran tests for both Common Voice versions. Note: Common Voice doesn't seem to fully preserve the test split as fixed between the dataset versions so it is possible that some of the training examples of Common Voice 9.0 are in the test split of the Common Voice 7.0 and vice versa. Thus, Common Voice test result comparisons are not fully accurate between the models trained with different Common Voice versions but the comparison should still be meaningful enough.

### Common Voice 7.0 testing

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish --dataset mozilla-foundation/common_voice_7_0 --config fi --split test
```

This model (the second row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

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
python3 eval.py --model_id Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish --dataset mozilla-foundation/common_voice_9_0 --config fi --split test
```

This model (the second row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

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
python3 eval.py --model_id Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish --dataset google/fleurs --config fi_fi --split test
```

This model (the second row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

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