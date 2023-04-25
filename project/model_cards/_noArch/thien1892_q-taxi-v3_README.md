---
tags:
- Taxi-v3
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: taxi-v3
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Taxi-v3
      type: Taxi-v3
    metrics:
    - type: mean_reward
      value: 7.58 +/- 2.72
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **Taxi-v3**
  This is a trained model of a **Q-Learning** agent playing **Taxi-v3** .

  ## Usage
1. Load model
  ```python
from urllib.error import HTTPError
from huggingface_hub import hf_hub_download

def load_from_hub(repo_id: str, filename: str) -> str:
    """
    Download a model from Hugging Face Hub.
    :param repo_id: id of the model repository from the Hugging Face Hub
    :param filename: name of the model zip file from the repository
    """
    # Get the model from the Hub, download and cache the model on your local disk
    pickle_model = hf_hub_download(
        repo_id=repo_id,
        filename=filename
    )

    with open(pickle_model, 'rb') as f:
      downloaded_model_file = pickle.load(f)
    
    return downloaded_model_file
  ```
2. Evaluate model
   ```
model = load_from_hub(repo_id="thien1892/q-taxi-v3", filename="q-learning.pkl") # Try to use another model
print(model)
env = gym.make(model["env_id"])
evaluate_agent(env, model["max_steps"], model["n_eval_episodes"], model["qtable"], model["eval_seed"])
   ```
  