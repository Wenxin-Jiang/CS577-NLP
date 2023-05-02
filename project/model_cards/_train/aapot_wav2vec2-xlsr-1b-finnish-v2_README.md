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
- name: wav2vec2-xlsr-1b-finnish-v2
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
      value: 9.73
    - name: Test CER
      type: cer
      value: 1.65
---

# Wav2Vec2 XLS-R for Finnish ASR

This acoustic model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) for Finnish ASR. The model has been fine-tuned with 275.6 hours of Finnish transcribed speech data. Wav2Vec2 XLS-R was introduced in
[this paper](https://arxiv.org/abs/2111.09296) and first released at [this page](https://github.com/pytorch/fairseq/tree/main/examples/wav2vec#wav2vec-20).

**Note**: there is a version with KenLM language model used in the decoding phase producing better transcriptions: [Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2](https://huggingface.co/Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2)

## Model description

Wav2Vec2 XLS-R is Facebook AI's large-scale multilingual pretrained model for speech. It is pretrained on 436k hours of unlabeled speech, including VoxPopuli, MLS, CommonVoice, BABEL, and VoxLingua107. It uses the wav2vec 2.0 objective, in 128 languages.

You can read more about the pretrained model from [this blog](https://ai.facebook.com/blog/xls-r-self-supervised-speech-processing-for-128-languages) and [this paper](https://arxiv.org/abs/2111.09296).

This model is fine-tuned version of the pretrained model (1 billion parameter variant) for Finnish ASR.

## Intended uses & limitations

You can use this model for Finnish ASR (speech-to-text) task. 

### How to use

Check the [run-finnish-asr-models.ipynb](https://huggingface.co/aapot/wav2vec2-xlsr-1b-finnish-v2/blob/main/run-finnish-asr-models.ipynb) notebook in this repository for an detailed example on how to use this model.

### Limitations and bias

This model was fine-tuned with audio samples which maximum length was 20 seconds so this model most likely works the best for quite short audios of similar length. However, you can try this model with a lot longer audios too and see how it works. If you encounter out of memory errors with very long audio files you can use the audio chunking method introduced in [this blog post](https://huggingface.co/blog/asr-chunking).

A vast majority of the data used for fine-tuning was from the Finnish Parliament dataset so this model may not generalize so well to very different domains like common daily spoken Finnish with dialects etc. In addition, audios of the datasets tend to be adult male dominated so this model may not work as well for speeches of children and women, for example.

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

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: [8-bit Adam](https://github.com/facebookresearch/bitsandbytes) with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
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
| 0.7778        | 0.17  | 500   | 0.2851          | 0.3572 |
| 0.5506        | 0.34  | 1000  | 0.1595          | 0.2130 |
| 0.6569        | 0.5   | 1500  | 0.1458          | 0.2046 |
| 0.5997        | 0.67  | 2000  | 0.1374          | 0.1975 |
| 0.542         | 0.84  | 2500  | 0.1390          | 0.1956 |
| 0.4815        | 1.01  | 3000  | 0.1266          | 0.1813 |
| 0.6982        | 1.17  | 3500  | 0.1441          | 0.1965 |
| 0.4522        | 1.34  | 4000  | 0.1232          | 0.1822 |
| 0.4655        | 1.51  | 4500  | 0.1209          | 0.1702 |
| 0.4069        | 1.68  | 5000  | 0.1149          | 0.1688 |
| 0.4226        | 1.84  | 5500  | 0.1121          | 0.1560 |
| 0.3993        | 2.01  | 6000  | 0.1091          | 0.1557 |
| 0.406         | 2.18  | 6500  | 0.1115          | 0.1553 |
| 0.4098        | 2.35  | 7000  | 0.1144          | 0.1560 |
| 0.3995        | 2.51  | 7500  | 0.1028          | 0.1476 |
| 0.4101        | 2.68  | 8000  | 0.1129          | 0.1511 |
| 0.3636        | 2.85  | 8500  | 0.1025          | 0.1517 |
| 0.3534        | 3.02  | 9000  | 0.1068          | 0.1480 |
| 0.3836        | 3.18  | 9500  | 0.1072          | 0.1459 |
| 0.3531        | 3.35  | 10000 | 0.0928          | 0.1367 |
| 0.3649        | 3.52  | 10500 | 0.1042          | 0.1426 |
| 0.3645        | 3.69  | 11000 | 0.0979          | 0.1433 |
| 0.3685        | 3.85  | 11500 | 0.0947          | 0.1346 |
| 0.3325        | 4.02  | 12000 | 0.0991          | 0.1352 |
| 0.3497        | 4.19  | 12500 | 0.0919          | 0.1358 |
| 0.3303        | 4.36  | 13000 | 0.0888          | 0.1272 |
| 0.3323        | 4.52  | 13500 | 0.0888          | 0.1277 |
| 0.3452        | 4.69  | 14000 | 0.0894          | 0.1279 |
| 0.337         | 4.86  | 14500 | 0.0917          | 0.1289 |
| 0.3114        | 5.03  | 15000 | 0.0942          | 0.1313 |
| 0.3099        | 5.19  | 15500 | 0.0902          | 0.1239 |
| 0.3079        | 5.36  | 16000 | 0.0871          | 0.1256 |
| 0.3293        | 5.53  | 16500 | 0.0861          | 0.1263 |
| 0.3123        | 5.7   | 17000 | 0.0876          | 0.1203 |
| 0.3093        | 5.86  | 17500 | 0.0848          | 0.1226 |
| 0.2903        | 6.03  | 18000 | 0.0914          | 0.1221 |
| 0.297         | 6.2   | 18500 | 0.0841          | 0.1185 |
| 0.2797        | 6.37  | 19000 | 0.0858          | 0.1165 |
| 0.2878        | 6.53  | 19500 | 0.0874          | 0.1161 |
| 0.2974        | 6.7   | 20000 | 0.0835          | 0.1173 |
| 0.3051        | 6.87  | 20500 | 0.0835          | 0.1178 |
| 0.2941        | 7.04  | 21000 | 0.0852          | 0.1155 |
| 0.258         | 7.21  | 21500 | 0.0832          | 0.1132 |
| 0.2778        | 7.37  | 22000 | 0.0829          | 0.1110 |
| 0.2751        | 7.54  | 22500 | 0.0822          | 0.1069 |
| 0.2887        | 7.71  | 23000 | 0.0819          | 0.1103 |
| 0.2509        | 7.88  | 23500 | 0.0787          | 0.1055 |
| 0.2501        | 8.04  | 24000 | 0.0807          | 0.1076 |
| 0.2399        | 8.21  | 24500 | 0.0784          | 0.1052 |
| 0.2539        | 8.38  | 25000 | 0.0772          | 0.1075 |
| 0.248         | 8.55  | 25500 | 0.0772          | 0.1055 |
| 0.2689        | 8.71  | 26000 | 0.0763          | 0.1027 |
| 0.2855        | 8.88  | 26500 | 0.0756          | 0.1035 |
| 0.2421        | 9.05  | 27000 | 0.0771          | 0.0998 |
| 0.2497        | 9.22  | 27500 | 0.0756          | 0.0971 |
| 0.2367        | 9.38  | 28000 | 0.0741          | 0.0974 |
| 0.2473        | 9.55  | 28500 | 0.0739          | 0.0982 |
| 0.2396        | 9.72  | 29000 | 0.0756          | 0.0991 |
| 0.2602        | 9.89  | 29500 | 0.0737          | 0.0975 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

## Evaluation results

Evaluation was done with the [Common Voice 7.0 Finnish test split](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0).

To evaluate this model, run the `eval.py` script in this repository:

```bash
python3 eval.py --model_id aapot/wav2vec2-xlsr-1b-finnish-v2 --dataset mozilla-foundation/common_voice_7_0 --config fi --split test
```

This model (the first row of the table) achieves the following WER (Word Error Rate) and CER (Character Error Rate) results compared to our other models:

|                                         | WER (with LM) | WER (without LM) | CER (with LM) | CER (without LM) |
|-----------------------------------------|---------------|------------------|---------------|------------------|
|aapot/wav2vec2-xlsr-1b-finnish-lm-v2     |**4.09**       |**9.73**          |**0.88**       |**1.65**          |
|aapot/wav2vec2-xlsr-1b-finnish-lm        |5.65           |13.11             |1.20           |2.23              |
|aapot/wav2vec2-xlsr-300m-finnish-lm      |8.16           |17.92             |1.97           |3.36              |

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