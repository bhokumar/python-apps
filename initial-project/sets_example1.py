set1 = {1, 2, 3, 4, 5, 6}
set1.remove(1)

print(set1)

print(set1.add(1))

maths_students = {"Mathew", "Helen", "Prashant", "James", "Aparna"}

biology_students = {"Jane", "Mathew", "Charlotte", "Mesut", "Oliver", "James"}

print(maths_students | biology_students)

print(maths_students & biology_students)

print({x**2 for x in range(10)})

print({val.upper() for val in "hello"})