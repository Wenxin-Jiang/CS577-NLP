[DialogLM: Pre-trained Model for Long Dialogue Understanding and Summarization](https://arxiv.org/abs/2109.02492).

## Introduction
DialogLED is a pre-trained model for long dialogue understanding and summarization. It builds on the Longformer-Encoder-Decoder (LED) architecture and uses window-based denoising as the pre-training task on a large amount of long dialogue data for further training. Here is a base version of DialogLED, the input length is limited to 16,384 in the pre-training phase.

## Finetuning for Downstream Tasks
Please refer to [our GitHub page](https://github.com/microsoft/DialogLM).