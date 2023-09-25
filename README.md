# Private Generative AI Model For Data Analytics On Your Data Warehouse
This repository helps to build a private AI in SQL analytics with generative models

![architecture_diagram.png](images%2Farchitecture_diagram.png)

# The Contents

# Introduction

# Build a private generative AI model focus on using SQL for data analytics


```shell
python3 -m manifest.api.app \
    --model_type huggingface \
    --model_generation_type text-generation \
    --model_name_or_path NumbersStation/nsql-350M \
    --device 0
The cache for model files in Transformers v4.22.0 has been updated. Migrating your old cache. This is a one-time only operation. You can interrupt this and resume the migration later on by calling `transformers.utils.move_cache()`.
0it [00:00, ?it/s]
[2023-09-25 15:49:08,043] [INFO] [real_accelerator.py:158:get_accelerator] Setting ds_accelerator to cuda (auto detect)
Model Name: NumbersStation/nsql-350M Model Path: NumbersStation/nsql-350M
Downloading (…)okenizer_config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 237/237 [00:00<00:00, 1.19MB/s]
Downloading (…)olve/main/vocab.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 798k/798k [00:00<00:00, 823kB/s]
Downloading (…)olve/main/merges.txt: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 456k/456k [00:00<00:00, 648kB/s]
Downloading (…)/main/tokenizer.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.11M/2.11M [00:00<00:00, 3.66MB/s]
Downloading (…)in/added_tokens.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.08k/1.08k [00:00<00:00, 6.30MB/s]
Downloading (…)cial_tokens_map.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 99.0/99.0 [00:00<00:00, 643kB/s]
Downloading (…)lve/main/config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.01k/1.01k [00:00<00:00, 8.33MB/s]
Downloading pytorch_model.bin: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.51G/1.51G [00:38<00:00, 38.8MB/s]
Downloading (…)neration_config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 115/115 [00:00<00:00, 967kB/s]
Loaded Model DType torch.float32
Usings max_length: 2048
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.22.31.156:5000
Press CTRL+C to quit
```
