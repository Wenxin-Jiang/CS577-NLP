---
language: en
license: bsd-3-clause
library_name: pytorch-lightning
tags:
- pytorch-lightning
- audio-to-audio
datasets: vctk
model_name: nu-wave-x2
---

# nu-wave-x2

## Model description


NU-Wave: A Diffusion Probabilistic Model for Neural Audio Upsampling


- [GitHub Repo](https://github.com/mindslab-ai/nuwave)
- [Paper](https://arxiv.org/pdf/2104.02321.pdf)

This model was trained by contributor [Frederico S. Oliveira](https://huggingface.co/freds0), who graciously [provided the checkpoint](https://github.com/mindslab-ai/nuwave/issues/18) in the original author's GitHub repo.

This model was trained using source code written by Junhyeok Lee and Seungu Han under the BSD 3.0 License. All credit goes to them for this work.

This model takes in audio at 24kHz and upsamples it to 48kHz.


## Intended uses & limitations

#### How to use

You can try out this model here: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/nateraw/bd78af284ef78a960e18a75cb13deab1/nu-wave-x2.ipynb)

#### Limitations and bias

Provide examples of latent issues and potential remediations.

## Training data

Describe the data you used to train the model.
If you initialized it with pre-trained weights, add a link to the pre-trained model card or repository with description of the pre-training data.

## Training procedure

Preprocessing, hardware used, hyperparameters...

## Eval results

You can check out the authors' results at [their project page](https://mindslab-ai.github.io/nuwave/). The project page contains many samples of upsampled audio from the authors' models. 

### BibTeX entry and citation info

```bibtex
@inproceedings{lee21nuwave,
  author={Junhyeok Lee and Seungu Han},
  title={{NU-Wave: A Diffusion Probabilistic Model for Neural Audio Upsampling}},
  year=2021,
  booktitle={Proc. Interspeech 2021},
  pages={1634--1638},
  doi={10.21437/Interspeech.2021-36}
}
```