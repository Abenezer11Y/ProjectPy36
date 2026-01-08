import array as arr

array1 = arr.array("i", [1, 2, 3, 4, 5, 6, 3, 5, 1, 3,])
print(f"The original array is: {str(array1)}")
print(f"The amount of times cherry was seen was: {str(array1.count(3))}")

array1.reverse()
print("When we reverse it:", str(array1))