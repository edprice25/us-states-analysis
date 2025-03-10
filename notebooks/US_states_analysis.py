#!/usr/bin/env python
# coding: utf-8

# In[1]:


saveFigures=False


# In[2]:


# State Income Tax
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Fill NaN data with empty string
filledDf = df.fillna({
    'State Income Tax (Type)': '',
    'State Income Tax (Notes)': '',
})

# Sort the DataFrame
sortedDf = filledDf.sort_values(by=["State Income Tax (Approx Pct)"], ascending=False)

# Color mapping for groups.
# These six colors (excluding the purposely hidden white), taken from the default matplotlib color cycle,
# offer good contrast and are generally distinguishable by people with color vision deficiencies.
sortedDf['group'] = sortedDf['State Income Tax (Type)']
colors = {
    'Flat rate': '#1f77b4', # a muted blue
    'Top marginal rate': '#2ca02c', # a vibrant green
    'Approx top rate': '#ff7f0e', # a bright orange
    'Only dividends & interest taxed': '#8c564b', # a dark brown
    '': 'white',
}
sortedDf['color'] = sortedDf['group'].map(colors)

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(6,25), y="State Income Tax (Approx Pct)", color=sortedDf['color'])

# Create legend elements
patches = [mpatches.Patch(color=color, label=group) for group, color in colors.items()]
plt.legend(handles=patches, loc='best')

# Format the x-axis to display percentages
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1))

# Add value labels on each bar
for container in ax.containers:
    #ax.bar_label(container)  # no formatting
    #ax.bar_label(container, fmt=' {:.2%}')  # pct formatting
    ax.bar_label(container, fmt=lambda x: f' {x:.2%}' if x > 0 else ' None')  # conditional pct formatting

# Label some of the horizontal bars (patches) with additional information
notes_index = sortedDf.columns.get_loc("State Income Tax (Notes)")
for p in ax.patches:
    # Find the corresponding DataFrame row index
    bar_index = np.floor(p.get_y())+1

    # Get the value from the DataFrame
    notes_value = sortedDf.iloc[int(bar_index), notes_index]

    # Add the text to the bar
    ax.annotate(text=notes_value, xy=(p.get_x(), p.get_y()), fontsize=8, va='top')

# Customize the chart
plt.ylabel('')
plt.title('State Income Tax (approx pct) for all US States/Territories in 2024')

# Hide x-axis tick marks and labels on the top and bottom
ax.tick_params(top=False, labeltop=False, bottom=False, labelbottom=False)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-state-income-tax.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[3]:


# Sales Tax
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Fill NaN data with empty string
filledDf = df.fillna({
    'Sales Tax (Type)': '',
    'Sales Tax (Notes)': '',
})

# Sort the DataFrame
sortedDf = filledDf.sort_values(by=["Sales Tax (Pct)"], ascending=False)

# Color mapping for groups.
# These four colors (excluding the purposely hidden white), taken from the default matplotlib color cycle,
# offer good contrast and are generally distinguishable by people with color vision deficiencies.
sortedDf['group'] = sortedDf['Sales Tax (Type)']
colors = {
    'Base rate': '#1f77b4', # a muted blue
    'Gross Receipts Tax': '#2ca02c', # a vibrant green
    'General Excise Tax': '#ff7f0e', # a bright orange
    'IVU (Sales Tax)': '#8c564b', # a dark brown
    '': 'white',
}
sortedDf['color'] = sortedDf['group'].map(colors)

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(6,25), y="Sales Tax (Pct)", color=sortedDf['color'])

# Create legend elements
patches = [mpatches.Patch(color=color, label=group) for group, color in colors.items()]
plt.legend(handles=patches, loc='best')

# Format the x-axis to display percentages
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1))

# Add value labels on each bar
for container in ax.containers:
    #ax.bar_label(container)  # no formatting
    #ax.bar_label(container, fmt=' {:.2%}')  # pct formatting
    ax.bar_label(container, fmt=lambda x: f' {x:.2%}' if x > 0 else ' None')  # conditional pct formatting

# Label some of the horizontal bars (patches) with additional information
notes_index = sortedDf.columns.get_loc("Sales Tax (Notes)")
for p in ax.patches:
    # Find the corresponding DataFrame row index
    bar_index = np.floor(p.get_y())+1

    # Get the value from the DataFrame
    notes_value = sortedDf.iloc[int(bar_index), notes_index]

    # Add the text to the bar
    ax.annotate(text=notes_value, xy=(p.get_x(), p.get_y()), fontsize=8, va='top')

# Customize the chart
plt.ylabel('')
plt.title('Sales Tax (pct) for all US States/Territories in 2024')

# Hide x-axis tick marks and labels on the top and bottom
ax.tick_params(top=False, labeltop=False, bottom=False, labelbottom=False)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-sales-tax.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[4]:


