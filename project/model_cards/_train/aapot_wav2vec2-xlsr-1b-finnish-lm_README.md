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
- name: wav2vec2-xlsr-1b-finnish-lm
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
      value: 5.65
    - name: Test CER
      type: cer
      value: 1.2
---

# Wav2Vec2 XLS-R for Finnish ASR

This acoustic model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) for Finnish ASR. The model has been fine-tuned with 259.57 hours of Finnish transcribed speech data. Wav2Vec2 XLS-R was introduced in
[this paper](https://arxiv.org/abs/2111.09296) and first released at [this page](https://github.com/pytorch/fairseq/tree/main/examples/wav2vec#wav2vec-20).

This repository also includes Finnish KenLM language model used in the decoding phase with the acoustic model.

**Note**: this model is exactly the same as the [Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm](https://huggingface.co/Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm) model so this model has just been copied/moved to the `Finnish-NLP` Hugging Face organization.

**Note**: there is a better V2 version of this model which has been fine-tuned longer with 16 hours of more data: [Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2](https://huggingface.co/Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2)

## Model description

Wav2Vec2 XLS-R is Facebook AI's large-scale multilingual pretrained model for speech. It is pretrained on 436k hours of unlabeled speech, including VoxPopuli, MLS, CommonVoice, BABEL, and VoxLingua107. It uses the wav2vec 2.0 objective, in 128 languages.

You can read more about the pretrained model from [this blog](https://ai.facebook.com/blog/xls-r-self-supervised-speech-processing-for-128-languages) and [this paper](https://arxiv.org/abs/2111.09296).

This model is fine-tuned version of the pretrained model (1 billion parameter variant) for Finnish ASR.

## Intended uses & limitations

You can use this model for Finnish ASR (speech-to-text) task. 

### How to use

Check the [run-finnish-asr-models.ipynb](https://huggingface.co/aapot/wav2vec2-xlsr-1b-finnish-lm/blob/main/run-finnish-asr-models.ipynb) notebook in this repository for an detailed example on how to use this model.

### Limitations and bias

This model was fine-tuned with audio samples which maximum length was 20 seconds so this model most likely works the best for quite short audios of similar length. However, you can try this model with a lot longer audios too and see how it works. If you encounter out of memory errors with very long audio files you can use the audio chunking method introduced in [this blog post](https://huggingface.co/blog/asr-chunking).

A vast majority of the data used for fine-tuning was from the Finnish Parliament dataset so this model may not generalize so well to very different domains like common daily spoken Finnish with dialects etc. In addition, audios of the datasets tend to be adult male dominated so this model may not work as well for speeches of children and women, for example.

The Finnish KenLM language model used in the decoding phase has been trained with text data from the audio transcriptions. Thus, the decoder's language model may not generalize to very different language, for example to spoken daily language with dialects. It may be beneficial to train your own KenLM language model for your domain language and use that in the decoding.

## Training data

This model was fine-tuned with 259.57 hours of Finnish transcribed speech data from following datasets:

| Dataset                                                                                                                           | Hours    | % of total hours |
|:----------------------------------------------------------------------------------------------------------------------------------|:--------:|:----------------:|
| [Common Voice 7.0 Finnish train + evaluation + other splits](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0) | 9.70 h   | 3.74 %           |
| [Finnish parliament session 2](https://b2share.eudat.eu/records/4df422d631544ce682d6af1d4714b2d4)                                 | 0.24 h   | 0.09 %           |
| [VoxPopuli Finnish](https://github.com/facebookresearch/voxpopuli)                                                                | 5.94 h   | 2.29 %           |
| [CSS10 Finnish](https://github.com/kyubyong/css10)                                                                                | 10.32 h  | 3.98 %           |
| [Aalto Finnish Parliament ASR Corpus](http://urn.fi/urn:nbn:fi:lb-2021051903)                                                     | 228.00 h | 87.84 %          |
| [Finnish Broadcast Corpus](http://urn.fi/urn:nbn:fi:lb-2016042502)                                                                | 5.37 h   | 2.07 %           |

Datasets were filtered to include maximum length of 20 seconds long audio samples.

## Training procedure

This model was trained during [Robust Speech Challenge Event](https://discuss.huggingface.co/t/open-to-the-community-robust-speech-recognition-challenge/13614) organized by Hugging Face. Training was done on a Tesla V100 GPU, sponsored by OVHcloud.

Training script was provided by Hugging Face and it is available [here](https://github.com/huggingface/transformers/blob/main/examples/research_projects/robust-speech-event/run_speech_recognition_ctc_bnb.py). We only modified its data loading for our custom datasets.

For the KenLM language model training, we followed the [blog post tutorial](https://huggingface.co/blog/wav2vec2-with-ngram) provided by Hugging Face. Training data for the 5-gram KenLM were text transcriptions of the audio training data.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: [8-bit Adam](https://github.com/facebookresearch/bitsandbytes) with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5
- mixed_precision_training: Native AMP

The pretrained `facebook/wav2vec2-xls-r-1b` model was initialized with following hyperparameters:
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
| 0.968         | 0.18  | 500   | 0.4870          | 0.4720 |
| 0.6557        | 0.36  | 1000  | 0.2450          | 0.2931 |
| 0.647         | 0.54  | 1500  | 0.1818          | 0.2255 |
| 0.5297        | 0.72  | 2000  | 0.1698          | 0.2354 |
| 0.5802        | 0.9   | 2500  | 0.1581          | 0.2355 |
| 0.6351        | 1.07  | 3000  | 0.1689          | 0.2336 |
| 0.4626        | 1.25  | 3500  | 0.1719          | 0.3099 |
| 0.4526        | 1.43  | 4000  | 0.1434          | 0.2069 |
| 0.4692        | 1.61  | 4500  | 0.1645          | 0.2192 |
| 0.4584        | 1.79  | 5000  | 0.1483          | 0.1987 |
| 0.4234        | 1.97  | 5500  | 0.1499          | 0.2178 |
| 0.4243        | 2.15  | 6000  | 0.1345          | 0.2070 |
| 0.4108        | 2.33  | 6500  | 0.1383          | 0.1850 |
| 0.4048        | 2.51  | 7000  | 0.1338          | 0.1811 |
| 0.4085        | 2.69  | 7500  | 0.1290          | 0.1780 |
| 0.4026        | 2.87  | 8000  | 0.1239          | 0.1650 |
| 0.4033        | 3.04  | 8500  | 0.1346          | 0.1657 |
| 0.3986        | 3.22  | 9000  | 0.1310          | 0.1850 |
| 0.3867        | 3.4   | 9500  | 0.1273          | 0.1741 |
| 0.3658        | 3.58  | 10000 | 0.1219          | 0.1672 |
| 0.382         | 3.76  | 10500 | 0.1306          | 0.1698 |
| 0.3847        | 3.94  | 11000 | 0.1230          | 0.1577 |
| 0.3691        | 4.12  | 11500 | 0.1310          | 0.1615 |
| 0.3593        | 4.3   | 12000 | 0.1296          | 0.1622 |
| 0.3619        | 4.48  | 12500 | 0.1285          | 0.1601 |
| 0.3361        | 4.66  | 13000 | 0.1261          | 0.1569 |
| 0.3603        | 4.84  | 13500 | 0.1235          | 0.1533 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

## Evaluation results

Evaluation was done with the [Common Voice 7.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0).

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id aapot/wav2vec2-xlsr-1b-finnish-lm --dataset mozilla-foundation/common_voice_7_0 --config fi --split test
```

This model (the second row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models:

|                                         | WER (with LM) | WER (without LM) | CER (with LM) | CER (without LM) |
|-----------------------------------------|---------------|------------------|---------------|------------------|
|aapot/wav2vec2-xlsr-1b-finnish-lm-v2     |**4.09**       |**9.73**          |**0.88**       |**1.65**          |
|aapot/wav2vec2-xlsr-1b-finnish-lm        |5.65           |13.11             |1.20           |2.23              |
|aapot/wav2vec2-xlsr-300m-finnish-lm      |8.16           |17.92             |1.97           |3.36              |

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