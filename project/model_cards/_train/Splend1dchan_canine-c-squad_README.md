python run_squad.py   \
--model_name_or_path google/canine-c  \
--do_train   \
--do_eval   \
--per_gpu_train_batch_size 1   \
--per_gpu_eval_batch_size 1   \
--gradient_accumulation_steps 128   \
--learning_rate 3e-5   \
--num_train_epochs 3   \
--max_seq_length 1024   \
--doc_stride 128   \
--max_answer_length 240   \
--output_dir canine-c-squad \
--model_type bert

{
  "_name_or_path": "google/canine-c",
  "architectures": [
    "CanineForQuestionAnswering"
  ],
  "attention_probs_dropout_prob": 0.1,
  "bos_token_id": 57344,
  "downsampling_rate": 4,
  "eos_token_id": 57345,
  "hidden_act": "gelu",
  "hidden_dropout_prob": 0.1,
  "hidden_size": 768,
  "initializer_range": 0.02,
  "intermediate_size": 3072,
  "layer_norm_eps": 1e-12,
  "local_transformer_stride": 128,
  "max_position_embeddings": 16384,
  "model_type": "canine",
  "num_attention_heads": 12,
  "num_hash_buckets": 16384,
  "num_hash_functions": 8,
  "num_hidden_layers": 12,
  "pad_token_id": 0,
  "torch_dtype": "float32",
  "transformers_version": "4.19.0.dev0",
  "type_vocab_size": 16,
  "upsampling_kernel_size": 4,
  "use_cache": true
}

{'exact': 58.893093661305585, 'f1': 72.18823344945899}