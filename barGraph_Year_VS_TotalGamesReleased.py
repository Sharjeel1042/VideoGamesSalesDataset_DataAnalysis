from main import dfTime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

videoGames=dfTime.groupby('year_of_release')['name'].count()
year=videoGames.index.tolist()
totalGamesReleased=videoGames.values.tolist()

fig, ax=plt.subplots(figsize=(10,6))
bars=ax.bar(year,totalGamesReleased,0.7,color='green')
plt.title('Year VS Total Games Released',fontdict={'fontsize':20,'font':'DejaVu Sans Mono'})
plt.xlabel('Year',fontdict={'fontsize':10,'font':'DejaVu Sans'})
plt.ylabel("Number Of Games Released",fontdict={'font':'DejaVu Sans','fontsize':10})
for bar in bars:
    height=bar.get_height()
    ax.set_xticks(year)
    ax.set_xticklabels(year,fontdict={'font':'Georgia','fontsize':7})
    ax.text(
        bar.get_x()+bar.get_width()/2,
        height,
        f'{height}',
        ha='center',
        va='bottom',
        fontdict={'fontsize':7}
    )

plt.show()
