from main import dfTime
import matplotlib.pyplot as plt

sales=dfTime.groupby('year_of_release').sum(numeric_only=True)
plt.figure(figsize=(12,4),dpi=150)
plt.plot(sales.index,sales['na_sales'],label='North America',color='green',marker='o',markeredgecolor='yellow')
plt.plot(sales.index,sales['eu_sales'],label='Europe',color='blue',marker='o',markeredgecolor='yellow')
plt.plot(sales.index,sales['jp_sales'],label='Japan',color='red',marker='o',markeredgecolor='yellow')
plt.plot(sales.index,sales['other_sales'],label="Others",color='black',marker='o',markeredgecolor='yellow')
plt.xlabel('Year',fontdict={'fontsize':15,'font':'DejaVu Sans Mono'})
plt.ylabel('Sales\n(million)',fontdict={'fontsize':15,'font':'DejaVu Sans Mono'})
plt.legend()
plt.show()
plt.savefig('LineGraph_Year VS RegionalSales.png',dpi=150)



