instructor = {
    "name": "Bhoopendra",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarous": False,
    44: "My favorite number"
}

#instructor["address"]

print("name" in instructor)

print(4 in instructor.values())

#instructor.clear()

print(instructor)

instructor1 = instructor.copy()

#instructor1.clear()

print(instructor)
#print(instructor1)

print(instructor1 == instructor)

print(instructor1 is instructor)