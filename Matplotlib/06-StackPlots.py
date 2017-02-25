import matplotlib.pyplot as plt


days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([], [], color='r', label = 'Sleeping', linewidth = 5)
plt.plot([], [], color='m', label = 'Eating', linewidth = 5)
plt.plot([], [], color='c', label = 'Working', linewidth = 5)
plt.plot([], [], color='b', label = 'Playing', linewidth = 5)

# days will be x-axis and rest is y-axis
plt.stackplot(days, sleeping, eating, working, playing, colors = ['r','m','c','b'])

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graphs')
plt.legend()
plt.show()
