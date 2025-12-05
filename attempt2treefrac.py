import math
import matplotlib.pyplot as plt

def plot_complex(origin, end):
    x = [origin.real, end.real]
    y = [origin.imag, end.imag]
    plt.plot(x, y, linewidth=2, color="green")

def tree(origin, branch, angle, scale, rec_factor):
    if rec_factor > 0:
        plot_complex(origin, branch)

        branch_l = ((branch - origin) * math.e ** (1j * angle) * scale) + branch
        branch_r = ((branch - origin) * math.e ** (-1j * angle) * scale) + branch

        tree(branch, branch_l, angle, scale, rec_factor - 1)
        tree(branch, branch_r, angle, scale, rec_factor - 1)

origin = 0 + 0j
first_end = 0 + 0.7j
angle = math.pi / 4.123234334234
scale = 0.7
recursion_factor = 13

tree(origin, first_end, angle, scale, recursion_factor)

plt.axis("equal")
plt.axis("off")
plt.show()
