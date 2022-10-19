import csv
import matplotlib.pyplot as plt
from datetime import datetime

sitka = r'C:\Users\User\Desktop\python\Projects\Data_Visualization\data\sitka_weather_2018_simple.csv'
deathvally = r'C:\Users\User\Desktop\python\Projects\Data_Visualization\data\death_valley_2018_simple.csv'

with open(sitka) as f1:
    reader = csv.reader(f1) 
    Shigh, dates = [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
         high = int(row[5])
        except ValueError:
            print('error 1')
        else:
          Shigh.append(high)
          dates.append(current_date)

with open(deathvally) as f2:
    reader = csv.reader(f2)
    Dhigh = []
    for row in reader:
        try:
            high = int(row[4])
        except ValueError:
            pass
        else:
            Dhigh.append(high)
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,Shigh, c= 'blue', alpha = 0.5)
ax.plot(dates, Dhigh, c = 'red', alpha = 0.5)
plt.fill_between(dates, Shigh, Dhigh, facecolor = 'blue', alpha = 0.1)
plt.title('Daily high and low Temprature - 2018', fontsize = 14)
fig.autofmt_xdate()
plt.xlabel('', fontsize = 14)
plt.ylabel('Tempratur(F)', fontsize = 14)
plt.tick_params(axis='both', which = 'major', labelsize = 16)
plt.show()
