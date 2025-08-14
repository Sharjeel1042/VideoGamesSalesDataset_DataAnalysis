import matplotlib.pyplot as plt
from main import dfNonTime
import pandas as pd

sales={
    'North-America':dfNonTime['na_sales'].sum(),
    'Europe':dfNonTime['eu_sales'].sum(),
    'Japan':dfNonTime['jp_sales'].sum(),
    'Other':dfNonTime['other_sales'].sum()
}

sales_series=pd.Series(sales)
plt.figure(figsize=(15,5),dpi=150)
sales_series.plot(kind='pie',autopct='%1.1f%%',startangle=90,
                  textprops={'color':'black','fontsize':12,'weight':'bold'})
plt.title('Global Sales By Region',fontdict={'font':'DejaVu Sans Mono','fontsize':20,'weight':'bold'})
plt.ylabel('')

plt.show()
plt.savefig('PieChart_GlobalSalesByRegion.png',dpi=150)
