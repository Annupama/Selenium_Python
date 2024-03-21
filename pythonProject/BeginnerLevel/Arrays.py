# Arrays are used to store multiple values in one single variable
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
# Modify the value
cars[0] = "Toyota"
x = len(cars)
print(x)
# Looping the array elements
for x in cars:
  print(x)
# Adding array elements
cars.append("Honda")
# Removing array elements
cars.pop(1)
print(cars)
# Accessing the elements in the array
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[0])
print("Access element is: ", a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print("Access element is: ", b[1])
print("Access element is: ", b[2])
# Adding elements to the array
a = arr.array('i', [1, 2, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()
# Counting elements in the array
my_array = arr.array('i', [1, 2, 3, 4, 2, 5, 2])
count = my_array.count(2)
print("Number of occurrences of 2:", count)
# Reversing the elements in the array
my_array = arr.array('i', [1, 2, 3, 4, 5])
print("Original array:", *my_array)
my_array.reverse()
print("Reversed array:", *my_array)
