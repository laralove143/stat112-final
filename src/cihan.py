import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\cihan\Downloads\clean.csv"  
df_clean = pd.read_csv(file_path)  

data_2014 = df_clean[df_clean["year"] == 2014]

plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=data_2014,
    x="health_expenditure_gdp",
    y="life_expectancy",
    size="population", 
    sizes=(60, 1200), 
    alpha=0.6,
    hue="country",
    palette='viridis'
)

plt.title('Health Expenditure (% of GDP) vs Life Expectancy (2014)', fontsize=16)
plt.xlabel('Health Expenditure (% of GDP)', fontsize=14)
plt.ylabel("Life Expectancy (2014)", fontsize=14)
plt.legend(title='Countries and Populations', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()