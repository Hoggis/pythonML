
import numpy as np
import matplotlib.pyplot as plt
# define variables to be used later
x = np.arange(0,100)
y = x*2
z = x**2

#Fig one
fig = plt.figure()

#add axes
ax = fig.add_axes([0,0,1,1]) #[left, bottom, width, height]
#format axes
#extra for readability practice, not actually asked for
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('First fig')
ax.plot(x,y)

#Fig two
fig = plt.figure()

#add axes
ax1 = fig.add_axes([0,0,1,1]) # bigger canvas axes
ax2 = fig.add_axes([0.2,0.5,.2,.2]) # inner canvas axes

#format axes
#outer figure
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Second fig')

#inner figure
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Inner fig')

#plotting
ax1.plot(x,y, 'r')
ax2.plot(x,y, 'r')

#Fig three
fig = plt.figure()

#add axes
ax1 = fig.add_axes([0,0,1,1]) # bigger canvas axes
ax2 = fig.add_axes([0.2,0.5,.4,.4]) # inner canvas axes

#format axes
#outer figure
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Second fig')

#inner figure
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Inner fig')

#set limits for the inner canvas axes
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)

#plotting
ax1.plot(x,z)
ax2.plot(x,y)



#Fig 4, create two figures side by side
fig, axes = plt.subplots(nrows=1, ncols=2)


#formatting left figure
axes[0].set_xlabel('x[0]')
axes[0].set_ylabel('y[0]')
axes[0].set_title('title[0]')

#formatting right figure
axes[1].set_xlabel('x[1]')
axes[1].set_ylabel('y[1]')
axes[1].set_title('title[1]')

#plotting
axes[0].plot(x, y, 'b', lw=3, ls='--')
axes[1].plot(x, z, 'r', lw=3, ls='--')

#sets graphs side by side and not on top of each other
plt.tight_layout()

#Fig five, same as previous but figsize is different
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,3))

#formatting left figure
axes[0].set_xlabel('x[0]')
axes[0].set_ylabel('y[0]')
axes[0].set_title('title[0]')

#formatting right figure
axes[1].set_xlabel('x[1]')
axes[1].set_ylabel('y[1]')
axes[1].set_title('title[1]')

axes[0].plot(x, y, 'b', linestyle='-')
axes[1].plot(x, z, 'r', linestyle= '--')

plt.tight_layout()

plt.show()