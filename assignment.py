# AIML Assessment – Week 2
# NumPy, Pandas & Matplotlib (Single Page Code)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# SECTION 1: NUMPY
# =========================

# 1. Create array from 1 to 20
arr = np.arange(1, 21)
print("Array (1 to 20):", arr)

# 2. Reshape into 4x5 matrix
matrix = arr.reshape(4, 5)
print("\n4x5 Matrix:\n", matrix)

# 3. Mean, Median, Standard Deviation
print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# 4. Extract even numbers
even_numbers = arr[arr % 2 == 0]
print("\nEven Numbers:", even_numbers)

# 5. Random 5x5 m
