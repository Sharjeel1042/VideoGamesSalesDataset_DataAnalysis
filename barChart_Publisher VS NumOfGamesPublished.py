from main import dfNonTime
import matplotlib.pyplot as plt
import pandas as pd

dfNonTime.info()

sales=dfNonTime.groupby('publisher')['name'].count().sort_values(ascending=False)
top3=sales.head(3)
others=sales.iloc[3:].count()
plot=top3._append(pd.Series({'Others':others}))
plt.figure(figsize=(8,5),dpi=150)
plt.bar(plot.index,plot.values,color='yellow',width=0.5)
for i,value in enumerate(plot.values):
        plt.text(i,value,f'{value:.2f}',ha='center',va='bottom')

plt.savefig('BarGraph_Top3HighestSellingPlatforms.png')
plt.show()

