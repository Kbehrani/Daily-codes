#remember these things about sets
#1 items of a set are in no particular order
#2 no duplicates are allowed
#3 items must be immutable objects

animals={"dog","cat","tiger","elephant","dog"} #diuplicate value would be removed
print(animals)

animals=set()
print(animals)

animals=set(["cat","dog"]) #adding a list inside this set function
print(animals)
#sets are mutable - we can add/remmove from them
animals={"dog","cat","tiger","elephant","dog"} #duplicate value would be removed
animals.add("monkey")
print(animals)

animals={"dog","cat","elephant"}
wild_animals ={"tiger","leopard", "elephant"}

animals.update(wild_animals,{"dolphins"})
print(animals)

#discard method to remove 
# animals.discard("cat")
# print(animals)

# animals.remove("cat")
# print(animals)
# #to remove all
# animals.clear()
# print(animals)

domestic_animals={"dog","cat","elephant"}
wild_animals={"lion","tiger","elephant"}
animals=domestic_animals.union(wild_animals)

print(animals)

#intersection of sets 
domestic_animals={"dog","cat","elephant"}
wild_animals={"lion","tiger","elephant"}
# animals=domestic_animals.intersection(wild_animals)
animals=domestic_animals & wild_animals

print(animals)


