---
license: mit
tags:
- object-detection
- object-tracking
- video
- video-object-segmentation
inference: false
---

# unicorn_track_large_mask 

## Table of Contents
- [unicorn_track_large_mask](#-model_id--defaultmymodelname-true)
  - [Table of Contents](#table-of-contents)
  - [Model Details](#model-details)
  - [Uses](#uses)
      - [Direct Use](#direct-use)
  - [Evaluation Results](#evaluation-results)


<model_details>

## Model Details

Unicorn accomplishes the great unification of the network architecture and the learning paradigm for four tracking tasks. Unicorn puts forwards new state-of-the-art performance on many challenging tracking benchmarks using the same model parameters. This model has an input size of 800x1280.

- License: This model is licensed under the MIT license
- Resources for more information:
  - [Research Paper](https://arxiv.org/abs/2111.12085)
  - [GitHub Repo](https://github.com/MasterBin-IIAU/Unicorn)

</model_details>

<uses>

## Uses

#### Direct Use

This model can be used for:

* Single Object Tracking (SOT)
* Multiple Object Tracking (MOT)
* Video Object Segmentation (VOS)
* Multi-Object Tracking and Segmentation (MOTS)

<Eval_Results>

## Evaluation Results

LaSOT AUC (%): 68.5
BDD100K mMOTA (%): 41.2
DAVIS17 J&F (%): 69.2
BDD100K MOTS mMOTSA (%): 29.6


</Eval_Results>

<Cite>

## Citation Information

```bibtex
@inproceedings{unicorn,
  title={Towards Grand Unification of Object Tracking},
  author={Yan, Bin and Jiang, Yi and Sun, Peize and Wang, Dong and Yuan, Zehuan and Luo, Ping and Lu, Huchuan},
  booktitle={ECCV},
  year={2022}
}
```
</Cite>