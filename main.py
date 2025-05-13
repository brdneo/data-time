import pandas as pd
import kagglehub
import os

# handle do dataset e o arquivo
dataset_handle = "mohammadtalib786/retail-sales-dataset"
file_name_inside_dataset = "retail_sales_dataset.csv"

# download do dataset
dataset_directory = kagglehub.dataset_download(dataset_handle)

# caminho completo para o csv
full_path_to_file = os.path.join(dataset_directory, file_name_inside_dataset)

df = pd.read_csv(full_path_to_file)

print(df.head())