import numpy as np

#1 Save and Write Files
#Example 1, save numbers
# file_data = np.array([4, 1, 14, 2, 30])
np.save("file.npy", file_data)
loaded_data = np.load("file.npy")
print("file:", loaded_data)

#Example 2, save characters
file_data = np.array([["Kissy"], ["Kim"], ["Alliah"], ["Van"]])
np.save("file.npy", file_data)
loaded_data = np.load("file.npy")
print("file:", loaded_data)

#Example 3, save data to text file
data = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt("file.txt", data, delimiter=" ")


# #2 Load File
#Example 1, load file
loaded_data = np.load("file.npy")
print("loaded file:", loaded_data)

#Example 2, using loadtxt 
data = np.loadtxt("file.txt")
print(data)

#Example 3, using genfromtext, specific data
data = np.genfromtxt("file.txt", max_rows=1, usecols=(0, 2))
print(data)


