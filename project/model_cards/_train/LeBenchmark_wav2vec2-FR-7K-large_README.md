---
language: "fr"
thumbnail:
tags:
- wav2vec2
license: "apache-2.0"
---

# LeBenchmark: wav2vec2 large model trained on 7K hours of French speech

  

LeBenchmark provides an ensemble of pretrained wav2vec2 models on different French datasets containing spontaneous, read, and broadcasted speech. For more information on the different benchmarks that can be used to evaluate the wav2vec2 models, please refer to our paper at: [Task Agnostic and Task Specific Self-Supervised Learning from Speech with LeBenchmark](https://openreview.net/pdf?id=TSvj5dmuSd)

  

## Model and data descriptions

  
We release four different models that can be found under our HuggingFace organization. Two different wav2vec2 architectures *Base* and *Large* are coupled with our small (1K), medium (3K), and large (7K) corpus. A larger one should come later. In short:

- [wav2vec2-FR-7K-large](https://huggingface.co/LeBenchmark/wav2vec2-FR-7K-large): Large wav2vec2 trained on 7.6K hours of French speech (1.8K Males / 1.0K Females / 4.8K unknown).
- [wav2vec2-FR-7K-base](https://huggingface.co/LeBenchmark/wav2vec2-FR-7K-base): Base wav2vec2 trained on 7.6K hours of French speech (1.8K Males / 1.0K Females / 4.8K unknown).
- [wav2vec2-FR-3K-large](https://huggingface.co/LeBenchmark/wav2vec2-FR-3K-large): Large wav2vec2 trained on 2.9K hours of French speech (1.8K Males / 1.0K Females / 0.1K unknown).
- [wav2vec2-FR-3K-base](https://huggingface.co/LeBenchmark/wav2vec2-FR-3K-base): Base wav2vec2 trained on 2.9K hours of French speech (1.8K Males / 1.0K Females / 0.1K unknown).
- [wav2vec2-FR-2.6K-base](https://huggingface.co/LeBenchmark/wav2vec2-FR-2.6K-base): Base wav2vec2 trained on 2.6K hours of French speech (**no spontaneous speech**).
- [wav2vec2-FR-1K-large](https://huggingface.co/LeBenchmark/wav2vec2-FR-1K-large): Large wav2vec2 trained on 1K hours of French speech (0.5K Males / 0.5K Females).
- [wav2vec2-FR-1K-base](https://huggingface.co/LeBenchmark/wav2vec2-FR-1K-base): Base wav2vec2 trained on 1K hours of French speech (0.5K Males / 0.5K Females).

## Intended uses & limitations

Pretrained wav2vec2 models are distributed under the Apache-2.0 license. Hence, they can be reused extensively without strict limitations. However, benchmarks and data may be linked to corpora that are not completely open-sourced.

## Fine-tune with Fairseq for ASR with CTC

As our wav2vec2 models were trained with Fairseq, then can be used in the different tools that they provide to fine-tune the model for ASR with CTC. The full procedure has been nicely summarized in [this blogpost](https://huggingface.co/blog/fine-tune-wav2vec2-english).

Please note that due to the nature of CTC, speech-to-text results aren't expected to be state-of-the-art. Moreover, future features might appear depending on the involvement of Fairseq and HuggingFace on this part.
  
## Integrate to SpeechBrain for ASR, Speaker, Source Separation ...

Pretrained wav2vec models recently gained in popularity. At the same time, [SpeechBrain toolkit](https://speechbrain.github.io) came out, proposing a new and simpler way of dealing with state-of-the-art speech & deep-learning technologies.

While it currently is in beta, SpeechBrain offers two different ways of nicely integrating wav2vec2 models that were trained with Fairseq i.e our LeBenchmark models!

 1. Extract wav2vec2 features on-the-fly (with a frozen wav2vec2 encoder) to be combined with any speech-related architecture. Examples are: E2E ASR with CTC+Att+Language Models; Speaker Recognition or Verification, Source Separation ...
 2. *Experimental:* To fully benefit from wav2vec2, the best solution remains to fine-tune the model while you train your downstream task. This is very simply allowed within SpeechBrain as just a flag needs to be turned on. Thus, our wav2vec2 models can be fine-tuned while training your favorite ASR pipeline or Speaker Recognizer.

**If interested, simply follow this [tutorial](https://colab.research.google.com/drive/17Hu1pxqhfMisjkSgmM2CnZxfqDyn2hSY?usp=sharing)**

## Referencing LeBenchmark

```
@article{Evain2021LeBenchmarkAR,
  title={LeBenchmark: A Reproducible Framework for Assessing Self-Supervised Representation Learning from Speech},
  author={Sol{\`e}ne Evain and Ha Nguyen and Hang Le and Marcely Zanon Boito and Salima Mdhaffar and Sina Alisamir and Ziyi Tong and N. Tomashenko and Marco Dinarelli and Titouan Parcollet and A. Allauzen and Y. Est{\`e}ve and B. Lecouteux and F. Portet and S. Rossato and F. Ringeval and D. Schwab and L. Besacier},
  journal={ArXiv},
  year={2021},
  volume={abs/2104.11462}
}
```
