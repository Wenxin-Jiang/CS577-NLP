---
language: en
license: apache-2.0
inference: false
---

# GPT-NeoX-20B-Erebus
## Model description
This is the second generation of the original Shinen made by Mr. Seeker. The full dataset consists of 6 different sources, all surrounding the "Adult" theme. The name "Erebus" comes from the greek mythology, also named "darkness". This is in line with Shin'en, or "deep abyss". For inquiries, please contact the KoboldAI community. **Warning: THIS model is NOT suitable for use by minors. The model will output X-rated content.**

## Training procedure
GPT-NeoX-20B-Erebus was trained on a TPUv3-256 TPU pod using a heavily modified version of Ben Wang's Mesh Transformer JAX library, the original version of which was used by EleutherAI to train their GPT-J-6B model.

## Training data
The data can be divided in 6 different datasets:
- Literotica (everything with 4.5/5 or higher)
- Sexstories (everything with 90 or higher)
- Dataset-G (private dataset of X-rated stories)
- Doc's Lab (all stories)
- Pike Dataset (novels with "adult" rating)
- SoFurry (collection of various animals)

The dataset uses `[Genre: <comma-separated list of genres>]` for tagging.

## Limitations and biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion). **Warning: This model has a very strong NSFW bias!**

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
