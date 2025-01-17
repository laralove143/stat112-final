#importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Setting the theme of the graph
sns.set_theme(
    style="ticks",
    font="Verdana",
    palette=sns.color_palette(["#77dd77", "#ffb347", "#ff6961"]),
    context="paper",
)

# Loading the previously cleaned dateset
cleaned_path = "/Users/seymakarabulut/Downloads/VERYclean.xlsx"
df_cleaned = pd.read_excel(cleaned_path)

#The code of the boxplots that displays the relationships between Mortality Rate Per 1000, Cause of Death and Economic Status
plt.figure(figsize=(12, 8))
sns.boxplot(
    data=df_cleaned,
    x="mortality_rate_per_thousand",
    y="cause_of_death",
    hue="economic_status",

)

# Determining the title and axis names
plt.title("Mortality Rate by Cause of Death and Economic Status", fontsize=16)
plt.xlabel("Mortality Rate Per 1000", fontsize=12)
plt.ylabel("Cause of Death", fontsize=12)

# Creating a legend
plt.legend(
    title="Economic Status",
    loc="lower left",
    bbox_to_anchor=(-0.2, 0)  # Adjust x and y values as needed
)

# Displaying the plot
plt.tight_layout()
plt.show()