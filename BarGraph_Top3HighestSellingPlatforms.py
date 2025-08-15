import pandas as pd
from main import dfNonTime
import matplotlib.pyplot as plt

dfNonTime.info()
sales=dfNonTime.groupby('platform')['global_sales'].sum().sort_values(ascending=False)
top3=sales.head(3)
others=sales.iloc[3:].sum()
plot=top3._append(pd.Series({'Others':others}))

plt.figure(figsize=(10,5),dpi=150)
plt.bar(plot.index,plot.values,color='skyblue')
plt.xlabel('Platform',fontdict={'fontsize':15,'font':'DejaVu Sans'})
plt.ylabel('Global sales\n(million)',fontdict={'fontsize':15,'font':'DejaVu Sans'})
plt.xticks(fontname='DejaVu Sans', fontsize=10)
plt.yticks(fontname='DejaVu Sans',fontsize=10)
for i,value in enumerate(plot.values):
    plt.text(i,value,f'{value:.2f}',ha='center',va='bottom',fontdict={'fontsize':12.5})

plt.savefig('BarGraph_Top3HighestSellingPlatforms.png')
plt.show()

