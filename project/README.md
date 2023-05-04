# Extracting Metadata from Unstructured Pre-trained Model Documentation

This repo includes the artifact for my CS 577 NLP course project.

## Getting Started

Detailed instructions about how to get a copy of the project up and running on one's local machine for development and testing purposes.

### Prerequisites

The environment is exported in `environment.yml` in the root directory.

### Dataset
This repository includes all the data needed to run the experiments. The PTM documentations is in the `model_card` directory. The data is in the form of README files. 

For question answering model, the data is in the form of JSON files: `squad_format_data.json`.

### Running the experiments
- Classification:
```
python ./CLSmodel/train_BERT.py
```

- Question Answering
```
python ./QAmodel/train_QA.py
```

### Results
All my results and logs are saved in `.txt` files and `.out` files. The `.out` files are the logs from the HPC cluster. The `.txt` files are the results from the local experiments.

### Learning Curves
All my learning Curves are saved in the subfolders.