import numpy as np
arr_a = np.array([10, 20, 30])
arr_b = np.array([2, 4, 6])

# Element-wise operations
print("Addition:", arr_a + arr_b)
print("Multiplication:", arr_a * arr_b)

# Statistical functions
delays = np.array([1.2, 1.5, 0.9, 2.1])
print(f"Max Delay: {np.max(delays)} | Average Delay: {np.mean(delays)}")
