import numpy 

a = numpy.array([[2,10,20],[80,43,31],[22,43,10]])

print("The original array:\n")
print(a)


print("\nThe minimum element among the array:",numpy.amin(a))
print("The maximum element among the array:",numpy.amax(a))

print("\nThe minimum element among the rows of array",numpy.amin(a,0))
print("The maximum element among the rows of array",numpy.amax(a,0))

print("\nThe minimum element among the columns of array",numpy.amin(a,1))
print("The maximum element among the columns of array",numpy.amax(a,1))