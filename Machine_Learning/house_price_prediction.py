import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split #splitting data
from sklearn.linear_model import LinearRegression #model to use
import matplotlib.pyplot as plt


df = pd.read_csv(r"boston.csv")
print(df.head())

print(df.shape)

print(df.corr())

plt.rcParams["figure.fisize"] = [8,6]
sns.heatmap(df.corr())



