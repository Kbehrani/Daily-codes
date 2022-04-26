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

learnt something new today
