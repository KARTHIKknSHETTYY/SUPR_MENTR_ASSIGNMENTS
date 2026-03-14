import time
import numpy as np

# Python list
python_list = list(range(1000000))

start = time.time()
result = [x * 2 for x in python_list]
end = time.time()

print("Python list execution time:", end - start)

# NumPy array
numpy_array = np.arange(1000000)

start = time.time()
result = numpy_array * 2
end = time.time()

print("NumPy array execution time:", end - start)