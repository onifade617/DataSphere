import seaborn as sns


#get the pre-installed Dow Jones dataset on sns
dow_jones = sns.load_dataset("dowjones")
print(dow_jones.head())


#get the pre-installed Dow Jones dataset on sns
flights = sns.load_dataset("flights")
print(flights.head())


#get the pre-installed Planets dataset on sns
planets = sns.load_dataset("planets")
print(planets.head())


#get the pre-installed Dow Jones dataset on sns
health = sns.load_dataset("healthexp")
print(health.head())