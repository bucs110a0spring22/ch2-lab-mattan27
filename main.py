import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
print(classes_per_week, type(classes_per_week))
cost_per_class = 37.5
print("Cost per class:", cost_per_class)
print(cost_per_class, type(cost_per_class))

#Part B
my_list = list = ["motorcycle", "keyboard", "legos", "speakers", "water bottle"]
print("Random Item is:", random.choice(my_list))
