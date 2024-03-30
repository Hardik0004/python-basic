import copy

original_list = [1, [2, 3], [4, 5]]
deep_copy = copy.deepcopy(original_list)

# Find the memory addresses of the original list and deep copy
address_original = id(original_list)
address_deep_copy = id(deep_copy)
deep_copy[1][1]= [100]
print(deep_copy)
print("@@@@@@@@@")
print("Original list", original_list)
# Find the memory addresses of the nested lists
address_inner_original = id(original_list[1])
address_inner_copy = id(deep_copy[1])

print("Memory address of the original list:", hex(address_original))
print("Memory address of the deep copy:", hex(address_deep_copy))
print("Memory address of the nested list in the original:", hex(address_inner_original))
print("Memory address of the nested list in the deep copy:", hex(address_inner_copy))
