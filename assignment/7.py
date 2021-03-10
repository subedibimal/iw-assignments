my_friends = [("Anish", "Ghimire", 20), ("Sagar"), ("Karki"), 18]

age_sum = 0
for fname, lname,age in my_friends:
    if age:
        age_sum += age

avg_age = age_sum / len(my_friends)

print(f"Average Age: {avg_age}")
