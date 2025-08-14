import matplotlib.pyplot as plt
from main import dfTime
import pandas as pd
import numpy as np

sales=dfTime.groupby('year_of_release')['global_sales'].sum()

year=sales.index.tolist()
globalSales=sales.values.tolist()

sales.plot(kind='line',marker='x',color='green',markeredgecolor='red')
plt.title('Year VS Global Sales',fontdict={'font':'DejaVu Sans Mono','fontsize':20})
plt.xlabel("Year",fontdict={'fontsize':15})
plt.ylabel("Global Sales\n(million)",fontdict={'fontsize':15})
plt.show()
