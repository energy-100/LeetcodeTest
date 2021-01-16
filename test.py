a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]

print((1,1) in zip(a,b))

import numpy as np
from collections import Counter

data = np.array([1.1, 1.1, 1.1, 2, 3, 5, 4, 4, 4, 5])

# 方法一
print('Counter(data)\n', Counter(data))  # 调用Counter函数
