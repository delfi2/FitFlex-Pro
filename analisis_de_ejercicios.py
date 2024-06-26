import csv
import pandas as pd
import matplotlib.pyplot as mp

with open ("fit_run.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

#Lee los archivos CSV
df_inv= pd.read_csv ("inversores.csv", sep=",")
df_emp=pd.read_csv ("emprendedores.csv", sep=",")