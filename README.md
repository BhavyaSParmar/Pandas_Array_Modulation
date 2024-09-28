# Python-Pandas

Creating Numpy Arrays
Operation 1: Convert a Python list [[1,2,3],[4,5,6]] into a NumPy array.
This involves converting a standard Python list into a structured NumPy array for efficient numerical operations.
Output: A 2D NumPy array.
Operation 2: Create a 3x2 2D array filled with numbers from 1 to 6.

Operation: np.arange(1,7).reshape(3,2) creates a 2D array from a sequence of numbers (1 to 6).
Output: A 3x2 NumPy array with shape (3,2).

Operation 3: Create an array of even numbers from 2 to 100 and find the mean value.
Operation: np.arange(2, 101, 2) generates even numbers between 2 and 100, and np.mean() computes the average.
Output: Mean of the generated even numbers.

Operation 4: Create a 3x3x3 array with random float values, and find the minimum and maximum values in the array.
Operation: np.random.random((3,3,3)) generates a 3D array with random numbers. The minimum and maximum values are found using np.min() and np.max().
Output: The 3D array and its minimum and maximum values.

Operation 5: Create a 3x4 2D array filled with values from 10 to 21 (inclusive).
Operation: np.arange(10,22).reshape(3,4) creates and reshapes a sequential array of values.
Output: A 3x4 array with values from 10 to 21.

Operation 6: Create a 1D array of length 10 starting from 5 with a step of 3 between consecutive numbers.
Operation: np.arange(5,35,3) generates numbers starting at 5 with steps of 3.
Output: A 1D array of length 10.

Operation 7: Create a 10x10 array filled with random values and calculate the memory size of the array.
Operation: np.random.random((10,10)) generates the array, and x.nbytes computes its memory usage.
Output: The 10x10 array and its memory size in bytes.

Operation 8: Create a 1D array of size 10 where the fifth value is specifically set to 5.
Operation: x[4] = 5 manually sets the fifth element of the array to 5.
Output: A modified 1D array with the fifth value as 5.

Operation 9: Create an array with values ranging from 10 to 49 and reverse the array.
Operation: np.arange(10,50)[::-1] creates the array and reverses it.
Output: A reversed array ranging from 49 to 10.

Operation 10: Create a 3x2 array with random values from a uniform distribution.
Operation: np.random.random((3, 2)) generates a 2D array with random float numbers between 0 and 1.
Output: A 3x2 array with random values.

Summary:
The script focuses on generating and manipulating NumPy arrays in various shapes, sizes, and data types.
It involves common operations such as reshaping, slicing, finding mean, minimum, and maximum values, and working with random values.
This exploration emphasizes basic and intermediate array manipulation techniques used in data analysis, particularly in scientific computing.
