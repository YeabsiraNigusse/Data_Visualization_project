import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
x_value  = range(1,1001)
y_value = [x**2 for x in x_value]
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues, s=10)
ax.set_title('square numbers', fontsize = 24)
ax.set_xlabel('value', fontsize = 14)
ax.set_ylabel('square of value', fontsize = 14)
ax.tick_params(axis= 'both',  which = 'major', labelsize = 14)
ax.axis([0,1100,0,1100000])
plt.show()