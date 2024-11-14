import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/RK/Downloads/matches.csv")
matches_per_season=data.groupby("Season").size().reset_index(name='Match_Count')
print(matches_per_season)
plt.bar(matches_per_season['Season'],matches_per_season['Match_Count'])
plt.xlabel('season')
plt.ylabel('number of matches')
plt.title('number of matches in each season')
plt.show()