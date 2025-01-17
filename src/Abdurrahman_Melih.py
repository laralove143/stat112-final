import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# Set seaborn theme and style
sns.set_theme(
    style="ticks",
    font="Verdana",
    palette=sns.color_palette(["#77dd77", "#ffb347", "#ff6961"]),  # Custom color palette
    context="paper",
)

mpl.rcParams["figure.dpi"] = 300  # Adjusting DPI for high resolution

# Load the cleaned dataset
file_path = 'finalfinal.csv'
df_clean = pd.read_csv(file_path)

# Converting the 'year' column to a numeric type, handling non-numeric values by replacing them with 0, and ensuring the final type is integer.
df_clean['year'] = pd.to_numeric(df_clean['year'], errors='coerce').fillna(0).astype(int)

# Filtering data for 'Infectious diseases'
infectious_data = df_clean[df_clean['cause_of_death'] == 'Infectious diseases']

# Group by year and calculate death count (using the count of rows for each year)
grouped_data = infectious_data.groupby('year').agg({
    'cause_of_death': 'count',  # 'count' of rows represents the death count
    'poverty_rate_percent': 'mean'
}).reset_index()

# Renaming columns for clarity
grouped_data = grouped_data.rename(columns={'cause_of_death': 'death_count'})

# Filling the missing years
all_years = pd.DataFrame({'year': range(grouped_data['year'].min(), grouped_data['year'].max() + 1)})
grouped_data = pd.merge(all_years, grouped_data, on='year', how='left')

# Handling NaN values
grouped_data['death_count'] = grouped_data['death_count'].fillna(0).astype(int)
grouped_data['poverty_rate_percent'] = grouped_data['poverty_rate_percent'].fillna(grouped_data['poverty_rate_percent'].mean())

# Plot the data
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plot for deaths due to infectious diseases with new color
ax1.bar(grouped_data['year'], grouped_data['death_count'], color=sns.color_palette(["#ffb347"])[0], alpha=0.7, label='Deaths due to Infectious Diseases')
ax1.set_xlabel('Year')
ax1.set_ylabel('Deaths (Count)', color=sns.color_palette(["black"])[0])
ax1.tick_params(axis='y', labelcolor=sns.color_palette(["black"])[0])
ax1.set_xticks(grouped_data['year'])  

# Line plot for poverty rate with new color
ax2 = ax1.twinx()
ax2.plot(grouped_data['year'], grouped_data['poverty_rate_percent'], color=sns.color_palette(["#ff6961"])[0], marker='o', label='Average Poverty Rate (%)')
ax2.set_ylabel('Average Poverty Rate (%)', color=sns.color_palette(["black"])[0])
ax2.tick_params(axis='y', labelcolor=sns.color_palette(["black"])[0])

# Adding legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

plt.title('Infectious Diseases Deaths and Poverty Rate Over Time')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
