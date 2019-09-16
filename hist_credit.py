import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv('creditcard.csv')

def hist_disp():
	df.hist(figsize = (20,20))
	return (plt.show())
    