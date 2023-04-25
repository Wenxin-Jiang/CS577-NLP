---
tags:
- audio-to-audio
- asteroid
- audio
- audio-source-separation
datasets:
- wham
- sep_clean
license: cc-by-sa-4.0
---

## Asteroid model `mpariente/DPRNNTasNet(ks=16)_WHAM!_sepclean`

♻️ Imported from https://zenodo.org/record/3903795#.X8pMBRNKjUI

This model was trained by Manuel Pariente using the wham/DPRNN recipe in [Asteroid](https://github.com/asteroid-team/asteroid). It was trained on the sep_clean task of the WHAM! dataset.


### Demo: How to use in Asteroid

```python
# coming soon
```


### Training config

- data:
	- mode: min
	- nondefault_nsrc: None
	- sample_rate: 8000
	- segment: 2.0
	- task: sep_clean
	- train_dir: data/wav8k/min/tr
	- valid_dir: data/wav8k/min/cv
- filterbank:
	- kernel_size: 16
	- n_filters: 64
	- stride: 8
- main_args:
	- exp_dir: exp/train_dprnn_ks16/
	- help: None
- masknet:
	- bidirectional: True
	- bn_chan: 128
	- chunk_size: 100
	- dropout: 0
	- hid_size: 128
	- hop_size: 50
	- in_chan: 64
	- mask_act: sigmoid
	- n_repeats: 6
	- n_src: 2
	- out_chan: 64
- optim:
	- lr: 0.001
	- optimizer: adam
	- weight_decay: 1e-05
- positional arguments:
- training:
	- batch_size: 6
	- early_stop: True
	- epochs: 200
	- gradient_clipping: 5
	- half_lr: True
	- num_workers: 6
 
#### Results

- `si_sdr`: 18.227683982688003
- `si_sdr_imp`: 18.22883576588251
- `sdr`: 18.617789605060587
- `sdr_imp`: 18.466745426438173
- `sir`: 29.22773720052717
- `sir_imp`: 29.07669302190474
- `sar`: 19.116352171914485
- `sar_imp`: -130.06009796503054
- `stoi`: 0.9722025377865715
- `stoi_imp`: 0.23415680987800583

### Citing Asteroid

```BibTex
@inproceedings{Pariente2020Asteroid,
    title={Asteroid: the {PyTorch}-based audio source separation toolkit for researchers},
    author={Manuel Pariente and Samuele Cornell and Joris Cosentino and Sunit Sivasankaran and
            Efthymios Tzinis and Jens Heitkaemper and Michel Olvera and Fabian-Robert Stöter and
            Mathieu Hu and Juan M. Martín-Doñas and David Ditter and Ariel Frank and Antoine Deleforge
            and Emmanuel Vincent},
    year={2020},
    booktitle={Proc. Interspeech},
}
```

Or on arXiv:

```bibtex
@misc{pariente2020asteroid,
      title={Asteroid: the PyTorch-based audio source separation toolkit for researchers}, 
      author={Manuel Pariente and Samuele Cornell and Joris Cosentino and Sunit Sivasankaran and Efthymios Tzinis and Jens Heitkaemper and Michel Olvera and Fabian-Robert Stöter and Mathieu Hu and Juan M. Martín-Doñas and David Ditter and Ariel Frank and Antoine Deleforge and Emmanuel Vincent},
      year={2020},
      eprint={2005.04132},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
}
```