import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 9]

# plt.plot(x, y, marker='^', linestyle='-')  #plt.plot() 기본적으로 점들을 선으로 연결 
# plt.title('Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# plt.scatter(x, y, marker="o", color="red")
# plt.title('Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# plt.bar(x, y, color="skyblue")
# plt.title('Bar Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()


# data = np.random.randn(1000)
# plt.hist(data, bins=30, color="green", alpha=0.5)
# plt.title('Histogram')
# plt.xlabel("Value")
# plt.ylabel('Frequency')
# plt.show()


x = np.linspace(0, 2 * np.pi, 400)
# y1 = np.sin(x**2)
# y2 = np.cos(x**2)

# fig, axes = plt.subplots(2, 2)
# axes[0,0].plot(x, y1, 'tab:blue')
# axes[0,0].set_title('Axes[0,0]')
# axes[0,1].plot(x, y2, 'tab:orange')
# axes[0,1].set_title('Axes[0,1]')
# axes[1,0].plot(x, -y1, 'tab:green')
# axes[1,0].set_title('Axes[1,0]')
# axes[1,1].plot(x, -y2, 'tab:red')
# axes[1,1].set_title('Axes[1,1]')

# for ax in axes.flat :
#   ax.set(xlabel='x-axis', ylabel='y-axis')
#   ax.label_outer()

# plt.show()


fig, ax1 = plt.subplots()
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color='tab:red')
ax1.plot(x, np.sin(x), color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx() # x축 공유
ax2.set_ylabel('cos(x)', color='tab:blue')
ax2.plot(x, np.cos(x), color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

fig.tight_layout()
plt.show()