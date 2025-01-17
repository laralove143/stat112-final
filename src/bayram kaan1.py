import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#opening and reading cleaned data file as csv 
data = open(r'c:\Users\bayram kaan\Documents\clean.csv')
df = pd.read_csv(data)
#writing palette and other factors to set theme
sns.set_theme(
    style="ticks",
    font="Verdana",
    palette=sns.color_palette(["#77dd77", "#ffb347", "#ff6961"]),
    context="paper",
)
#creating swarmplot to visualize distribution and relationship
swarmplot = sns.swarmplot(data=df, x="cause_of_death", y="environmental_pollution_index", hue="cause_of_death", legend=False, palette="deep", size= 6)
#writing title, fixing label
swarmplot.set_title("Relationship Cause of the Death and Pollution")
swarmplot.set(xlabel ="", ylabel= "Enviromental Pollution Index")
plt.show()

