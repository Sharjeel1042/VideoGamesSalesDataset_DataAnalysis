from main import dfNonTime
import pandas as pd
import matplotlib.pyplot as plt

sales=dfNonTime.groupby('name')['global_sales'].sum().sort_values(ascending=False)
top3=sales.head(10)
others=sales.iloc[10:].sum()
plot=top3._append(pd.Series({'Others':others}))

plt.figure(figsize=(10,2))
plt.bar(plot.index,plot.values,color='skyblue')
plt.title('Top 10 Games Sold Globally')
plt.xticks(rotation=90)
plt.xlabel('Game Name')
plt.ylabel('Global Slaes\n(millions)')
for i,value in enumerate(plot.values):
    plt.text(i,value,f'{value:.2f}',ha='center',va='bottom')

plt.grid(axis='y',color='black',linestyle='solid',linewidth=0.5)
plt.savefig('barGraph_Top10GamesGlobally.png',dpi=150)
plt.show()
