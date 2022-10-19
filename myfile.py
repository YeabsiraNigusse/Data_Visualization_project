import csv
import matplotlib.pyplot as plt

path = r'C:\Users\User\Desktop\python\Projects\Data_Visualization\data\GHCND_sample_csv.csv'
with open(path) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    prcpitation = []
    for row in reader:
      prcp = float(row[8])
      prcpitation.append(prcp)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(prcpitation, c = 'blue')
ax.set_title('Prcpitation', fontsize = 14)
ax.set_xlabel('',fontsize = 16)
ax.set_ylabel('prciptation', fontsize = 16)
plt.tick_params(axis='both', which = 'major',labelsize = 16)
plt.show()

