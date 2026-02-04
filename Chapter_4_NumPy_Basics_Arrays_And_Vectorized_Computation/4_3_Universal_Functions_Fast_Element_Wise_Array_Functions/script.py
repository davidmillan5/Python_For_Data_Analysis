import numpy as np

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

