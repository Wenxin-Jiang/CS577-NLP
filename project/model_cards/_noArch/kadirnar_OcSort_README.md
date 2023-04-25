---
license: mit
tags:
  - object-detection
  - computer-vision
  - sort
  - tracker
  - ocsort
---

### Model Description
Observation-Centric SORT ([OC-SORT(https://arxiv.org/abs/2203.14360)]) is a pure motion-model-based multi-object tracker. It aims to improve tracking robustness in crowded scenes and when objects are in non-linear motion. It is designed by recognizing and fixing limitations in Kalman filter and SORT. It is flexible to integrate with different detectors and matching modules, such as appearance similarity. It remains, Simple, Online and Real-time.
<img src="https://raw.githubusercontent.com/noahcao/OC_SORT/master/assets/teaser.png" width="600"/>

### Installation
```
pip install ocsort
```

### Tracker
```python
from ocsort.ocsort import OCSort

tracker = OCSort(args)
for image in images:
   dets = detector(image)
   online_targets = tracker.update(dets)
```

### BibTeX Entry and Citation Info
 ```
, Jinkun and Weng, Xinshuo and Khirodkar, Rawal and Pang, Jiangmiao and Kitani, Kris},
  journal={arXiv preprint arXiv:2203.14360},
  year={2022}
}
```