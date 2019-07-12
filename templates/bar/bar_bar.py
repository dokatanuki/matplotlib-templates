import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Bar width
w=0.2

# Data
legend = np.array(['hoge', 'fuga', 'piyo', 'foo'])
throughput = np.array([50, 500, 200, 400])
utilization = np.array([23, 20, 100, 100])

# Index
x=np.arange(len(legend))

# Plot graphs
plt.xticks(x+w/2, legend, rotation=0)
plt.xlabel('Server number')

plt.ylim(0,600)
plt.ylabel('Throughput [req/s]')
b1 = plt.bar(x, throughput, width=w, label='Throughput [req/s]', fill=None, hatch='xx')

plt.twinx()
plt.ylim(0,120)
plt.ylabel('CPU Utilization [%]')
b2 = plt.bar(x+w, utilization, width=w, label='CPU Utilization [%]', fill=None, hatch='//')

plt.legend(handles=[b1,b2],loc='best')
plt.title('Bar')
plt.tight_layout()
plt.show()
