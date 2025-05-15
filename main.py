import pandas as pd
import kagglehub as kgh
import os

# handle do dataset e o arquivo
dataset = "ky1338/10000-movies-letterboxd-data"

# download do dataset
dataset_directory = kgh.dataset_download(dataset)

for f in os.listdir(dataset_directory):
    print(f)

files = os.listdir(dataset_directory)

filename = "f"

# caminho completo para o csv
full_path_to_file = os.path.join(dataset_directory, filename)

df = pd.read_csv(filename)

print(df.head())