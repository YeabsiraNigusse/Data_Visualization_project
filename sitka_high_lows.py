import matplotlib.pyplot as plt
from datetime import datetime
import csv

path = r'C:\Users\User\Desktop\python\Projects\Data_Visualization\data\death_valley_2018_simple.csv'
with open(path) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
           low = int(row[5])
           high = int(row[4])
        except:
            print(f'missing data for {current_date}')
        else:
          highs.append(high)
          lows.append(low)
          dates.append(current_date)
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs, c= 'blue', alpha = 0.5)
ax.plot(dates, lows, c = 'red', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
plt.title('Daily high and low Temprature - 2018', fontsize = 14)
fig.autofmt_xdate()
plt.xlabel('', fontsize = 14)
plt.ylabel('Tempratur(F)', fontsize = 14)
plt.tick_params(axis='both', which = 'major', labelsize = 16)
plt.show()