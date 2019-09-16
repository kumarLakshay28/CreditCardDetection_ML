# Correlation Matrix

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv('creditcard.csv')

def cormat_disp():
    cormat = df.corr()
    fig = plt.figure(figsize =(12,9))
    sns.heatmap(cormat, vmax = .8, square=True)
    plt.show()