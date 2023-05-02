
tags:
- automatic-speech-recognition
- robust-speech-event

        
---




This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on a private dataset.
It achieves the following results on the evaluation set:


The following hyper-parameters were used during training:
- learning_rate: 3e-4
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 800
- num_epochs: 30
- mixed_precision_training: Native AMP
