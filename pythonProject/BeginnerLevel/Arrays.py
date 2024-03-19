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
