# Tranception model

This Hugging Face Hub repo contains the model checkpoint for the Tranception model as described in our paper ["Tranception: protein fitness prediction with autoregressive transformers and inference-time retrieval"](https://arxiv.org/abs/2205.13760). The official GitHub repository can be accessed [here](https://github.com/OATML-Markslab/Tranception). This project is a joint collaboration between the [Marks lab](https://www.deboramarkslab.com/) and the [OATML group](https://oatml.cs.ox.ac.uk/).

## Abstract
The ability to accurately model the fitness landscape of protein sequences is critical to a wide range of applications, from quantifying the effects of human variants on disease likelihood, to predicting immune-escape mutations in viruses and designing novel biotherapeutic proteins. Deep generative models of protein sequences trained on multiple sequence alignments have been the most successful approaches so far to address these tasks. The performance of these methods is however contingent on the availability of sufficiently deep and diverse alignments for reliable training. Their potential scope is thus limited by the fact many protein families are hard, if not impossible, to align. Large language models trained on massive quantities of non-aligned protein sequences from diverse families address these problems and show potential to eventually bridge the performance gap. We introduce Tranception, a novel transformer architecture leveraging autoregressive predictions and retrieval of homologous sequences at inference to achieve state-of-the-art fitness prediction performance. Given its markedly higher performance on multiple mutants, robustness to shallow alignments and ability to score indels, our approach offers significant gain of scope over existing approaches. To enable more rigorous model testing across a broader range of protein families, we develop ProteinGym -- an extensive set of multiplexed assays of variant effects, substantially increasing both the number and diversity of assays compared to existing benchmarks.

## License
This project is available under the MIT license.

## Reference
If you use Tranception or other files provided through our GitHub repository, please cite the following paper:
```
Notin, P., Dias, M., Frazer, J., Marchena-Hurtado, J., Gomez, A., Marks, D.S., Gal, Y. (2022). Tranception: Protein Fitness Prediction with Autoregressive Transformers and Inference-time Retrieval. ICML.
```

## Links
Pre-print: https://arxiv.org/abs/2205.13760
GitHub: https://github.com/OATML-Markslab/Tranception