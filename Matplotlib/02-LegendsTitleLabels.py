import matplotlib.pyplot as plt


x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y, label="First Line")
plt.plot(x2,y2, label="SecondLine")

# For x-axis
plt.xlabel('X-Axis')
# For y-axis
plt.ylabel('Y-Axis')
# For title
plt.title('First Graph\nDemo')
# Making legends
plt.legend()
plt.show()
