names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random


random_name = random.choice(names).title()
print(f"{random_name} is paying the bill for your meal!")