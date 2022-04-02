# python local and global variables 

# message="How are you doing?"

# def greet():
#     message="How are you"
#     print("Inside message", message)

# greet()
# print("Outside message", message)

# Global and Local variables
# def add_numbers(n1,n2):
#     result=n1+n2
#     return result
# output=add_numbers(2,5)
# print(output)

#Lists & Tuples in python - compound data types 

# numbers= [1,5,6,-4]
# print(numbers)


# random_list=[2.5,"hello",-5,2.5]
# print(random_list)

languages=["Python","C++","Java",".Net"]
#print(languages)

#index
print(languages[1])
#negative indexing
print(languages[-3])

print(languages[0:3]) #starting index is inclusive, last in exclusive
print(languages[1:3])
print(languages[:3]) #blank starting index is read as 0

#change items in a list

#lists are mutable objects
languages[1]="Ruby"
print(languages)

#iterate through list
languages=["Python","C++","Java",".Net"]
# print("Python" in languages)
# print("Rust" in languages)

for language in languages:
    print(language)

#list methods
languages=["Python","C++","Java",".Net"]
languages.append("Rust")
print(languages)
languages.insert(1,"Rust")
print(languages)
