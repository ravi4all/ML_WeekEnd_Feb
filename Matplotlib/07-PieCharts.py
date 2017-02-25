import matplotlib.pyplot as plt


days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]


slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']

colors = ['r','m','c','b']

# To plot the pie chart with 90 deg angle ( startangle = 90 )
# explode will slice out the part that you want
# autopct will put percentage on pie
plt.pie(slices,
        labels=activities,
        colors = colors,
        startangle = 90,
        shadow = True,
        explode=(0,0.1,0,0),
        autopct = '%1.1f%%')

plt.title('Pie Chart')
plt.legend()
plt.show()
