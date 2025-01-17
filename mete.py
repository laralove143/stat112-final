import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = "/Users/metekocoglu/Downloads/clean.csv"  
df_cleaned = pd.read_csv(file_path)

# Display the first few rows of the dataset to ensure correct loading
print(df_cleaned.head())

# Create a violin plot to show the distribution of Healthcare Quality Index and Life Expectancy across different Economic Status
plt.figure(figsize=(12, 6))

# Define a custom color palette
custom_palette = ["#77dd77", "#AEC6CF", "#ff6961"]

# Violin plot for Healthcare Quality Index by Economic Status
plt.subplot(1, 2, 1)  # First plot in a 1x2 grid
sns.violinplot(
    data=df_cleaned,
    x='economic_status',
    y='healthcare_quality_index',
    hue='economic_status',  # Set the hue to the same as x
    palette=custom_palette,
    dodge=False,  # Avoid splitting by hue
    legend=False  # Suppress legend
)
plt.title('Distribution of Healthcare Quality Index by Economic Status', fontsize=14)
plt.xlabel('Economic Status', fontsize=12)
plt.ylabel('Healthcare Quality Index', fontsize=12)

# Violin plot for Life Expectancy by Economic Status
plt.subplot(1, 2, 2)  # Second plot in a 1x2 grid
sns.violinplot(
    data=df_cleaned,
    x='economic_status',
    y='life_expectancy',
    hue='economic_status',  # Set the hue to the same as x
    palette=custom_palette,
    dodge=False,  # Avoid splitting by hue
    legend=False  # Suppress legend
)
plt.title('Distribution of Life Expectancy by Economic Status', fontsize=14)
plt.xlabel('Economic Status', fontsize=12)
plt.ylabel('Life Expectancy', fontsize=12)

plt.tight_layout()  # Adjust the layout to prevent overlap
plt.show()




