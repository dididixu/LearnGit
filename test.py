import numpy as np

h = 32
w = 48

input_2Ddate = np.random.randn(h, w)
output_2Ddate = np.zeros(shape=(h, w))

kern = np.random.randn(3, 3)

padding = np.zeros(shape=(h + 2, w + 2))
padding[1:-1, 1:-1] = input_2Ddate  # 外围全是0

for i in range(h):
    for j in range(w):
        window = padding[i:i + 3, j:j + 3]
        output_2Ddate[i, j] = np.sum(kern * window)
