---
language: en
license: apache-2.0
---
# GPT-NeoX-20B-Skein
## Model description
Skein is a series of hybrid story generation models intended for use in both text adventure writing and normal novel-style writing. The models are known to possess a strong second person bias. For inquiries, please contact the KoboldAI community.

The name comes from the Integrated Development Environment for the Inform 7 programming language, which calls a dialogue tree a "skein". Inform 6 and 7 were used to create some of the interactive fiction in the dataset.

## Training procedure
GPT-NeoX-20B-Skein was trained on a TPUv3-32 TPU pod using a heavily modified version of Ben Wang's Mesh Transformer JAX library, the original version of which was used by EleutherAI to train their GPT-J-6B model. The training hyperparameters and statistics can be found [here](https://wandb.ai/ve-forbryderne/skein-20b?workspace=user-ve-forbryderne).

## Training data
The data are mostly comprised of light novels from the dataset of the [KoboldAI/GPT-Neo-2.7B-Horni-LN](https://huggingface.co/KoboldAI/GPT-Neo-2.7B-Horni-LN) model and assorted interactive fiction. The dataset uses `[Themes: <comma-separated list of genres>]` for tagging. For more details, consult [this document](https://wandb.ai/ve-forbryderne/skein/runs/files/files/datasets/README.txt).

## Limitations and biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion).

## Citation details
The GPT-NeoX-20B model weights:
```bibtex
@inproceedings{gpt-neox-20b,
  title={{GPT-NeoX-20B}: An Open-Source Autoregressive Language Model},
  author={Black, Sid and Biderman, Stella and Hallahan, Eric and Anthony, Quentin and Gao, Leo and Golding, Laurence and He, Horace and Leahy, Connor and McDonell, Kyle and Phang, Jason and Pieler, Michael and Prashanth, USVSN Sai and Purohit, Shivanshu and Reynolds, Laria and Tow, Jonathan and Wang, Ben and Weinbach, Samuel},
  booktitle={Proceedings of the ACL Workshop on Challenges \& Perspectives in Creating Large Language Models},
  url={https://arxiv.org/abs/2204.06745},
  year={2022}
}
```

The Mesh Transformer JAX library:
```bibtex
@misc{mesh-transformer-jax,
  author = {Wang, Ben},
  title = {{Mesh-Transformer-JAX: Model-Parallel Implementation of Transformer Language Model with JAX}},
  howpublished = {\url{https://github.com/kingoflolz/mesh-transformer-jax}},
  year = 2021,
  month = May
}
```
