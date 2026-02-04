import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
print(arr)


print('===============================================================')

print(np.sqrt(arr))

print('===============================================================')

print(np.exp(arr))

print('===============================================================')

rng = np.random.default_rng(seed=12345)
x = rng.standard_normal(8)
print(x)

print('===============================================================')

y = rng.standard_normal(8)

print(y)

print('===============================================================')

print(np.maximum(x,y))


print('===============================================================')


arr = rng.standard_normal(7) * 5
print(arr)

print('===============================================================')

remainder, whole_part = np.modf(arr)

print(remainder)

print(whole_part)

print('===============================================================')

# Array-Oriented Programming With Arrays

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)

print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)

print(z)

plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.close("all")