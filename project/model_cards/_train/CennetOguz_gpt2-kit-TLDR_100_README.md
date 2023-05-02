---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2-kit-TLDR_100
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-kit-TLDR_100

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0927

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 3.5116          |
| No log        | 2.0   | 12   | 2.8345          |
| No log        | 3.0   | 18   | 2.4549          |
| No log        | 4.0   | 24   | 2.2672          |
| No log        | 5.0   | 30   | 2.1318          |
| No log        | 6.0   | 36   | 2.0241          |
| No log        | 7.0   | 42   | 1.9446          |
| No log        | 8.0   | 48   | 1.8859          |
| No log        | 9.0   | 54   | 1.8432          |
| No log        | 10.0  | 60   | 1.8038          |
| No log        | 11.0  | 66   | 1.7691          |
| No log        | 12.0  | 72   | 1.7473          |
| No log        | 13.0  | 78   | 1.7169          |
| No log        | 14.0  | 84   | 1.7055          |
| No log        | 15.0  | 90   | 1.6911          |
| No log        | 16.0  | 96   | 1.6842          |
| No log        | 17.0  | 102  | 1.6711          |
| No log        | 18.0  | 108  | 1.6609          |
| No log        | 19.0  | 114  | 1.6582          |
| No log        | 20.0  | 120  | 1.6518          |
| No log        | 21.0  | 126  | 1.6519          |
| No log        | 22.0  | 132  | 1.6736          |
| No log        | 23.0  | 138  | 1.6529          |
| No log        | 24.0  | 144  | 1.6738          |
| No log        | 25.0  | 150  | 1.6636          |
| No log        | 26.0  | 156  | 1.6510          |
| No log        | 27.0  | 162  | 1.6793          |
| No log        | 28.0  | 168  | 1.6638          |
| No log        | 29.0  | 174  | 1.6743          |
| No log        | 30.0  | 180  | 1.6827          |
| No log        | 31.0  | 186  | 1.6757          |
| No log        | 32.0  | 192  | 1.6947          |
| No log        | 33.0  | 198  | 1.6969          |
| No log        | 34.0  | 204  | 1.6967          |
| No log        | 35.0  | 210  | 1.7152          |
| No log        | 36.0  | 216  | 1.7040          |
| No log        | 37.0  | 222  | 1.7261          |
| No log        | 38.0  | 228  | 1.7267          |
| No log        | 39.0  | 234  | 1.7309          |
| No log        | 40.0  | 240  | 1.7514          |
| No log        | 41.0  | 246  | 1.7474          |
| No log        | 42.0  | 252  | 1.7605          |
| No log        | 43.0  | 258  | 1.7584          |
| No log        | 44.0  | 264  | 1.7817          |
| No log        | 45.0  | 270  | 1.7860          |
| No log        | 46.0  | 276  | 1.7870          |
| No log        | 47.0  | 282  | 1.8184          |
| No log        | 48.0  | 288  | 1.8138          |
| No log        | 49.0  | 294  | 1.8304          |
| No log        | 50.0  | 300  | 1.8314          |
| No log        | 51.0  | 306  | 1.8236          |
| No log        | 52.0  | 312  | 1.8518          |
| No log        | 53.0  | 318  | 1.8497          |
| No log        | 54.0  | 324  | 1.8685          |
| No log        | 55.0  | 330  | 1.8666          |
| No log        | 56.0  | 336  | 1.8769          |
| No log        | 57.0  | 342  | 1.8987          |
| No log        | 58.0  | 348  | 1.8971          |
| No log        | 59.0  | 354  | 1.9251          |
| No log        | 60.0  | 360  | 1.9175          |
| No log        | 61.0  | 366  | 1.9014          |
| No log        | 62.0  | 372  | 1.9187          |
| No log        | 63.0  | 378  | 1.9326          |
| No log        | 64.0  | 384  | 1.9401          |
| No log        | 65.0  | 390  | 1.9453          |
| No log        | 66.0  | 396  | 1.9523          |
| No log        | 67.0  | 402  | 1.9818          |
| No log        | 68.0  | 408  | 1.9802          |
| No log        | 69.0  | 414  | 1.9813          |
| No log        | 70.0  | 420  | 1.9797          |
| No log        | 71.0  | 426  | 2.0078          |
| No log        | 72.0  | 432  | 2.0135          |
| No log        | 73.0  | 438  | 2.0050          |
| No log        | 74.0  | 444  | 2.0082          |
| No log        | 75.0  | 450  | 2.0360          |
| No log        | 76.0  | 456  | 2.0310          |
| No log        | 77.0  | 462  | 2.0093          |
| No log        | 78.0  | 468  | 2.0108          |
| No log        | 79.0  | 474  | 2.0347          |
| No log        | 80.0  | 480  | 2.0559          |
| No log        | 81.0  | 486  | 2.0624          |
| No log        | 82.0  | 492  | 2.0562          |
| No log        | 83.0  | 498  | 2.0367          |
| 1.0231        | 84.0  | 504  | 2.0499          |
| 1.0231        | 85.0  | 510  | 2.0606          |
| 1.0231        | 86.0  | 516  | 2.0652          |
| 1.0231        | 87.0  | 522  | 2.0565          |
| 1.0231        | 88.0  | 528  | 2.0612          |
| 1.0231        | 89.0  | 534  | 2.0706          |
| 1.0231        | 90.0  | 540  | 2.0714          |
| 1.0231        | 91.0  | 546  | 2.0740          |
| 1.0231        | 92.0  | 552  | 2.0700          |
| 1.0231        | 93.0  | 558  | 2.0705          |
| 1.0231        | 94.0  | 564  | 2.0787          |
| 1.0231        | 95.0  | 570  | 2.0881          |
| 1.0231        | 96.0  | 576  | 2.0913          |
| 1.0231        | 97.0  | 582  | 2.0933          |
| 1.0231        | 98.0  | 588  | 2.0949          |
| 1.0231        | 99.0  | 594  | 2.0929          |
| 1.0231        | 100.0 | 600  | 2.0927          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Tokenizers 0.12.1
