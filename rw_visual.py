import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig,ax = plt.subplots(figsize = (15,9))
point_numbers = range(rw.num_of_ponts)

ax.scatter(rw.x_values,rw.y_values,c= point_numbers,cmap = plt.cm.Blues,edgecolors = 'none',s=15)
plt.show()