# Property Tax
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Fill NaN data with empty string
filledDf = df.fillna({
    'Property Tax Exceptions and Notable Exemptions': '',
})

# Sort the DataFrame
sortedDf = filledDf.sort_values(by=["Effective Property Tax Rate (Approx Pct)"], ascending=False)

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(6,30), y="Effective Property Tax Rate (Approx Pct)", legend=False)

# Format the x-axis to display percentages
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1))

# Add value labels on each bar
for container in ax.containers:
    #ax.bar_label(container)  # no formatting
    #ax.bar_label(container, fmt=' {:.2%}')  # pct formatting
    ax.bar_label(container, fmt=lambda x: f' {x:.2%}' if x > 0 else ' None')  # conditional pct formatting

# Label some of the horizontal bars (patches) with additional information
notes_index = sortedDf.columns.get_loc("Property Tax Exceptions and Notable Exemptions")
for p in ax.patches:
    # Find the corresponding DataFrame row index
    bar_index = np.floor(p.get_y())+1

    # Get the value from the DataFrame
    notes_value = sortedDf.iloc[int(bar_index), notes_index]

    # Add the text to the bar
    ax.annotate(text=notes_value, xy=(p.get_x(), p.get_y()), fontsize=8, va='top')

# Customize the chart
plt.ylabel('')
plt.title('Effective Property Tax Rate (approx pct) for all US States/Territories in 2024')

# Hide x-axis tick marks and labels on the top and bottom
ax.tick_params(top=False, labeltop=False, bottom=False, labelbottom=False)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-property-tax.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[5]:


# Population
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Sort the DataFrame
sortedDf = df.sort_values(by=["Total Population"])

# Set the calculated columns
sortedDf['Older Population'] = sortedDf['Total Population'] * sortedDf['Seniors Population (Pct)']
sortedDf['Younger Population'] = sortedDf['Total Population'] * (1.0 - sortedDf['Seniors Population (Pct)'])

# Create horizontal bar plot (two bars)
#ax = sortedDf.plot.barh(figsize=(10,25), y=['Older Population', 'Younger Population'], color=['#ff7f0e', '#1f77b4'])

# Create horizontal bar plot (stacked)
ax = sortedDf.plot.barh(figsize=(10,20), y=['Older Population', 'Younger Population'], stacked=True, color=['#ff7f0e', '#1f77b4'])

# Format the x-axis to display commas for thousands separators
#ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

# Format the x-axis to display millions
ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: f'{x/1e6:.1f}M'))

# Define symbols for trends
trend_symbols = {
    "Growing": "↑",
    "Growing (slow)": "↑",
    "Stable": "→",
    "Slightly Shrinking/Stable": "→",
    "Stable/Slightly Shrinking": "→",
    "Shrinking": "↓",
    "Slightly Shrinking": "↓",
}

# Choose arrow colors for each type of trend
seniors_arrow_color = '#ff7f0e' # a bright orange
total_arrow_color = 'black'

# For Seniors Population, annotate each bar with the corresponding trend arrow.
for i, (pop_val, trend) in enumerate(zip(sortedDf['Older Population'], sortedDf['Seniors Population Trend'])):
    ax.text(pop_val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color=seniors_arrow_color)

# For Total Population, annotate each bar with the corresponding trend arrow.
for i, (pop_val, trend) in enumerate(zip(sortedDf['Total Population'], sortedDf['Total Population Trend'])):
    ax.text(pop_val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color=total_arrow_color)

# Customize the chart
plt.ylabel('')
plt.title('Population for all US States/Territories in 2024')

# Move tick marks and labels to the top
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

# Move the legend to the upper right using bbox_to_anchor
#plt.legend(loc='upper right', bbox_to_anchor=(1, 0.95))
legend1 = ax.legend(loc='upper right', bbox_to_anchor=(1, 0.95))

# Create a second legend for the trend arrows using custom patches
seniors_patch = mpatches.Patch(color=seniors_arrow_color, label='Older Population Trend')
total_patch = mpatches.Patch(color=total_arrow_color, label='Total Population Trend')
legend2 = ax.legend(handles=[seniors_patch, total_patch], loc='upper right', bbox_to_anchor=(1, 0.90), title='Trends (↑ → ↓)')

# Add the first legend back to the axes (so both show up)
ax.add_artist(legend1)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-population.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[6]:


# Tech Jobs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Sort the DataFrame
sortedDf = df.sort_values(by=["Tech/IT Jobs (Approx)"])

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(10,20), y=['Tech/IT Jobs (Approx)'], legend=False)

# Format the x-axis to display commas for thousands separators
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

# Define symbols for trends
trend_symbols = {
    "Growing": "↑",
    "Stable": "→",
    "Shrinking": "↓",
}

