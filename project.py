import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv')

Arizona = data[data.Jurisdiction == "Arizona"] # grabs all the rows within Arizona
Arizona2020 = Arizona[Arizona.Year == 2020]
ArizonaMean = Arizona2020["New registered voters"].mean()


California = data[data.Jurisdiction == "California"] # grabs all the rows within Arizona
California2020 = California[California.Year == 2020]
CaliforniaMean = California2020["New registered voters"].mean()

print("The mean amount of new voters in Arizona 2020 was " + str(ArizonaMean)) 
print("The mean amount of new voters in California 2020 was " + str(CaliforniaMean)) 