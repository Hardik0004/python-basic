
import copy

original_list = [1, [2, 3], [4, 5]]
shallow_copy = copy.copy(original_list)

# Find the memory addresses of the original list and shallow copy
address_original = id(original_list)
address_shallow_copy = id(shallow_copy)
shallow_copy[1][1]= 100
print("Shallow copy", shallow_copy)
print("@@@@@@@@@@@@@@")
print("original_list", original_list)
# # Find the memory addresses of the nested lists
# address_inner_original = id(original_list[1])
# address_inner_copy = id(shallow_copy[1])

# print("Memory address of the original list:", hex(address_original))
# print("Memory address of the shallow copy:", hex(address_shallow_copy))
# print("Memory address of the nested list in the original:", hex(address_inner_original))
# print("Memory address of the nested list in the shallow copy:", hex(address_inner_copy))
