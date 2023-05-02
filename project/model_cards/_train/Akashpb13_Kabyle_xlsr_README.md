---
language:
- kab
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- sw
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/Kabyle_xlsr
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: kab
    metrics:
    - name: Test WER
      type: wer
      value: 0.3188425282720088
    - name: Test CER
      type: cer
      value: 0.09443079928558358
---

# Akashpb13/Kabyle_xlsr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - hu dataset.
It achieves the following results on the evaluation set (which is 10 percent of train data set merged with dev datasets):
- Loss: 0.159032
- Wer: 0.187934
## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice Kabyle train.tsv. Only 50,000 records were sampled randomly and trained due to huge size of dataset.
Only those points were considered where upvotes were greater than downvotes and duplicates were removed after concatenation of all the datasets given in common voice 7.0

## Training procedure
For creating the training dataset, all possible datasets were appended and 90-10 split was used. 

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 0.000096
- train_batch_size: 8
- seed: 13
- gradient_accumulation_steps: 4
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP


### Training results
| Step  | Training Loss | Validation Loss | Wer      |
|-------|---------------|-----------------|----------|
| 500   | 7.199800      | 3.130564        | 1.000000 |
| 1000  | 1.570200      | 0.718097        | 0.734682 |
| 1500  | 0.850800      | 0.524227        | 0.640532 |
| 2000  | 0.712200      | 0.468694        | 0.603454 |
| 2500  | 0.651200      | 0.413833        | 0.573025 |
| 3000  | 0.603100      | 0.403680        | 0.552847 |
| 3500  | 0.553300      | 0.372638        | 0.541719 |
| 4000  | 0.537200      | 0.353759        | 0.531191 |
| 4500  | 0.506300      | 0.359109        | 0.519601 |
| 5000  | 0.479600      | 0.343937        | 0.511336 |
| 5500  | 0.479800      | 0.338214        | 0.503948 |
| 6000  | 0.449500      | 0.332600        | 0.495221 |
| 6500  | 0.439200      | 0.323905        | 0.492635 |
| 7000  | 0.434900      | 0.310417        | 0.484555 |
| 7500  | 0.403200      | 0.311247        | 0.483262 |
| 8000  | 0.401500      | 0.295637        | 0.476566 |
| 8500  | 0.397000      | 0.301321        | 0.471672 |
| 9000  | 0.371600      | 0.295639        | 0.468440 |
| 9500  | 0.370700      | 0.294039        | 0.468902 |
| 10000 | 0.364900      | 0.291195        | 0.468440 |
| 10500 | 0.348300      | 0.284898        | 0.461098 |
| 11000 | 0.350100      | 0.281764        | 0.459805 |
| 11500 | 0.336900      | 0.291022        | 0.461606 |
| 12000 | 0.330700      | 0.280467        | 0.455234 |
| 12500 | 0.322500      | 0.271714        | 0.452694 |
| 13000 | 0.307400      | 0.289519        | 0.455465 |
| 13500 | 0.309300      | 0.281922        | 0.451217 |
| 14000 | 0.304800      | 0.271514        | 0.452186 |
| 14500 | 0.288100      | 0.286801        | 0.446830 |
| 15000 | 0.293200      | 0.276309        | 0.445399 |
| 15500 | 0.289800      | 0.287188        | 0.446230 |
| 16000 | 0.274800      | 0.286406        | 0.441243 |
| 16500 | 0.271700      | 0.284754        | 0.441520 |
| 17000 | 0.262500      | 0.275431        | 0.442167 |
| 17500 | 0.255500      | 0.276575        | 0.439858 |
| 18000 | 0.260200      | 0.269911        | 0.435425 |
| 18500 | 0.250600      | 0.270519        | 0.434686 |
| 19000 | 0.243300      | 0.267655        | 0.437826 |
| 19500 | 0.240600      | 0.277109        | 0.431731 |
| 20000 | 0.237200      | 0.266622        | 0.433994 |
| 20500 | 0.231300      | 0.273015        | 0.428868 |
| 21000 | 0.227200      | 0.263024        | 0.430161 |
| 21500 | 0.220400      | 0.272880        | 0.429607 |
| 22000 | 0.218600      | 0.272340        | 0.426883 |
| 22500 | 0.213100      | 0.277066        | 0.428407 |
| 23000 | 0.205000      | 0.278404        | 0.424020 |
| 23500 | 0.200900      | 0.270877        | 0.418987 |
| 24000 | 0.199000      | 0.289120        | 0.425821 |
| 24500 | 0.196100      | 0.275831        | 0.424066 |
| 25000 | 0.191100      | 0.282822        | 0.421850 |
| 25500 | 0.190100      | 0.275820        | 0.418248 |
| 26000 | 0.178800      | 0.279208        | 0.419125 |
| 26500 | 0.183100      | 0.271464        | 0.419218 |
| 27000 | 0.177400      | 0.280869        | 0.419680 |
| 27500 | 0.171800      | 0.279593        | 0.414924 |
| 28000 | 0.172900      | 0.276949        | 0.417648 |
| 28500 | 0.164900      | 0.283491        | 0.417786 |
| 29000 | 0.164800      | 0.283122        | 0.416078 |
| 29500 | 0.165500      | 0.281969        | 0.415801 |
| 30000 | 0.163800      | 0.283319        | 0.412753 |
| 30500 | 0.153500      | 0.285702        | 0.414046 |
| 31000 | 0.156500      | 0.285041        | 0.412615 |
| 31500 | 0.150900      | 0.284336        | 0.413723 |
| 32000 | 0.151800      | 0.285922        | 0.412292 |
| 32500 | 0.149200      | 0.289461        | 0.412153 |
| 33000 | 0.145400      | 0.291322        | 0.409567 |
| 33500 | 0.145600      | 0.294361        | 0.409614 |
| 34000 | 0.144200      | 0.290686        | 0.409059 |
| 34500 | 0.143400      | 0.289474        | 0.409844 |
| 35000 | 0.143500      | 0.290340        | 0.408367 |
| 35500 | 0.143200      | 0.289581        | 0.407351 |
| 36000 | 0.138400      | 0.292782        | 0.408736 |
| 36500 | 0.137900      | 0.289108        | 0.408044 |
| 37000 | 0.138200      | 0.292127        | 0.407166 |
| 37500 | 0.134600      | 0.291797        | 0.408413 |
| 38000 | 0.139800      | 0.290056        | 0.408090 |
| 38500 | 0.136500      | 0.291198        | 0.408090 |
| 39000 | 0.137700      | 0.289696        | 0.408044 |


### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.3
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/Kabyle_xlsr --dataset mozilla-foundation/common_voice_8_0 --config kab --split test
```

