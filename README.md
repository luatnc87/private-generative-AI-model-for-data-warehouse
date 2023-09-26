# Private Generative AI Model For Data Analytics On Your Data Warehouse
This repository helps to build a private AI in SQL analytics with generative models

<p align="center">
    <img src="images/architecture_diagram.png" width="600">
</p>

# The Contents
- [Introduction](#introduction)
- [Build a SQL Chatbot powered by the generative AI model](#build-a-sql-chatbot-powered-by-the-generative-ai-model)
  - [Start server to serving a Text-to-SQL model](#start-server-to-serving-a-text-to-sql-model)
  - [Build a SQL chat bot application with Streamlit framework](#build-a-sql-chat-bot-application-with-streamlit-framework)
- ✨ [Demo](#demo)
- 💖 [Supporting Links](#supporting-links)

# Introduction

# Build a SQL Chatbot powered by the generative AI model

## Start server to serving a Text-to-SQL model
In this tutorial, we will use the [NSQL model](https://huggingface.co/NumbersStation) to generate SQL from your text input.
NSQL is a family of autoregressive open-source large foundation models (FMs) designed specifically for SQL generation tasks.
Therea are some kind of NSQL models such as `nsql-350M`, `nsql-2B`, `nsql-6B` and the latest `nsql-llama-2-7B` model that are available on the `HuggingFace`.
We will leverage the [Mainifest](https://github.com/HazyResearch/manifest) library to use the `NSQL model`.
You can run following command to start a huggingface local server to server `nsql-350M` model:

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
>NOTE: In this tutorial, we use nsql-350M to minimize required memory and storage.

## Build a SQL chat bot application with Streamlit framework


## Demo
### Start the SQL chat-bot application:
You can run the following command to start a streamlit application. Make sure that you have already installed necessary libraries previously.
```shell
streamlit run streamlit_app/SQL_chat_bot.sql

You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.22.31.156:8501
```

Then, go to the *http://127.0.0.1:8501* on a web browser to access the application UI. Wait some second, you should see the applicaiton UI as below:

![streamlit_app_1.png](images%2Fstreamlit_app_1.png)

Input the DuckDB's database path and database schema:

<img src="images/streamlit_app_sibar.png" width="350">

Then, click on `Load schema` button to load the database schema.
![streamlit_app_load_schema.png](images%2Fstreamlit_app_load_schema.png)

Next step, we can ask your SQL bot in natural language.
Example:
![streamlit_app_run.png](images%2Fstreamlit_app_run.png)

# Supporting Links
- [NSQL](https://huggingface.co/NumbersStation)
- [Manifest](https://github.com/HazyResearch/manifest)
- 