#17: Python Dictionaries to Store key/value Pairs | Python for Beginners

person1={"name":"linus", "age":21}
print(person1)
# person1={"name": "linus", "age": 21}
# # print(person1["name"])
# print(person1.get("hobbies"))
# print(person1.get("hobbies", ["dancing", "fishing"]))

# person2={10:"linus", ("age"):21}
# print(person2)

# add and change dictionary elemets
person1={"name": "linus", "age": 21}
# person1["name"]="dennis"
# print(person1)
person1["hobbies"]= ["dancing", "fishing"]
# print(person1)

#removing an item from the dictionary
# using pop method


for key in person1:
    print(key)
    print(person1[key])
