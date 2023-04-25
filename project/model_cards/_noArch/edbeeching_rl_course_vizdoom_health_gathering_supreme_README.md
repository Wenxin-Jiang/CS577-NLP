---
library_name: sample-factory
tags:
- deep-reinforcement-learning
- reinforcement-learning
- sample-factory
model-index:
- name: APPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: doom_health_gathering_supreme
      type: doom_health_gathering_supreme
    metrics:
    - type: mean_reward
      value: 8.07 +/- 1.90
      name: mean_reward
      verified: false
---

A(n) **APPO** model trained on the **doom_health_gathering_supreme** environment.

This model was trained using Sample-Factory 2.0: https://github.com/alex-petrenko/sample-factory.
Documentation for how to use Sample-Factory can be found at https://www.samplefactory.dev/


## Downloading the model

After installing Sample-Factory, download the model with:
```
python -m sample_factory.huggingface.load_from_hub -r edbeeching/rl_course_vizdoom_health_gathering_supreme
```

    
## Using the model

To run the model after download, use the `enjoy` script corresponding to this environment:
```
python -m .usr.local.lib.python3.8.dist-packages.ipykernel_launcher --algo=APPO --env=doom_health_gathering_supreme --train_dir=./train_dir --experiment=rl_course_vizdoom_health_gathering_supreme
```


You can also upload models to the Hugging Face Hub using the same script with the `--push_to_hub` flag.
See https://www.samplefactory.dev/10-huggingface/huggingface/ for more details
        
## Training with this model

To continue training with this model, use the `train` script corresponding to this environment:
```
python -m .usr.local.lib.python3.8.dist-packages.ipykernel_launcher --algo=APPO --env=doom_health_gathering_supreme --train_dir=./train_dir --experiment=rl_course_vizdoom_health_gathering_supreme --restart_behavior=resume --train_for_env_steps=10000000000
```

Note, you may have to adjust `--train_for_env_steps` to a suitably high number as the experiment will resume at the number of steps it concluded at.
        