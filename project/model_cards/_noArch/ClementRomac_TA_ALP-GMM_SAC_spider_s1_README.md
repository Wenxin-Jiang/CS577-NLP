---
tags:
- sac
- deep-reinforcement-learning
- reinforcement-learning
- teach-my-agent-parkour
---

  # Deep RL Agent Playing TeachMyAgent's parkour.
  You can find more info about TeachMyAgent [here](https://developmentalsystems.org/TeachMyAgent/).
  
  Results of our benchmark can be found in our [paper](https://arxiv.org/pdf/2103.09815.pdf).
  
  You can test this policy [here](https://huggingface.co/spaces/flowers-team/Interactive_DeepRL_Demo).

  *This policy was not part of TeachMyAgent's benchmark*
  
  ## Results
  Percentage of mastered tasks (i.e. reward >= 230) after 20 millions steps on the Parkour track. 
  
  Results shown are averages over 16 seeds along with the standard deviation for each morphology as well as the aggregation of the 48 seeds in the *Overall* column. 
  
  We highlight the best results in bold.
  
  | Algorithm     | BipedalWalker  | Fish          | Climber      | Overall       |
  |---------------|----------------|---------------|--------------|---------------|
  | Random        | 27.25 (± 10.7) | 23.6 (± 21.3) | 0.0 (± 0.0)  | 16.9 (± 18.3) |
  | ADR           | 14.7 (± 19.4)  | 5.3 (± 20.6)  | 0.0 (± 0.0)  | 6.7 (± 17.4)  |
  | ALP-GMM       | **42.7** (± 11.2)  | 36.1 (± 28.5) | 0.4 (± 1.2)  | **26.4** (± 25.7) |
  | Covar-GMM     | 35.7 (± 15.9)  | 29.9 (± 27.9) | 0.5 (± 1.9)  | 22.1 (± 24.2) |
  | GoalGAN       | 25.4 (± 24.7)  | 34.7 ± 37.0)  | 0.8 (± 2.7)  | 20.3 (± 29.5) |
  | RIAC          | 31.2 (± 8.2)   | **37.4** (± 25.4) | 0.4  (± 1.4) | 23.0 (± 22.4) |
  | SPDL          | 30.6 (± 22.8)  | 9.0 (± 24.2)  | **1.0** (± 3.4)  | 13.5 (± 23.0) |
  | Setter-Solver | 28.75 (± 20.7) | 5.1 (± 7.6)   | 0.0 (± 0.0)  | 11.3 (± 17.9) |

  # Hyperparameters
  ```python
  {'student': 'SAC'
'environment': 'parkour'
'training_steps': 20000000
'n_evaluation_tasks': 100
'teacher': 'ALP-GMM'
'morphology': 'spider'}
  ```
  
