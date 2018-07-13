#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%
data = pd.read_csv('Data/stats.csv').iloc[:,1:]
data
#%%
data = data[data['Games'] > 50].sort_values(by=['Games'], ascending=False)
data
#%%
# plt.plot(data['Games'], (data['Mafia_wins'] + data['Don_wins']) / (data['Mafia_games'] + data['Don_games']))
# plt.plot(data['Games'], (data['Citizen_wins'] + data['Sheriff_wins']) / (data['Citizen_games'] + data['Sheriff_games']))

plt.plot(data['Games'], data['Citizen_games'] / data['Games'])
plt.show