# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
words1 = Counter(c for clist in class1 for c in clist)
print(words1)
words2 = Counter(d for dlist in class2 for d in dlist)
print(words2)

# TODO: How many students in class 1 named James?
james = class1.count("James")
print(james)
# TODO: How many students are in class 1?
num_students = len(class1)
print("The number of students in class 1 is:", num_students)

# TODO: Combine the two classes
classes = class1 + class2
print(classes)

# TODO: What's the most common name in the two classes?
name_counts = Counter(classes)
most_common_name = name_counts.most_common(1)[0][0]

print("The most common name in the class is:", most_common_name)

# TODO: Separate the classes again
combined_class = ['Bob', 'James', 'Chad', 'Darcy', 'Penny', 'Hannah', 'Kevin', 'James', 'Melanie', 'Becky', 'Steve',
                  'Frank', 'Bill', 'Barry', 'Cindy', 'Debbie', 'Frank', 'Gabby', 'Kelly', 'James', 'Joe', 'Sam', 'Tara', 'Ziggy']
max_students_per_class = 12

# Split the combined class into separate classes
num_classes = len(combined_class) // max_students_per_class
if len(combined_class) % max_students_per_class != 0:
    num_classes += 1

separated_classes = [combined_class[i * max_students_per_class:(
    i + 1) * max_students_per_class] for i in range(num_classes)]

# Print the separated classes
for i, class_names in enumerate(separated_classes):
    print(f"Class {i+1}: {class_names}")

# TODO: What's common between the two classes?
