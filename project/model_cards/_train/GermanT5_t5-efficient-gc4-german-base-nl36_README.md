---
language: de
license: mit
tags:
- german
- deutsch
---

# Creators
- [Stefan Schweter](https://github.com/stefan-it) ([schweter.ml](https://schweter.ml))
- [Philip May](https://may.la) ([T-Systems onsite](https://www.t-systems-onsite.de/))
- [Philipp Schmid ](https://www.philschmid.de/) ([Hugging Face](https://huggingface.co/))

# Evaluation
Evaluation was done on a summarization task with:
- train data: [Swisstext](https://www.swisstext.org/2019/shared-task/german-text-summarization-challenge.html)
- test data: [MLSUM](https://huggingface.co/datasets/mlsum)
- GPUs: 4 (V100)

for details see: <https://github.com/GermanT5/german-t5-eval>

# Tips for training on GPUs
This model is too big to fit on a normal 16GB GPU in FP32 mode.
For various reasons, T5 models cannot be trained in FP16 mode.
However, mixed precision training is not yet supported on many GPUs. 
For example, it does not work on V100 GPUs. On A100, however, it does.

That is why we suggest to use [DeepSpeed](https://github.com/microsoft/DeepSpeed) for training.
In particular, we recommend the [ZeRO-3 Example](https://huggingface.co/docs/transformers/main_classes/deepspeed#zero3-example) `auto` configuration.

> ZeRO-Offload pushes the boundary of the maximum model size that can be trained efficiently using minimal GPU resources, by exploiting computational and memory resources on both GPUs and their host CPUs.

see [ZeRO-Offload](https://www.deepspeed.ai/features/#zero-offload) 

## License - The MIT License
Copyright 2022 Stefan Schweter<br>
Copyright 2022 Philip May, T-Systems onsite<br>
Copyright 2022 P. S.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
