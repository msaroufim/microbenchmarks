import os
import time
import zipfile
from transformers import AutoModelForCausalLM, AutoTokenizer

# Step 1: Download the weights of the model using the provided code
model_id = "meta-llama/Llama-2-7b-hf"

# Use the current directory as the cache directory
current_directory = os.path.dirname(os.path.abspath(__file__))

tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=current_directory)
model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=current_directory)


# Time the zips, can use iostat to monitor io device usage
# `time zip -r blobs.zip blob`
# `time unzip blobs.zip`
