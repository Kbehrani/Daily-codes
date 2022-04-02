# Tuple vs lists

languages=("python","Java","C++","Matlab")
languages[0]="Java"
print(languages)

#tuple used when we know we will not change value till end of the program - it uses less memory
#tuple is more efficient
import sys
a_list = list()
a_tuple = tuple()
a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

mixed_list = ["Hello", -34, "Java", True]

print("1.", mixed_list[-1])

mixed_list[1] = "Hi"
print("2.", mixed_list)

mixed_tuple = (1, 3, 4, 5)

mixed_tuple[1] = 100
print("3.", mixed_tuple)
