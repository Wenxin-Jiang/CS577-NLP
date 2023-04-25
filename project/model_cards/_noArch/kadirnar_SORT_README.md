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
[Sort](https://arxiv.org/abs/1602.00763): A simple online and realtime tracking algorithm for 2D multiple object tracking in video sequences<img src="https://raw.githubusercontent.com/noahcao/OC_SORT/master/assets/teaser.png" width="600"/>

### Installation
```
pip install sort-track
```

### Tracker
```python
from sort.tracker import SortTracker

tracker = SortTracker(args)
for image in images:
   dets = detector(image)
   online_targets = tracker.update(dets)
```

### BibTeX Entry and Citation Info
 ```
@inproceedings{Bewley2016_sort,
  author={Bewley, Alex and Ge, Zongyuan and Ott, Lionel and Ramos, Fabio and Upcroft, Ben},
  booktitle={2016 IEEE International Conference on Image Processing (ICIP)},
  title={Simple online and realtime tracking},
  year={2016},
  pages={3464-3468},
  keywords={Benchmark testing;Complexity theory;Detectors;Kalman filters;Target tracking;Visualization;Computer Vision;Data Association;Detection;Multiple Object Tracking},
  doi={10.1109/ICIP.2016.7533003}
}
```