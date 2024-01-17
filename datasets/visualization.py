import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data Preparation
data = {
    "Dataset": ["Chipanalog", "Book", "Financial Reports", "Texas Instruments"],
    "Count of Sections": [1651, 897, 2172, 3196],
    "Count of Chars": [1298349, 310978, 654459, 2076141],
    "Count of Tokens": [675804, 235452, 449685, 666759],
    "Count of Words": [488929, 38583, 77573, 353682]
}
df = pd.DataFrame(data)

# Melting the DataFrame and filtering out 'Count of Chars'
df_melted = df.melt(id_vars="Dataset", var_name="Metric", value_name="Count")
df_filtered = df_melted[df_melted['Metric'] != 'Count of Chars']

# Setting up the plot
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid", font_scale=1.2)

# Bar plot for Count of Words and Count of Tokens on the left y-axis
ax1 = sns.barplot(x='Dataset', y='Count', hue='Metric',
                  data=df_filtered[(df_filtered['Metric'] == 'Count of Words') | (df_filtered['Metric'] == 'Count of Tokens')],
                  palette='pastel')
ax1.set_ylabel('Count for Words and Tokens')
ax1.set_xlabel('')

# Adjusting the left y-axis to represent counts in units of 1000 (keeping linear scale)
ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}k".format(int(x/1000))))

# ax1.set_xlabel('Dataset')
plt.xticks(rotation=45)

# Creating a second y-axis for the line plot of Count of Sections
ax2 = ax1.twinx()

# Setting the range for the right y-axis
ax2.set_ylim(500, 5000)

# Line plot for Count of Sections on the right y-axis
lineplot = sns.lineplot(x='Dataset', y='Count', data=df_filtered[df_filtered['Metric'] == 'Count of Sections'],
                        ax=ax2, color='black', marker='o', label='Count of Sections')
ax2.set_ylabel('Count of Sections')
ax2.grid(False)

# Adding data labels to the line plot
for x, y in zip(df_filtered[df_filtered['Metric'] == 'Count of Sections']['Dataset'], df_filtered[df_filtered['Metric'] == 'Count of Sections']['Count']):
    ax2.text(x, y+100, f'{y}', color='black', ha='right', va='bottom')

# Adjusting legend position
ax1.legend(loc='upper left')
ax2.legend(loc='lower right')

# Setting Times New Roman font
plt.rcParams["font.family"] = "Times New Roman"

# Display the plot
plt.tight_layout()
plt.show()
