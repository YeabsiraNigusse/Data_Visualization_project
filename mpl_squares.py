import matplotlib.pyplot as plt

square = [1, 4, 9, 16, 25]
inputs = [1,2,3,4,5]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(inputs,square, linewidth = 3)
ax.set_title('square numbers', fontsize = 24)
ax.set_xlabel('value', fontsize = 14)
ax.set_ylabel('square of value', fontsize = 14)
ax.tick_params(axis= 'both', labelsize = 14)
plt.show()
    