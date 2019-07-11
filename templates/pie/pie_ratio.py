import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Initialize graph style
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
sns.set_context("paper", 1.5, {"lines.linewidth": 4})
sns.set_palette("winter_r", 8, 1)
sns.set('talk', 'whitegrid', 'dark', font_scale=1.0,
        rc={"lines.linewidth": 2, 'grid.linestyle': '--'})

# Data
data = [505, 400, 245, 50]
legend = ['hoge', 'fuga', 'piyo', 'foo']
col = ['#3498db', '#1abc9c', '#e74c3c', '#f1c40f']

# Plot graphs
plt.figure(figsize=[9, 5], dpi=100)
plt.pie(data, counterclock=False, colors=col, shadow=False, startangle=90, autopct=lambda p:'{:.1f}%'.format(p) if p>=5 else '')
plt.legend(legend, loc='center right')
plt.title('Pie')
plt.tight_layout()
plt.axis('equal')
plt.show()
