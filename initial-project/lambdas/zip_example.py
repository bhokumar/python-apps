first_zip = zip([1, 2, 3], [4, 5, 6])

zipped_list = list(first_zip)

print(zipped_list)

zipped_dict = dict(zip([1, 2, 3], [4, 5, 6]))

print(zipped_dict)


midterm = [80, 91, 78]
finals = [98, 89, 53]

student = ['dang', 'ang', 'kate']

final_grade = {pair[0]: max(pair[1], pair[2]) for pair in zip(student, midterm, finals)}

print(final_grade)
zipped_student_scores = zip(
    student,
    map(
        lambda pair: max(pair),
        zip(midterm, finals)
    )
)

zipped_scores_dict = {pair[0]: pair[1] for pair in zipped_student_scores}
print("Scores {}" .format(zipped_scores_dict))

print("".join(['a', 'b', 'c', 'd']))

#raise ValueError("Error while reading value")