# Annotate each bar with the corresponding trend arrow.
for i, (val, trend) in enumerate(zip(sortedDf['Tech/IT Jobs (Approx)'], sortedDf['Tech/IT Jobs Trend'])):
    ax.text(val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color='black')

# Customize the chart
plt.ylabel('')
plt.title('Tech Jobs for all US States/Territories in 2024')

# Move tick marks and labels to the top
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-tech-jobs.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[7]:


# Monthly Rent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Sort the DataFrame
sortedDf = df.sort_values(by=["Average Monthly Rent (Estimate USD)"], ascending=False)

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(10,20), y=['Average Monthly Rent (Estimate USD)'], legend=False)

# Format the x-axis to display currency with commas for thousands separators
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))

# Define symbols for trends
trend_symbols = {
    "Rising": "↑",
    "Stable": "→",
    "Falling": "↓",
}

# Annotate each bar with the corresponding trend arrow.
for i, (val, trend) in enumerate(zip(sortedDf['Average Monthly Rent (Estimate USD)'], sortedDf['Monthly Rent Trend'])):
    ax.text(val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color='black')

# Customize the chart
plt.ylabel('')
plt.title('Average Monthly Rent (estimate USD) for all US States/Territories in 2024')

# Show tick marks and labels on the top and bottom
ax.tick_params(top=True, labeltop=True, bottom=True, labelbottom=True)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-monthly-rent.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[8]:


# Household Annual Salary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Sort the DataFrame
sortedDf = df.sort_values(by=["Avg Household Annual Salary (Estimate USD)"])

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(10,20), y=['Avg Household Annual Salary (Estimate USD)'], legend=False)

# Format the x-axis to display currency thousands
ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, pos: f'${x/1e3:.1f}K'))

# Define symbols for trends
trend_symbols = {
    "Rising": "↑",
    "Stable": "→",
    "Falling": "↓",
}

# Annotate each bar with the corresponding trend arrow.
for i, (val, trend) in enumerate(zip(sortedDf['Avg Household Annual Salary (Estimate USD)'], sortedDf['Household Annual Salary Trend'])):
    ax.text(val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color='black')

# Customize the chart
plt.ylabel('')
plt.title('Average Household Annual Salary (estimate USD) for all US States/Territories in 2024')

# Show tick marks and labels on the top and bottom
ax.tick_params(top=True, labeltop=True, bottom=True, labelbottom=True)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-household-annual-salary.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[9]:


# Cost of Living
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Sort the DataFrame
sortedDf = df.sort_values(by=["Cost of Living Index (Approx) (US Avg 100)"], ascending=False)

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(10,20), y=['Cost of Living Index (Approx) (US Avg 100)'], legend=False)

# Define symbols for trends
trend_symbols = {
    "Rising": "↑",
    "Stable": "→",
    "Falling": "↓",
}

# Annotate each bar with the corresponding trend arrow.
for i, (val, trend) in enumerate(zip(sortedDf['Cost of Living Index (Approx) (US Avg 100)'], sortedDf['Cost of Living Trend'])):
    ax.text(val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color='black')

# Customize the chart
plt.ylabel('')
plt.title('Cost of Living Index (US avg 100) for all US States/Territories in 2024')

# Show tick marks and labels on the top and bottom
ax.tick_params(top=True, labeltop=True, bottom=True, labelbottom=True)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-cost-of-living.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()


# In[10]:


# Life Satisfaction Score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick

plt.close("all")

# Import Excel data into DataFrame
df = pd.read_excel(r"C:\ep\portfolio\GitHub repositories\us-states-analysis\data\US States Analysis.xlsx", "2024", index_col=0)

# Sort the DataFrame
sortedDf = df.sort_values(by=["Life Satisfaction Score (0-100)"])

# Create horizontal bar plot
ax = sortedDf.plot.barh(figsize=(10,20), y=['Life Satisfaction Score (0-100)'], legend=False)

# Define symbols for trends
trend_symbols = {
    "Improving": "↑",
    "Stable": "→",
    "Declining": "↓",
}

# Annotate each bar with the corresponding trend arrow.
for i, (val, trend) in enumerate(zip(sortedDf['Life Satisfaction Score (0-100)'], sortedDf['Life Satisfaction Trend'])):
    ax.text(val + 0.5, i, trend_symbols[trend], va='center', fontsize=14, color='black')

# Customize the chart
plt.ylabel('')
plt.title('Life Satisfaction Score (0-100) for all US States/Territories in 2024')

# Show tick marks and labels on the top and bottom
ax.tick_params(top=True, labeltop=True, bottom=True, labelbottom=True)

if saveFigures:
    # Save the figure as a PNG file
    plt.savefig("chart-life-satisfaction-score.png", bbox_inches='tight', dpi=300)
    plt.close()  # Close the figure to free up memory
else:
    # Display the chart
    plt.show()

