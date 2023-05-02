---
language:
- es
tags:
# - summarization  # Example: audio
- seq2seq  # Example: automatic-speech-recognition
- abstractive question answering
datasets:
- IIC/lfqa_es
metrics:
- rouge2
- rouge1
- rougel
- rougelsum

# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: mbart-large-lfqa-es
  results:
  - task: 
      type: question answering # Required. Example: automatic-speech-recognition
      name: abstractive question answering  # Optional. Example: Speech Recognition
    dataset:
      type: IIC/lfqa_es # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: IIC/lfqa_es  # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
      - type: rouge1    # Required. Example: wer
        value: 0.5107  # Required. Example: 20.90
        name: rouge1    # Optional. Example: Test WER
      - type: rouge2
        value: 0.0042
        name: rouge2
      - type: rougeL
        value: 0.5108
        name: rougeL
      - type: rougeLsum
        value: 0.5106
        name: rougeLsum
---

This model is a fine-tuned version of [MBART-large](https://huggingface.co/facebook/mbart-large-cc25), a multilingual text-to-text encoder-decoder transformer. It is trained on [lfqa-spanish](https://huggingface.co/datasets/IIC/lfqa_spanish), an automatically translated dataset, originally created in English in [this repository](https://huggingface.co/datasets/vblagoje/lfqa). For more details about the dataset, check its model card. 

For optimizing the model, we used [Adafactor](https://paperswithcode.com/method/adafactor) optimizer, which is better suited for t5-class models than AdamW (the typically used one). We used linear decay, and the full hyperparameters for this model were:

```json
{
  "learning_rate": 2e-4,
  "num_train_epochs": 4,
  "adam_beta1": 0.9,
  "adam_beta2": 0.999,
  "adam_epsilon": 1e-8,
  "total_train_batch_size": 64,
  "warmup_ratio": 0.06,
}
```

This model is therefore trained to provide long-form answers to open domain questions given certain context paragraphs which can be used to answer that question. Therefore the main task this model can perform is abstractive question answering.

The result it obtains on the validation set of this dataset (it doesn't have a test set), with num_beams = 8 and maximum target sequence length = 360 are:

```json
{"rouge1": 0.5107, "rouge2": 0.0042, "rougeL": 0.5108, "rougeLsum": 0.5106, "gen_len": 201.7371}
```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.