import matplotlib.pyplot as plt


# Scatter Plot :-
# a graph in which the values of two variables are plotted along two axes,
# the pattern of the resulting points revealing any correlation present.

x = [1,2,3,4,5,6,7,8]
y = [7,6,2,6,8,9,4,5]

# To plot the scatter
plt.scatter(x,y, label = "Scatter", color = 'c', marker = '.', s=30)


plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graphs')
plt.legend()
plt.show()
