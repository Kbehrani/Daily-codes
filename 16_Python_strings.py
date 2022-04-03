text= "Hello there"
print(text)

text ="He said, \"what\'s there?\" "
print(text)

#access characters from string

text="Python"
print(text[0])
print(text[3])

#slicing of string
print(text[1:4])
print(text[:6])

#strings are immutable - can't change its value like tuples

#python string operations
#string concatenation 

text1="Python"
text2="Programming"
result=text1+" " + text2
print(result)

text="Python"
new_text= text*3
print(new_text)

#Iteration through string

# use for loop

text="Python"
print(len(text))

for character in text: 
    print(character)

print("P" in text)
print("ont" in text)

#Python string methods
text="I Like python 3"
result= text.lower()
result1=text.upper()
print(result)
print(result1)
