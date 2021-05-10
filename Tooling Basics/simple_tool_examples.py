import numpy as numpy
x = np.array([[1,2,3], [4,5,6]])
print("x:\n{}".format(x))

# SciPy

from scipy import sparse

# create a 2d numpy array witha  diagonal of ones, and zeroes everywhere else
eye = np.eye(4)
print("Numpy array:\n", eye)

#Convert the Numpy array to a SciPy sparse matrix in CSR format
# Only the nonzero entries are stored 
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n", sparse_matrix)

data = np.ones(4)
row_indicies = np.arrange(4)
col_indicies = np.arrange(4)
eye_coo = sparse.coo_matrix((data, (row_indicies, col_indicies)))
print("COO reperesentation:\n", eye_coo)


# Matplotlib

%matplotlib inline
import matplotlib.pyplot as plt 
x = np.linspace(-10, 10 , 100)
y = np.sin(x)

plt.plot(x, y, marker = "x")



# Pandas

import pandas as pandas
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location' : ["new York", "Paris", "Berlin", "London"],
        'Age' : [24, 13, 53, 33]
        }
data_pandas = pd.DataFrame(data)
display(data_pandas)

# select all rows that have an age colun greater than 30
display(data_pandas[data_pandas.Age > 30])