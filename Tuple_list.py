# Tuple vs lists

# languages=("python","Java","C++","Matlab")
# languages[0]="Java"
# print(languages)

#tuple used when we know we will not change value till end of the program - it uses less memory
import sys
a_list = list()
a_tuple = tuple()
a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))
