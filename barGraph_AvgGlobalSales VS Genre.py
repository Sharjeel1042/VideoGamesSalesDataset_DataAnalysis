from main import dfNonTime
import matplotlib.pyplot as plt


plt.rcParams['xtick.labelsize']=10
plt.rcParams['xtick.labelcolor']='red'
plt.rcParams['ytick.labelsize']=10
plt.rcParams['ytick.labelcolor']='red'
plt.rcParams['font.family']='DejaVu Sans Mono'

sales=dfNonTime.groupby('genre')['global_sales'].mean().sort_values(ascending=False)
genre=sales.index.tolist()
avgGlobalSales=sales.values.tolist()

fig, ax=plt.subplots(figsize=(13,7),dpi=100)
bars=ax.bar(genre,avgGlobalSales,width=0.5,color='yellow')
plt.xlabel('Genre',fontdict={'fontsize':15,'font':'Comic Sans MS'})
plt.ylabel('Avg.Global Sales\n(millions)',fontdict={'fontsize':15,'font':'Comic Sans MS'})



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
plt.savefig('barGraph_AvgGlobalSales VS Genre.png')