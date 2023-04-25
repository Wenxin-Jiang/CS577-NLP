---
license: mit

datasets:
- coco
- openimagesv5
- objects365v1
- visualgenome

library_name: pytorch
tags:
- pytorch
- feature-extraction
---

# Model Card: VinVL VisualBackbone

Disclaimer: The model is taken from the official  repository, it can be found here: [microsoft/scene_graph_benchmark](https://github.com/microsoft/scene_graph_benchmark)

# Usage:

More info about how to use this model can be found here: [michelecafagna26/vinvl-visualbackbone](https://github.com/michelecafagna26/vinvl-visualbackbone)

# Quick start: Feature extraction

```python
from scene_graph_benchmark.wrappers import VinVLVisualBackbone

img_file = "scene_graph_bechmark/demo/woman_fish.jpg"

detector = VinVLVisualBackbone()

dets = detector(img_file)

```

`dets` contains the following keys: ["boxes", "classes", "scores", "features", "spatial_features"]

You can obtain the full VinVL's visual features by concatenating the "features" and the "spatial_features"

```python
import numpy as np

v_feats = np.concatenate((dets['features'],  dets['spatial_features']), axis=1)
# v_feats.shape = (num_boxes, 2054)
```

# Citations

Please consider citing the original project and the VinVL paper

```BibTeX

@misc{han2021image,
      title={Image Scene Graph Generation (SGG) Benchmark}, 
      author={Xiaotian Han and Jianwei Yang and Houdong Hu and Lei Zhang and Jianfeng Gao and Pengchuan Zhang},
      year={2021},
      eprint={2107.12604},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@inproceedings{zhang2021vinvl,
  title={Vinvl: Revisiting visual representations in vision-language models},
  author={Zhang, Pengchuan and Li, Xiujun and Hu, Xiaowei and Yang, Jianwei and Zhang, Lei and Wang, Lijuan and Choi, Yejin and Gao, Jianfeng},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={5579--5588},
  year={2021}
}

```
