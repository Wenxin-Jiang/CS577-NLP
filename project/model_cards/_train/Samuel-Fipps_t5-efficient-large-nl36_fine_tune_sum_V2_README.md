---
language: en
tags:
- summarization
license: mit
model-index:
- name: SamuelAllen123/t5-efficient-large-nl36_fine_tune_sum_V2
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 50.5049
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 25.6469
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 41.7544
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 46.2055
      verified: true
    - name: loss
      type: loss
      value: 1.5158178806304932
      verified: true
    - name: gen_len
      type: gen_len
      value: 24.0342
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 34.4055
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 14.127
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 24.3353
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 31.6582
      verified: true
    - name: loss
      type: loss
      value: 2.4456119537353516
      verified: true
    - name: gen_len
      type: gen_len
      value: 45.928
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: train
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 54.933
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 31.7965
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 47.0057
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 51.2027
      verified: true
    - name: loss
      type: loss
      value: 1.130684494972229
      verified: true
    - name: gen_len
      type: gen_len
      value: 23.7989
      verified: true
---
*NOT SELF REPORTED VALUES FOR THE LEADERBOARD, I HAVE NO CLUE WHY ITS BROKE. CHECK PULL REQUEST*

Use summarization without adding summarize to the start of the string.

Trained on Samsum train split. 

Parameters for training:

no_decay = ["bias", "LayerNorm.weight", "layer_norm.weight"]
optimizer_grouped_parameters = [
    {
        "params": [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
        "weight_decay": 0.0,
    },
    {
        "params": [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)],
        "weight_decay": 0.0,
    },
]

lr = 0.00005
optimizer = torch.optim.RAdam(optimizer_grouped_parameters, lr=lr)

lr_scheduler = get_scheduler(
        name="linear",
        optimizer=optimizer,
        num_warmup_steps=0,
        num_training_steps=50005)

This was only for 10K steps with a batch size of 10

If you want more info, feel free to message me or email me at:
samuelfipps@gmail.com