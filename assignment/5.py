my_info = ("Bimal", "Subedi", 20)

people = []

people.append(my_info)
people.append(("Sagar", "Karki", 20))
people.append(("Susan", "Shakya", 20))

people.sort(key=lambda x: x[-1])

print(people)
