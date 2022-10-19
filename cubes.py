import matplotlib.pyplot as plt


x_values = range(1,5000)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap = plt.cm.Blues,linewidth = 3)
ax.set_title('Cubes',fontsize = 24)
ax.set_xlabel('cubes', fontsize = 14)
ax.set_ylabel('cubes of numbers', fontsize = 14)
ax.tick_params(axis='both',which = 'major',labelsize = 14)
plt.show()