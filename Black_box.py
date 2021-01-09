import  numpy as np
import random
ten_to_twenty = np.arange(10,21,1)
total_weight = []


for i in range(100):
    single_weight = random.choice(ten_to_twenty)
    total_weight.append(single_weight)

print(len(total_weight))
print(total_weight)
print(total_weight[-1])