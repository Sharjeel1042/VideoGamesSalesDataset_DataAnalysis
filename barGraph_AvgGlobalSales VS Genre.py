from main import dfNonTime
import matplotlib.pyplot as plt

sales=dfNonTime.groupby('genre')['global_sales'].mean()
genre=sales.index.tolist()
avgGlobalSales=sales.values.tolist()

fig, ax=plt.subplots(figsize=(13,7),dpi=100)
bars=ax.bar(genre,avgGlobalSales,width=0.5,color='yellow')
plt.xlabel('Genre')
plt.ylabel('Avg.Global Sales\n(millions)')
for bar in bars:
    height=bar.get_height()
    ax.text(
    bar.get_x()+bar.get_width()/2,
    height,
    f'{height:.2f}',
    ha='center',
    va='bottom'
    )




plt.show()