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
    palette=sns.color_palette(["#77dd77"]),
    context="paper",
)
#creating swarmplot to visualize distribution and relationship
regplot = sns.regplot(data=df, x='life_expectancy', y='environmental_pollution_index', order=3, line_kws=dict(color="black"), ci=10)
#writing title, fixing label and selecting styles
regplot.set_title("Relationship Between Life Expectacny and Enviromental Pollution Index")
regplot.set(xlabel="Life Expectancy", ylabel="Enviromental Pollution Index")

plt.show()
