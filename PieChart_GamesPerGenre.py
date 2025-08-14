from main import dfNonTime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dfNonTime.info()

sales=dfNonTime.groupby('genre')['name'].count()
genre=sales.index.tolist()
gamesCount=sales.values.tolist()
sales.plot(kind='pie',startangle=90,labeldistance=1.1,autopct='%1.1f%%',pctdistance=0.9)
plt.ylabel('')
for text in plt.gca().texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

plt.show()
