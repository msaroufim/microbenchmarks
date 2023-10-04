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

# Step 2: Zip the blobs directory
zip_filename = os.path.join(current_directory, "blobs.zip")
blobs_directory = os.path.join(current_directory, "blobs")

start_zip = time.time()
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(blobs_directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, blobs_directory))
end_zip = time.time()
print(f"Time taken to zip: {end_zip - start_zip} seconds")

# Step 3: Unzip the blobs.zip file to a new directory
unzip_directory = os.path.join(current_directory, "unzipped_blobs")

start_unzip = time.time()
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(unzip_directory)
end_unzip = time.time()
print(f"Time taken to unzip: {end_unzip - start_unzip} seconds")
