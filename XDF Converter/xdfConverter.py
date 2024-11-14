import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  
import sys
import os

sub = sys.argv[-1]

data, header = pyxdf.load_xdf("./" + sub + ".xdf")
df_merged = pd.DataFrame()

for stream in data:
    y = stream['time_series']
    df_temp = pd.DataFrame(zip(stream['time_stamps'], y)) 
    df_merged = pd.concat([df_merged, df_temp], ignore_index=True)

df_merged.columns = ["Timestamp", "Data"]
df_merged.sort_values("Timestamp", inplace=True)

output_dir_path = "./Results/" + sub 
if not os.path.exists(output_dir_path):
    os.mkdir(output_dir_path)

df_merged.to_csv(output_dir_path + "/OutputCSV.csv")
print("Subject data successfully written to ", output_dir_path)