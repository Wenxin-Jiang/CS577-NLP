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
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-xlsr-300m-finnish-lm
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: fi
    metrics:
    - name: Test WER
      type: wer
      value: 8.16
    - name: Test CER
      type: cer
      value: 1.97
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
      value: 17.72
    - name: Test CER
      type: cer
      value: 6.78
---

# Wav2vec2-xls-r-300m for Finnish ASR

This acoustic model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) for Finnish ASR. The model has been fine-tuned with 275.6 hours of Finnish transcribed speech data. Wav2Vec2 XLS-R was introduced in
[this paper](https://arxiv.org/abs/2111.09296) and first released at [this page](https://github.com/pytorch/fairseq/tree/main/examples/wav2vec#wav2vec-20).

This repository also includes Finnish KenLM language model used in the decoding phase with the acoustic model.

**Note**: this model is exactly the same as the [aapot/wav2vec2-xlsr-300m-finnish-lm](https://huggingface.co/aapot/wav2vec2-xlsr-300m-finnish-lm) model so that model has just been copied/moved to this `Finnish-NLP` Hugging Face organization.

## Model description

Wav2Vec2 XLS-R is Facebook AI's large-scale multilingual pretrained model for speech. It is pretrained on 436k hours of unlabeled speech, including VoxPopuli, MLS, CommonVoice, BABEL, and VoxLingua107. It uses the wav2vec 2.0 objective, in 128 languages.

You can read more about the pretrained model from [this blog](https://ai.facebook.com/blog/xls-r-self-supervised-speech-processing-for-128-languages) and [this paper](https://arxiv.org/abs/2111.09296).

This model is fine-tuned version of the pretrained model (300 million parameter variant) for Finnish ASR.

## Intended uses & limitations

You can use this model for Finnish ASR (speech-to-text) task. 

### How to use

Check the [run-finnish-asr-models.ipynb](https://huggingface.co/Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm/blob/main/run-finnish-asr-models.ipynb) notebook in this repository for an detailed example on how to use this model.

### Limitations and bias

This model was fine-tuned with audio samples which maximum length was 20 seconds so this model most likely works the best for quite short audios of similar length. However, you can try this model with a lot longer audios too and see how it works. If you encounter out of memory errors with very long audio files you can use the audio chunking method introduced in [this blog post](https://huggingface.co/blog/asr-chunking).

A vast majority of the data used for fine-tuning was from the Finnish Parliament dataset so this model may not generalize so well to very different domains like common daily spoken Finnish with dialects etc. In addition, audios of the datasets tend to be adult male dominated so this model may not work as well for speeches of children and women, for example.

The Finnish KenLM language model used in the decoding phase has been trained with text data from the audio transcriptions and from a subset of Finnish Wikipedia. Thus, the decoder's language model may not generalize to very different language, for example to spoken daily language with dialects (because especially the Wikipedia contains mostly formal Finnish language). It may be beneficial to train your own KenLM language model for your domain language and use that in the decoding.

## Training data

This model was fine-tuned with 275.6 hours of Finnish transcribed speech data from following datasets:

| Dataset                                                                                                                           | Hours    | % of total hours |
|:------------------------------------------------------------------------------------------------------------------------------    |:--------:|:----------------:|
| [Common Voice 7.0 Finnish train + evaluation + other splits](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0) | 9.70 h   | 3.52 %           |
| [Finnish parliament session 2](https://b2share.eudat.eu/records/4df422d631544ce682d6af1d4714b2d4)                                 | 0.24 h   | 0.09 %           |
| [VoxPopuli Finnish](https://github.com/facebookresearch/voxpopuli)                                                                | 21.97 h  | 7.97 %           |
| [CSS10 Finnish](https://github.com/kyubyong/css10)                                                                                | 10.32 h  | 3.74 %           |
| [Aalto Finnish Parliament ASR Corpus](http://urn.fi/urn:nbn:fi:lb-2021051903)                                                     | 228.00 h | 82.73 %          |
| [Finnish Broadcast Corpus](http://urn.fi/urn:nbn:fi:lb-2016042502)                                                                | 5.37 h   | 1.95 %           |

Datasets were filtered to include maximum length of 20 seconds long audio samples.

## Training procedure

This model was trained during [Robust Speech Challenge Event](https://discuss.huggingface.co/t/open-to-the-community-robust-speech-recognition-challenge/13614) organized by Hugging Face. Training was done on a Tesla V100 GPU, sponsored by OVHcloud.

Training script was provided by Hugging Face and it is available [here](https://github.com/huggingface/transformers/blob/main/examples/research_projects/robust-speech-event/run_speech_recognition_ctc_bnb.py). We only modified its data loading for our custom datasets.

For the KenLM language model training, we followed the [blog post tutorial](https://huggingface.co/blog/wav2vec2-with-ngram) provided by Hugging Face. Training data for the 5-gram KenLM were text transcriptions of the audio training data and 100k random samples of cleaned [Finnish Wikipedia](https://huggingface.co/datasets/wikipedia) (August 2021) dataset.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-04
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: [8-bit Adam](https://github.com/facebookresearch/bitsandbytes) with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

The pretrained `facebook/wav2vec2-xls-r-300m` model was initialized with following hyperparameters:
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
| 0.973         | 0.17  | 500   | 0.5750          | 0.6844 |
| 0.713         | 0.34  | 1000  | 0.3356          | 0.4518 |
| 0.6563        | 0.5   | 1500  | 0.3007          | 0.4039 |
| 0.642         | 0.67  | 2000  | 0.2619          | 0.3674 |
| 0.6203        | 0.84  | 2500  | 0.2488          | 0.3558 |
| 0.6016        | 1.01  | 3000  | 0.2795          | 0.3835 |
| 0.5423        | 1.17  | 3500  | 0.2652          | 0.3310 |
| 0.5639        | 1.34  | 4000  | 0.2479          | 0.3462 |
| 0.586         | 1.51  | 4500  | 0.2409          | 0.3295 |
| 0.5169        | 1.68  | 5000  | 0.2728          | 0.3352 |
| 0.5176        | 1.84  | 5500  | 0.2254          | 0.3149 |
| 0.4983        | 2.01  | 6000  | 0.2169          | 0.3009 |
| 0.4982        | 2.18  | 6500  | 0.2215          | 0.3079 |
| 0.4898        | 2.35  | 7000  | 0.2174          | 0.3023 |
| 0.4922        | 2.51  | 7500  | 0.2217          | 0.3081 |
| 0.5025        | 2.68  | 8000  | 0.2002          | 0.2710 |
| 0.4745        | 2.85  | 8500  | 0.1935          | 0.2783 |
| 0.4377        | 3.02  | 9000  | 0.1859          | 0.2742 |
| 0.4511        | 3.18  | 9500  | 0.2038          | 0.2786 |
| 0.4411        | 3.35  | 10000 | 0.1863          | 0.2651 |
| 0.4501        | 3.52  | 10500 | 0.1948          | 0.2605 |
| 0.4557        | 3.69  | 11000 | 0.1872          | 0.2695 |
| 0.4493        | 3.85  | 11500 | 0.1888          | 0.2632 |
| 0.4047        | 4.02  | 12000 | 0.1818          | 0.2559 |
| 0.4319        | 4.19  | 12500 | 0.1896          | 0.2648 |
| 0.4162        | 4.36  | 13000 | 0.1953          | 0.2595 |
| 0.4046        | 4.52  | 13500 | 0.1864          | 0.2606 |
| 0.4195        | 4.69  | 14000 | 0.1843          | 0.2467 |
| 0.4146        | 4.86  | 14500 | 0.1686          | 0.2450 |
| 0.378         | 5.03  | 15000 | 0.1731          | 0.2401 |
| 0.3792        | 5.19  | 15500 | 0.1676          | 0.2325 |
| 0.3855        | 5.36  | 16000 | 0.1740          | 0.2326 |
| 0.4029        | 5.53  | 16500 | 0.1674          | 0.2345 |
| 0.386         | 5.7   | 17000 | 0.1735          | 0.2280 |
| 0.3811        | 5.86  | 17500 | 0.1692          | 0.2258 |
| 0.3607        | 6.03  | 18000 | 0.1797          | 0.2279 |
| 0.3604        | 6.2   | 18500 | 0.1651          | 0.2206 |
| 0.3362        | 6.37  | 19000 | 0.1627          | 0.2199 |
| 0.3611        | 6.53  | 19500 | 0.1652          | 0.2172 |
| 0.3671        | 6.7   | 20000 | 0.1564          | 0.2140 |
| 0.3769        | 6.87  | 20500 | 0.1525          | 0.2101 |
| 0.3539        | 7.04  | 21000 | 0.1639          | 0.2096 |
| 0.3225        | 7.21  | 21500 | 0.1611          | 0.2087 |
| 0.3323        | 7.37  | 22000 | 0.1633          | 0.2008 |
| 0.3327        | 7.54  | 22500 | 0.1692          | 0.1975 |
| 0.3456        | 7.71  | 23000 | 0.1555          | 0.1991 |
| 0.3058        | 7.88  | 23500 | 0.1590          | 0.1959 |
| 0.3034        | 8.04  | 24000 | 0.1531          | 0.1973 |
| 0.2925        | 8.21  | 24500 | 0.1583          | 0.1978 |
| 0.2967        | 8.38  | 25000 | 0.1546          | 0.1906 |
| 0.2974        | 8.55  | 25500 | 0.1540          | 0.1869 |
| 0.3131        | 8.71  | 26000 | 0.1534          | 0.1850 |
| 0.3306        | 8.88  | 26500 | 0.1482          | 0.1844 |
| 0.2842        | 9.05  | 27000 | 0.1490          | 0.1854 |
| 0.2879        | 9.22  | 27500 | 0.1463          | 0.1799 |
| 0.27          | 9.38  | 28000 | 0.1454          | 0.1798 |
| 0.2874        | 9.55  | 28500 | 0.1504          | 0.1787 |
| 0.2757        | 9.72  | 29000 | 0.1512          | 0.1784 |
| 0.3017        | 9.89  | 29500 | 0.1484          | 0.1800 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

## Evaluation results

Evaluation was done with the [Common Voice 7.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0), [Common Voice 9.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_9_0) and with the [FLEURS ASR Finnish test split](https://huggingface.co/datasets/google/fleurs). 

This model's training data includes the training splits of Common Voice 7.0 but our newer `Finnish-NLP/wav2vec2-base-fi-voxpopuli-v2-finetuned` and `Finnish-NLP/wav2vec2-large-uralic-voxpopuli-v2-finnish` models include the Common Voice 9.0 so we ran tests for both Common Voice versions. Note: Common Voice doesn't seem to fully preserve the test split as fixed between the dataset versions so it is possible that some of the training examples of Common Voice 9.0 are in the test split of the Common Voice 7.0 and vice versa. Thus, Common Voice test result comparisons are not fully accurate between the models trained with different Common Voice versions but the comparison should still be meaningful enough.

### Common Voice 7.0 testing

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm  --dataset mozilla-foundation/common_voice_7_0 --config fi --split test
```

This model (the third row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

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
python3 eval.py --model_id Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm  --dataset mozilla-foundation/common_voice_9_0 --config fi --split test
```

This model (the third row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

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
python3 eval.py --model_id Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm --dataset google/fleurs --config fi_fi --split test
```

This model (the third row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models and their parameter counts:

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