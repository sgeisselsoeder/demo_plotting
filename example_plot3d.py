import numpy as np
import matplotlib.pyplot as plt


x = np.random.random((100, 3))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xs = x[:, 0]
ys = x[:, 1]
zs = x[:, 2]
ax.scatter(xs, ys, zs)

ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_xlabel('X Label', fontsize=20, labelpad=20)
ax.set_ylabel('Y Label', fontsize=20, labelpad=20)
ax.set_zlabel('Z Label', fontsize=20, labelpad=20)

plt.xticks([0, 0.4, 0.7, 1.2])
plt.yticks(size='5')

# plt.show()
plt.savefig("funny_scatter")
