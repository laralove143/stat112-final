# Extract Mexico data
mexico_data = df_clean[df_clean['country'] == 'Mexico'].copy()

# Visualization variables
mexico_data['year'] = mexico_data['year'].astype(int)
bar_data = mexico_data[mexico_data['year'] != 2007]

# Visualization
fig, ax1 = plt.subplots(figsize=(12, 6))

# Line chart: Healthcare Access Index
ax1.plot(
    mexico_data['year'],
    mexico_data['healthcare_access_index'],
    color='blue',
    marker='o',
    label='Healthcare Access Index'
)
ax1.set_ylabel('Healthcare Access Index', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xlabel('Year')
ax1.set_xticks(mexico_data['year'])
ax1.set_xticklabels(mexico_data['year'], rotation=45)

# Bar chart: Mortality Rate per Thousand
ax2 = ax1.twinx()
ax2.bar(
    bar_data['year'],
    bar_data['mortality_rate_per_thousand'],
    color='orange',
    alpha=0.6,
    label='Mortality Rate (per 1000)'
)
ax2.set_ylabel('Mortality Rate (per 1000)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Title and legend
fig.suptitle('Healthcare Access and Mortality Rate in Mexico', fontsize=14)
fig.legend(loc="upper left", bbox_to_anchor=(0.2, 0.85))
ax1.grid(alpha=0.3)

# Tight layout
fig.tight_layout()
plt.show()