import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys

# 6x1 grid with starting point (0,0)
##ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
##ax2 = plt.subplot2grid((6,1), (1,0), rowspan=3, colspan=1)
##ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)


# Add subplot
# 111 - Height, Width, Plot
# 211 - Will add another subplot
# 212 - New subplot divide with height
##ax1 = fig.add_subplot(211)
##ax2 = fig.add_subplot(212)

# If we need 2 graph on top and 1 with full width then :-
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)


x,y = create_plots()
ax1.plot(x,y)

x,y = create_plots()
ax2.plot(x,y)

x,y = create_plots()
ax3.plot(x,y)

plt.show()
