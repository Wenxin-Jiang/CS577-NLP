Pretraining KoLD Dataset with pretrained "koelectra-v3" model.

dataset : https://github.com/boychaboy/KOLD

pretrained_model : https://huggingface.co/monologg/koelectra-base-v3-discriminator

So you should use tokenizer with "koelectra-base-v3-discriminator".

label maps are like
>
    {0: "not_hate_speech", 1: "hate_speech"}